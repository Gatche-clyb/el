# скрипт для установки программы-тренажера для умножения

Set-PSDebug -Trace 0
$ProgressPreference = 'SilentlyContinue'

function Update-Environment {
    # В основном используется для обновления Path
    $locations = 'HKLM:\SYSTEM\CurrentControlSet\Control\Session Manager\Environment',
                 'HKCU:\Environment'

    $locations | ForEach-Object {
        $k = Get-Item $_
        $k.GetValueNames() | ForEach-Object {
            $name  = $_
            $value = $k.GetValue($_)

            if ($userLocation -and $name -ieq 'PATH') {
                $Env:Path += ";$value"
            } else {
                Set-Item -Path Env:$name -Value $value
            }
        }
        $userLocation = $true
    }
}

# скачивание дистрибутивов, если они еще не скачаны
function download_dist {
    param (
        [HashTable]$package
    )
    $name = $package.Name
    $sha1 = $package.sha1
    if (Test-Path $package.OutFile) {
        $current_sha1 = (Get-FileHash $package.OutFile -Algorithm SHA1).Hash
        if ($current_sha1 -eq $package.sha1) {
            Write-Warning "Дистрибутив $name уже скачан и отпечаток совпал."
            return
        } else {
            Write-Warning "Дистрибутив $name`: Это не ожидаемый нами файл. Ожидаемый sha1=$sha1 текуший sha1=$current_sha1  Переименовываем и перескачиваем."
            $time_stamp = Get-Date -Format "_yyMMdd-HHmmss-"
            $time_zone = (Get-TimeZone).BaseUtcOffset.TotalMinutes
            $time_stamp += $time_zone 
            $NewName= $package.OutFile + $time_stamp
            Write-Warning "Новое имя файла: $NewName"
            Rename-Item -Path $package.OutFile -NewName $NewName
            Invoke-WebRequest -Uri $package.Uri -OutFile $package.OutFile
            $current_sha1 = (Get-FileHash $package.OutFile -Algorithm SHA1).Hash
            if ($current_sha1 -eq $package.sha1) {
                Write-Warning "Дистрибутив $name успешно перескачан и отпечаток совпал."
            } else {
                Write-Warning "Ой-ой. А дистрибутив $name в источнике поменялся."
            }
        }
    } else {
        Invoke-WebRequest -Uri $package.Uri -OutFile $package.OutFile
        $current_sha1 = (Get-FileHash $package.OutFile -Algorithm SHA1).Hash
        if ($current_sha1 -eq $package.sha1) {
            Write-Warning "Дистрибутив $name успешно скачан и отпечаток совпал."
        } else {
            Write-Warning "Ой-ой. А дистрибутив $name в источнике поменялся."
        }
    }
}
$files=@(
    @{
        Name="git"
        Uri="https://github.com/git-for-windows/git/releases/download/v2.47.1.windows.2/Git-2.47.1.2-64-bit.exe"
        OutFile="$HOME\Downloads\git_win64.exe"
        sha1="C9809C87D15D2D64BA3D753BA33800D1F3A71876"
    },
    @{
        Name="python"
        Uri="https://www.python.org/ftp/python/3.13.2/python-3.13.2-amd64.exe"
        OutFile="$HOME\Downloads\python_win64.exe"
        sha1="E3BC24FBC7FAA31A3533334F8E959E53F9564B9E"
    },
    @{
        Name="git_settings"
        URI="https://gifara.ru/7/wingit_defaultsettings.cfg"
        OutFile="$HOME\Downloads\git_settings2instal.cfg"
        sha1="227E2CE39B08334264F68D1A8FCE2A3E03960A8D"
    }

)
foreach ($file in $files) {
    download_dist -package $file
}

# установка git и python
try {git --version} catch{
    & $HOME\Downloads\git_win64.exe /SILENT /NOCANCEL /LOADINF="$HOME\Downloads\git_settings2instal.cfg" | out-null
    # out-null в конвеере нужен, чтобы дождаться завершения установки (иначе запустится в фоне)
}

$python_version = (python --version 2> $null)
if ( [string]::IsNullOrEmpty($python_version) ) {
    #& $HOME\Downloads\python_win64.exe /passive PretendPath=1 | out-null
    & $HOME\Downloads\python_win64.exe /passive PrependPath=1 | out-null
} else {
    Write-Warning  "$python_version"}
Update-Environment

# установка модулей для python и самой программы
python.exe -m pip install --upgrade pip
ssh -o StrictHostKeyChecking=no git@github.com 2> $null
git clone https://github.com/Gatche-clyb/el.git $HOME/el 2> $null
# todo: можно предусмотреть обновление при повторной установке.
pip install colorama
pip install pandas
pip install matplotlib
pip install seaborn

# создание ярлыка на рабочий стол
$WshShell = New-Object -comObject WScript.Shell
$Shortcut = $WshShell.CreateShortcut("$([environment]::GetFolderPath("Desktop"))\el.lnk")
$Shortcut.TargetPath = "python"
$Shortcut.Arguments = "$HOME\el\el.py"
$Shortcut.WorkingDirectory = "$HOME\el"
$Shortcut.Save()
