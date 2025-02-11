#!/bin/env el/bin/python3
# Настройки программы
time_limit = 15  # количество секунд на ответ
number_of_tasks = 10  # количество примеров
mul_limit = [1, 10]  # пределы множителей
div_limit = [1, 10]  # пределы делимого и частного в этом диапазоне
error_penalty = 150  # штраф за ошибку
timeout_penalty = 90  # штраф за таймаут
not_using_penalty = 90  # если пример до этого не встречался, то такое количество секунд
# конец настроек программы

# Строчка ниже означает, что мы импортируем библиотеку для генирации случайных чисел
#from father import *
import random
from colorama import Fore, Back, init  # ,библиотека для цветного вывода
import pandas as pd # мы импортируем библиотеку для оброботки данных
import os # модуль для проверки существования файлов
import matplotlib.pyplot as plt  # базовый модуль отрисовки графики
import seaborn as sns  # модуль графического представления данных
from datetime import datetime
from collections import namedtuple

pd.options.display.max_columns = None  # выводить все столбцы таблицы
init() # включаем возможность цветного вывода на экран
print('Инструкцию по установке программы можно найти по ссылке: https://gifara.ru/7/0')

#Ввод с ограничением времени

# загрузка предыдущих ответов
CSV_FILE = 'otveti.csv' # позволяет быстро сменить имя файла с ответами
user_settings_file = 'user_settings.csv'#?
DEFAULT_USER_ID = 346547893 # записываем первое попавшееся число

if not os.path.exists(CSV_FILE):# если нет файла с ответами то выполни блок ниже
    inputs_df_src = pd.DataFrame(data={'operation':'mul_1','suboperation':'mul_1_m', 'session': 1, 'user_id':DEFAULT_USER_ID,
        'var1': 1,'var2':1,'ansver_time': 0.5  ,'ansver_time_limit':15,'input':1,'status':'ok',
        'date_time':'2025-01-02 11:17:10.9'}, index=[0])#создаём структуру с ответами
    print('сгенерирован файл с ответами')#печатать сгенерирован файл с ответами 
else:# в противном случае файл существует перейди на другой блок
    inputs_df_src = pd.read_csv(CSV_FILE)
    print('загружен файл с ответами')#печатать загружен файл с ответами
inputs_df_src.date_time = pd.to_datetime(inputs_df_src.date_time) # текстовое представление времени переводим формат "время"

inputs_df = inputs_df_src.copy() # сравнивая копию с оригиналом потом будем находить изменения

def save_inputi():# создаём функцию с названием save_inputi
    global inputs_df, inputs_df_src#?
    izmeneniya = inputs_df[(~inputs_df.isin(inputs_df_src))]#?
    if len(izmeneniya) != 0:#?
        inputs_df.to_csv(CSV_FILE, index=False)#?
        print('файл с ответами записан на диск')#печатать файл с ответами записан на диск

def mini_kubik(*, user_id=DEFAULT_USER_ID, # создаём функцию с названием mini_kubik
        time_proverka_limit=[pd.to_datetime('2024-01-01'),pd.to_datetime('2026-01-01')], # интересующий нас диопозон времени
        operation=  'mul_1_m', # микро операции (* : + -)
        var_1_limit=[1,1], #диопозон 1 переменной (в данном случае от 1 до 1)
        var_2_limit=[1,1], #диопозон 2 переменной (в данном случае от 1 до 1)
        shtraf_za_ne_ispolzovanie =not_using_penalty,#задаём штафы в секундах 
        shtraf_za_timeout= timeout_penalty, 
        shtraf_za_oshibki=error_penalty
        ):
    global inputs_df#делаем inputs_df глобальными
    vibrannie_vvodi = inputs_df[#?
       (inputs_df.user_id == user_id)  # берём таблицу inputs_df. в этой таблице выбераем стодбец с названием user_id.
           # Далее ищем только строки, в которых в выбранном столбце значение равно user_id (передается в параметрах функции) 
       & (inputs_df.var1 >= var_1_limit[0])  # inputs_df.var1 сравнивается с var_1_limit[0]
       & (inputs_df.var1 <= var_1_limit[1])  # inputs_df.var1 сравнивается с var_1_limit[1]
       & (inputs_df.var2 >= var_2_limit[0])  # inputs_df.var2 сравнивается с var_2_limit[0]
       & (inputs_df.var2 <= var_2_limit[1])  # inputs_df.var2 сравнивается с var_2_limit[1]
       & (inputs_df.date_time >= time_proverka_limit[0])  # inputs_df.date_time сравнивается с time_proverka_limit[0]
       & (inputs_df.date_time <= time_proverka_limit[1])   # inputs_df.date_time сравнивается с time_proverka_limit[1]
       & (inputs_df.suboperation == operation)#?
       ].copy()#?
    #print(f"\tМиникубик:\t{operation=}\tvibrannie_vvodi=\n{vibrannie_vvodi}")
    df_gb = pd.DataFrame(columns =['var_1','var_2','suboperations','time_mean'])# создаём структуру игральной кости
    for i in range (var_1_limit[0],var_1_limit[1] + 1):#делаем цикл
        for j in range (var_2_limit[0],var_2_limit[1] + 1):#делаем цикл
           srednee_time = shtraf_za_ne_ispolzovanie#?
           vibrannie_vvodi_point = vibrannie_vvodi[(vibrannie_vvodi.var1 == i) & (vibrannie_vvodi.var2 == j)].copy()
           if len (vibrannie_vvodi_point) > 0:#если len > 0 
                vibrannie_vvodi_point.ansver_time = vibrannie_vvodi_point.apply(lambda row: row.ansver_time if row.status == 'ok'
                    else (timeout_penalty if row.status == 'timeout' else error_penalty), axis=1)
                srednee_time=vibrannie_vvodi_point.ansver_time.mean()#?
           df_gb.loc[len (df_gb)] = [i, j, operation, srednee_time]#?
    #print(f"\tМиникубик:\t{operation=}\tвозврат:\n{df_gb}")
    return df_gb  # возвращаемся к df_gb

def kubik(*, user_id=DEFAULT_USER_ID):#делаем функцию с названием kubik
    # созддим мини кубик для умножения
    mul = mini_kubik(user_id = user_id, operation = 'mul_1_m', var_1_limit = mul_limit, var_2_limit = mul_limit)
    # созддим мини кубик для деления
    div = mini_kubik(user_id = user_id, operation = 'mul_1_d',var_1_limit = div_limit, var_2_limit = div_limit)
     # созддим мини кубик в котором есть и умножение и деление
    rezult = df_weeks_concat = pd.concat([mul,div]).reset_index()
    # дабовляем таблицу вероятности
    rezult ["cumsum"] = rezult ["time_mean"].cumsum()
    return rezult #вернуться к результату
    
def input_keyboard(max_time=15):#создаём функцию
    res_input=namedtuple('res_input', ['input', 'time_exceeded', 'time_sec'])#делаем структуру с тремя переменными
    start = datetime.now().timestamp()#смотрим время перед началом ввода
    vvod=input()
    try:
        vvod = int(vvod)
    except:
        print('это не число. Заменяем на 0')
        vvod = 0
    finish = datetime.now().timestamp()#посмотрели время после конца ввода
    vremya=finish-start#сщитаем время ввода
    result = res_input(vvod, max_time, vremya)
    return result#вернуться к результату

def generaceya_primerov(kolichestvo_primerov, *, user_id=DEFAULT_USER_ID, ansver_time_limit=15):#создаём функцию
    global inputs_df
    #{'operation':'mul_1','suboperation':'mul_1_m', 'session': 1, 'user_id':DEFAULT_USER_ID,
    #    'var1': 1,'var2':1,'ansver_time': 5  ,'ansver_time_limit':15,'input':1,'status':'ok',
    #    'date_time':'2025-01-02 11:17:10.9'}
    kub = kubik()#делаем переменную kub
    #print('kub')#печатать куб
    #print(kub)#печатать куб
    max_sum = kub['cumsum'].max()
    num_session = inputs_df.session.max()+1
    da=0
    net=0
    Timaut=0
    for k in range(1,kolichestvo_primerov+1):
        temp = random.uniform(0,max_sum)
        #print(f"{max_sum=} {temp=:.1f}")
        primer = kub[kub['cumsum'] >= temp].sort_values('cumsum').head(1).iloc[0]#пример=
        # kub[kub['cumsum'] >= temp].sort_values('cumsum').head(1).iloc[0]
        status='in_process'
        date_time_current=datetime.now()#.timestamp()
        #print(primer)
        if primer['suboperations'] == 'mul_1_m':
            operation = 'mul_1'
            a = primer['var_1']
            b = primer['var_2']
            proizvedenie = a*b
            # Строчка ниже означает, печатать {a}*{b}=
            print(f"{a}*{b}=", end="")
            # Строчка ниже означает,запись в переменную с ввода с клавиотуры
            ##c = input_with_timeout(5, print_timeout=True, default = None).get().input
            ##c=input()
            vvod = input_keyboard(ansver_time_limit)#делаем структуру с переменными input, time_exceeded, time_sec
            # Оставить целое число
            c = int(vvod.input)
            # 2 Строчки ниже означает, если suma равна переменной с:напечатать ("Правильно")
            if proizvedenie==c:
                if  vvod.time_exceeded>=vvod.time_sec:
                    print (Fore.GREEN + "Правильно" + Fore.WHITE)
                    da=da+1
                    status='ok'
                else:
                    print (Fore.BLUE + "Неуспел. Будет ", proizvedenie, Fore.WHITE)
                    Timaut=Timaut+1
                    status='timaut'
            # 2 Строчки ниже означает, если suma неравна переменной с:напечатать ("Неправильно")
            else:
                print (Fore.RED + "Неправильно. Будет ", proizvedenie, Fore.WHITE)
                net=net+1
                status='error'
        if primer['suboperations'] == 'mul_1_d':
            operation = 'mul_1'
            a = primer['var_1']
            b = primer['var_2']
            proizvedenie = a*b
            delitel = b
            chastnoe = a
             # Строчка ниже означает, печатать {a}/{b}=
            print(f"{proizvedenie}:{delitel}=", end="")
            # Строчка ниже означает,запись в переменную с ввода с клавиотуры
            ##c = input_with_timeout(5, print_timeout=True, default = None).get().input
            ##c=input()
            vvod = input_keyboard(ansver_time_limit)
            # Оставить целое число
            c = int(vvod.input)
            # 2 Строчки ниже означает, если suma равна переменной с:напечатать ("Правильно")
            if chastnoe == c:
                if  vvod.time_exceeded>=vvod.time_sec:
                    print (Fore.GREEN + "Правильно" + Fore.WHITE)
                    da=da+1
                    status = 'ok'
            # 2 Строчки ниже означает, если suma неравна переменной с:напечатать ("Неправильно")
                else:
                    print (Fore.BLUE + "Неуспел. Будет ", chastnoe, Fore.WHITE)
                    Timaut=Timaut+1
            else:
                print (Fore.RED + "Неправильно. Будет ", chastnoe, Fore.WHITE)
                net=net+1
                
                status='error'
        inputs_df.loc[len(inputs_df)] = {'operation':operation,'suboperation':primer['suboperations'], 'session': num_session,
            'user_id':user_id,  'var1': primer['var_1'],'var2':primer['var_2'],
            'ansver_time': vvod.time_sec  ,'ansver_time_limit':ansver_time_limit, 'input':c, 'status':status,
        'date_time':date_time_current}
    #print(inputs_df)
    print(f" {Fore.WHITE} {da+net+Timaut} {Fore.GREEN} {da} {Fore.RED} {net} {Fore.BLUE} {Timaut}")#печатать скоко правильных а скоко неправильных

def preparate_to_heatmap(*, df, var1, var2, value, agg='mean'):
    #print(f"\tpreparate_to_heatmap\t{var1=}\t{var2=}\t{value=}\tdf=\n{df}")
    var1u = df[var1].unique().copy()
    var2u = df[var2].unique().copy()
    var1u.sort()
    var2u.sort()
    final_df = pd.DataFrame(columns=var2u)
    for v1 in var1u:
        series = pd.Series()
        for v2 in var2u:
            series[v2] = df[(df[var1] == v1) & (df[var2] == v2)][value].agg(agg)
        final_df.loc[v1]=series
    #print(f"\tpreparate_to_heatmap\tfinal_df=\n{final_df}")
    return final_df

def vozvrat_v_tablicu():
    #N_posledniy_sesii = inputs_df.session.max()
    #posledniya_sesiya = inputs_df[inputs_df.session == N_posledniy_sesii]
    kub = kubik().drop(['index','cumsum', 'suboperations'], axis=1)
    #print(f"kub=\n{kub}")
    #kub_m=kub[kub.suboperations == 'mul_1_m'].drop(, axis=1)
    #kub_d=kub[kub.suboperations == 'mul_1_d'].drop('suboperations', axis=1)
    df = preparate_to_heatmap(df=kub, var1='var_1', var2='var_2', value='time_mean')
    #print('df=')
    #print(df)
    ax = sns.heatmap(df, annot=True, fmt ='.1f', cmap="coolwarm", vmin = df.min().min(), vmax = time_limit)
    ax.set_title('Среднее время на решение примера (сек)')
    ax.set_xlabel('2 множитель', fontsize=10)
    ax.set_ylabel('1 множитель', fontsize=10)
    plt.show()
    #print('таблица ответов')
    #print (posledniya_sesiya)


#print('minikubikl')
#kub=kubik()
#print('generaceya_primerov')
generaceya_primerov(number_of_tasks, ansver_time_limit=7)
save_inputi()
vozvrat_v_tablicu()
