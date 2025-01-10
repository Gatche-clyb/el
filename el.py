# Строчка ниже означает, что мы импортируем библиотеку для генирации случайных чисел
from father import *
import random
from colorama import Fore, Back, init  # ,библиотека для цветного вывода
import pandas as pd # мы импортируем библиотеку для оброботки данных
import os # модуль для проверки существования файлов

pd.options.display.max_columns = None  # выводить все столбцы таблицы
init() # включаем возможность цветного вывода на экран
#Ввод с ограничением времени

# загрузка предыдущих ответов
CSV_FILE = 'otveti.csv' # позволяет быстро сменить имя файла с ответами
user_settings_file = 'user_settings.csv'
DEFAULT_USER_ID = 346547893

if not os.path.exists(CSV_FILE):# если нет файла с ответами то выполни блок ниже
    inputs_df_src = pd.DataFrame(data={'operation':'mul_1','suboperation':'mul_1_m', 'session': 1, 'user_id':DEFAULT_USER_ID,
        'var1': 1,'var2':1,'ansver_time': 5  ,'ansver_time_limit':15,'input':1,'status':'ok',
        'date_time':'2025-01-02 11:17:10.9'}, index=[0])
    print('сгенерирован файл с ответами')
else:# в противном случае файл существует перейди на другой блок
    inputs_df_src = pd.read_csv(CSV_FILE)
    print('загружен файл с ответами')
inputs_df_src.date_time = pd.to_datetime(inputs_df_src.date_time)

inputs_df = inputs_df_src.copy()

def save_inputi():
    global inputs_df, inputs_df_src
    izmeneniya = inputs_df[(~inputs_df.isin(inputs_df_src))]
    if len(izmeneniya) != 0:
        inputs_df.to_csv(CSV_FILE, index=False)
        print('файл с ответами записан на диск')

def mini_kubik(*, user_id=DEFAULT_USER_ID,
        time_proverka_limit=[pd.to_datetime('2024-01-01'),pd.to_datetime('2026-01-01')], # интересующий нас диопозон времени
        operation=  'mul_1_m', # микро операции (* : + -)
        var_1_limit=[1,1], #диопозон 1 переменной (в данном случае от 1 до 1)
        var_2_limit=[1,1],
        shtraf_za_ne_ispolzovanie =90,
        shtraf_za_timeout= 90, 
        shtraf_za_oshibki=150
        ):
    global inputs_df
    vibrannie_vvodi = inputs_df[
       (inputs_df.user_id == user_id)  # берём таблицу inputs_df. в этой таблице выбераем стодбец с названием user_id.
           # Далее ищем только строки, в которых в выбранном столбце значение равно user_id (передается в параметрах функции) 
       & (inputs_df.var1 >= var_1_limit[0])  # inputs_df.var1 сравнивается с var_1_limit[0]
       & (inputs_df.var1 <= var_1_limit[1])  # inputs_df.var1 сравнивается с var_1_limit[1]
       & (inputs_df.var2 >= var_2_limit[0])  # inputs_df.var2 сравнивается с var_2_limit[0]
       & (inputs_df.var2 <= var_2_limit[1])  # inputs_df.var2 сравнивается с var_2_limit[1]
       & (inputs_df.date_time >= time_proverka_limit[0])  # inputs_df.date_time сравнивается с time_proverka_limit[0]
       & (inputs_df.date_time <= time_proverka_limit[1])   # inputs_df.date_time сравнивается с time_proverka_limit[1]
       & (inputs_df.suboperation == operation)
       ].copy()       
    #print('vibrannie_vvodi')
    #print(vibrannie_vvodi)
    df_gb = pd.DataFrame(columns =['var_1','var_2','suboperations','time_mean'])
    for i in range (var_1_limit[0],var_1_limit[1] + 1):
        for j in range (var_2_limit[0],var_2_limit[1]  + 1):
           srednee_time = shtraf_za_ne_ispolzovanie
           if len (vibrannie_vvodi) > 0:
                #print('fhgf')
                srednee_time=inputs_df.ansver_time.mean()
           df_gb.loc[len (df_gb)] = [i, j, operation, srednee_time]
    return df_gb

def kubik(*, user_id=DEFAULT_USER_ID):
    # созддим мини кубик для умножения
    mul = mini_kubik(user_id = user_id, operation = 'mul_1_m',var_1_limit = [1,2],var_2_limit = [1,2])
    # созддим мини кубик для деления
    div = mini_kubik(user_id = user_id, operation = 'mul_1_d',var_1_limit = [1,2],var_2_limit = [1,2])
     # созддим мини кубик в котором есть и умножение и деление
    rezult = df_weeks_concat = pd.concat([mul,div]).reset_index()
    # дабовляем таблицу вероятности
    rezult ["cumsum"] = rezult ["time_mean"].cumsum()
    return rezult
    
def input_keyboard():
    res_input=namedtuple('res_input', ['input', 'time_exceeded', 'time_sec'])
    result = res_input(input(), 7, 3)
    return result

def generaceya_primerov(kolichestvo_primerov, *, user_id=DEFAULT_USER_ID, ansver_time_limit=15):
    global inputs_df
    #{'operation':'mul_1','suboperation':'mul_1_m', 'session': 1, 'user_id':DEFAULT_USER_ID,
    #    'var1': 1,'var2':1,'ansver_time': 5  ,'ansver_time_limit':15,'input':1,'status':'ok',
    #    'date_time':'2025-01-02 11:17:10.9'}
    kub = kubik()
    print('kub')
    print(kub)
    max_sum = kub['cumsum'].max()
    num_session = inputs_df.session.max()+1
    for k in range(1,kolichestvo_primerov+1):
        temp = random.uniform(0,max_sum)
        print(f"{max_sum=} {temp=:.1f}")
        primer = kub[kub['cumsum'] >= temp].sort_values('cumsum').head(1).iloc[0]
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
            c = input_keyboard().input
            # Оставить целое число
            c = int(c)
            # 2 Строчки ниже означает, если suma равна переменной с:напечатать ("Правильно")
            if proizvedenie==c:
                print (Fore.GREEN + "Правильно" + Fore.WHITE)
                status='ok'
            # 2 Строчки ниже означает, если suma неравна переменной с:напечатать ("Неправильно")
            else:
                print (Fore.RED + "Неправильно. Будет ", proizvedenie, Fore.WHITE)
                status='error'
        if primer['suboperations'] == 'mul_1_d':
            operation = 'mul_1'
            a = primer['var_1']
            b = primer['var_2']
            proizvedenie = a * b
            chastnoe = b
             # Строчка ниже означает, печатать {a}/{b}=
            print(f"{proizvedenie}/{a}=", end="")
            # Строчка ниже означает,запись в переменную с ввода с клавиотуры
            ##c = input_with_timeout(5, print_timeout=True, default = None).get().input
            ##c=input()
            c = input_keyboard().input
            # Оставить целое число
            c = int(c)
            # 2 Строчки ниже означает, если suma равна переменной с:напечатать ("Правильно")
            if chastnoe==c:
                print (Fore.GREEN + "Правильно" + Fore.WHITE)
                status = 'ok'
            # 2 Строчки ниже означает, если suma неравна переменной с:напечатать ("Неправильно")
            else:
                print (Fore.RED + "Неправильно. Будет ", proizvedenie, Fore.WHITE)
                status='error'
        inputs_df.loc[len(inputs_df)] = {'operation':operation,'suboperation':primer['suboperations'], 'session': num_session,
            'user_id':user_id,  'var1': primer['var_1'],'var2':primer['var_2'],
            'ansver_time': 5  ,'ansver_time_limit':ansver_time_limit, 'input':c, 'status':status,
        'date_time':date_time_current}
    print(inputs_df)



input_with_timeout.step_msc = 100
#inp = input_with_timeout(None, print_timeout=True, default = 'e').get().input
#конец ввода с ограничением времени 


#? # Строчка ниже означает, колч-во правильных ответов
da=0
#? # Строчка ниже означает, колч-во неправильных ответов

net=0
# создаём функцию с названием diablo_sum
def diablo_sum():
    '''
    эта функция делает 2 случайных числа умножает одно на другое и сравнивает введёное с клавиотуры с
    правильным считает колич-во правильных и неправильных и записывает их в переменные da и net
    '''
    global da, net
# В переменную a положим случайное число от 13 до 13, т.е. 13
    a=random.randint (13,13)
# В переменную b положим случайное число от -13 до 13, 
    b=random.randint (-13,13)
# В переменную suma записываем произведение a и b
    suma=a*b
    
    # Строчка ниже означает, печатать {a}*{b}=
    print(f"{a}*{b}=", end="")
    # Строчка ниже означает,запись в переменную с ввода с клавиотуры
    ##c = input_with_timeout(5, print_timeout=True, default = None).get().input
    ##c=input()
    c=input_keyboard().input
    # Оставить целое число
    c=int(c)
     # 2 Строчки ниже означает, если suma равна переменной с:напечатать ("Правильно")
    if suma==c:
        print (Fore.GREEN + "Правильно" + Fore.WHITE)
        da=da+1
        # 2 Строчки ниже означает, если suma неравна переменной с:напечатать ("Неправильно")
    else:
        print (Fore.RED + "Неправильно. Будет ", suma, Fore.WHITE)
        net=net+1
        

# for d in range (1,5): # запустить цикл 
	# # вызов функции diablo_sum которую я определила выше
	# diablo_sum()
	 # # Строчка ниже означает,напечатать сколько Правильных а сколько Неправильных
#print(f"Правильных {da} Неправильных {net}")
#print('inputs_df')
#print(inputs_df)

#print('minikubikl')
#kub=kubik()
#print('generaceya_primerov')
generaceya_primerov(3)
save_inputi()
