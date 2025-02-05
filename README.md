# Программа-тренажер для помощи в запоминании таблицы умножения

Основная ссылка: [https://github.com/Gatche-clyb/el](https://github.com/Gatche-clyb/el)  
Короткая ссылка (будет перенаправление на основную ссылку): [https://gifara.ru/7/0](https://gifara.ru/7/0)  
  
Программа генерирует примеры на умножение/деление, и проверяет правильность решения. Диапазоны множителей, количество примеров, время ответов и штрафы настраиваются.

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
<!--- * Скачайте [основную программу](https://github.com/Gatche-clyb/el/blob/main/el.py) и переместите ее в созданную папку ($HOME/el/)-->

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

## Общие сведения

После сеанса примеров выводится сводная таблица, в которой наглядно отображается среднее время ответа на примеры (красным подсвечены примеры, вызывающие сложность).  
Время в таблице усредняется по всем типам операций (умножение/деление), поэтому для того, чтобы выйти из красной зоны, требуется чтобы пример появился и на умножение, и на деление. Как это работает: допустим штраф за новый пример выставлен в 90 секунд, выпало 2 примера на умножение (время ответов 9.5 сек и 5.5 сек) и ни одного примера на деление. Итог: (90+9.5+5.5)/3 = 35 секунд.

## Обратная связь

До лета 2025 года по всем интересующим вопросам можно получить консультацию по телегаму: https://t.me/Aleksandr_Firsov
