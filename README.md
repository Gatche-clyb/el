# Программа-тренажер для помощи в запоминании таблицы умножения

Основная ссылка: [https://github.com/Gatche-clyb/el](https://github.com/Gatche-clyb/el)  
Короткая ссылка (будет перенаправление на основную ссылку): [https://gifara.ru/7/0](https://gifara.ru/7/0)

## Установка

### Windows

* Установить Python:
    * [скачать установщик с официального сайта](https://www.python.org/downloads/windows/ "желательно выбрать последнюю стабильную версию")
    * При установке Python установите флажок `Добавить Python 3.8 в %PATH%`, чтобы иметь возможность запускать скрипты Python из командной строки.
    * Установите дополнительные модули, нужные для работы (из коммандной строки):
        * Откройте коммандную строку. Для этого нажмите "Пуск" и начните набирать powershell. В верху списка отобразиться "Powershell". Кликните на нем. Появится черное окно командной строки. Дождитесь появления приглашения.
        * В командной строке создайте новую директорию, и перейдите в нее:
            * `mkdir el`
            * `cd el`
        * Запустите процесс скачивания и установки дополнительных модулей:
            * `pip install colorama`
            * `pip install pandas`
            * `pip install matplotlib`
            * `pip install seaborn`
* Скачайте [основную программу](https://github.com/Gatche-clyb/el/blob/main/el.py) и переместите ее в созданную папку (C:\Users\Имя_пользователя\el\)

<!--- Многострочный комменарий -->
### Linux (Ubuntu)

* установите python: `sudo apt install python3 python3.12-venv python3-pip`
* установите дополнительные модули: `sudo apt install python3-colorama python3-pandas python3-matplotlib python3-seaborn`
* установите git: `sudo apt install git`
* скачайте последнюю версию программы: `git clone https://github.com/Gatche-clyb/el.git`
* перейдите в папку с программой `cd el`
* создайте виртуальное окружение `python3 -m venv el`
<!-- -->

## Использование

### Windows

* Откройте командную строку (см. выше)
* перейдите в папку `cd el`
* запустить программу `python el.py`
* (при необходимости)
    * удаление статистики `rm otveti.csv`
    * изменение настроек программы `notepad el.py` (отредактировать первые 10 строчек программы)

### Linux
* перейдите в папку с программой `cd el`
* подключите виртуальное окружение `source el/bin/activate`
* запустите программу `python3 el.py`
