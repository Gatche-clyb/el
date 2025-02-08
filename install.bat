rem cd %HOMEPATH%\Downloads\
set git_distr=https://github.com/git-for-windows/git/releases/download/v2.47.1.windows.2/Git-2.47.1.2-64-bit.exe
set el_git=git@github.com:Gatche-clyb/el.git
set python_installer=https://www.python.org/ftp/python/3.13.2/python-3.13.2-amd64.exe
powershell Invoke-WebRequest %git_distr%  -OutFile .\git_win64.exe
powershell Invoke-WebRequest %python_installer%  -OutFile .\python_win64.exe
git_win64.exe
python_win64.exe /silent
git clone git@github.com:Gatche-clyb/el.git %HOMEPATH%\el
cd %HOMEPATH%\el
pip install colorama
pip install pandas
pip install matplotlib
pip install seaborn
