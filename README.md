# Программа-тренажер для помощи в запоминании таблицы умножения

Основная ссылка: [https://github.com/Gatche-clyb/el](https://github.com/Gatche-clyb/el)  
Короткая ссылка (будет перенаправление на основную ссылку): [https://gifara.ru/7/0](https://gifara.ru/7/0)  
  
Программа генерирует примеры на умножение/деление, и проверяет правильность решения. Диапазоны множителей, количество примеров, время ответов и штрафы настраиваются.

## Установка

### Windows
* Вариант 1: автоматически
    * Скачать установщик [install_el.bat](https://github.com/Gatche-clyb/el/blob/main/.tools/install_el.bat). Клик на 3 точках, выбрать "Download"
    * кликнуть на скаченом файле. Всплывет окошко "Система Windows защитила ваш компьютер". Нажимаем на ссылку "подробнее", затем на появившуюся кнопку "выполнить в любом случае".
    * установщик запустится, через какое-то время всплывет еще одно окошко с вопросом "Разрешить этому приложению вносить изменения на вашем устройстве". Нажимаем "да".
    * В автоматическом режиме установятся зависимые программы git и python. Затем в автоматическом режиме скачается последняя версия программы и необходимые библиотеки для python.
    * По завершению установщика можно пользоваться программой. Дополнительно создается ярлык на рабочий стол для запуска программы.
* Вариант 2: вручную
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
    * Скачайте [основную программу](https://github.com/Gatche-clyb/el/blob/main/el.py)
    * `cp ..\Downloads\el.py .\` скопировать программу из директории загрузок в папку с программой
<!--- Многострочный комменарий -->
### Linux (Ubuntu)
* Вариант 1: автоматический
    * `wget https://gifara.ru/7/5211-2213 | bash` скачивание последней версии скрипта автоустановки и его запуск. В процессе выполнения потребуются права sudo.
* Вариант2: вручную
    * `sudo apt upgrade && sudo apt upgrade -y` обновить актуальность программ
    * установите python: `sudo apt install -y python3 python3.12-venv python3-pip`
    * установите git: `sudo apt install -y git`
    * скачайте последнюю версию программы: `git clone https://github.com/Gatche-clyb/el.git`
    * перейдите в папку с программой `cd el`
    * создайте виртуальное окружение `python3 -m venv el`
    * `. el/bin/activate` войти в вертуальное окружение
        * Запустите процесс скачивания и установки дополнительных модулей:
            * `pip install colorama`
            * `pip install pandas`
            * `pip install matplotlib`
            * `pip install seaborn`

## Использование

### Windows
* в "пользовательском" режиме:
    * дважды кликните на ярлык программы на рабочем столе. Первый запуск может сопровождаться задержкой на несколько секунд.
* в ручном режиме:
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

## Общие сведения

После сеанса примеров выводится сводная таблица, в которой наглядно отображается среднее время ответа на примеры (красным подсвечены примеры, вызывающие сложность).  
Время в таблице усредняется по всем типам операций (умножение/деление), поэтому для того, чтобы выйти из красной зоны, требуется чтобы пример появился и на умножение, и на деление. Как это работает: допустим штраф за новый пример выставлен в 90 секунд, выпало 2 примера на умножение (время ответов 9.5 сек и 5.5 сек) и ни одного примера на деление. Итог: (90+9.5+5.5)/3 = 35 секунд.

## Обратная связь

До лета 2025 года по всем интересующим вопросам можно получить консультацию по телегаму: https://t.me/Aleksandr_Firsov
