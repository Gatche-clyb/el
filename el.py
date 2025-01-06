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
if not os.path.exists(CSV_FILE):# если нет файла с ответами то выполни блок ниже
    inputs_df_src = pd.DataFrame(data={'operation':'mul_1','suboperation':'mul_1_m', 'session': 1, 'user_id':346547893,
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

def mini_kubik(*, user_id=346547893, time_proverka_limit=['2024-01-01','2026-01-01'], operation,var_1_limit=[1,1], var_2_limit=[1,1]):
    global inputs_df
    vibrannie_vvodi = inputs_df[
       (inputs_df.user_id == user_id) &
       (inputs_df.var1 >= var_1_limit[0]) &
       (inputs_df.var1 <= var_1_limit[1]) &
       (inputs_df.var2 >= var_2_limit[0]) &
       (inputs_df.var2 <= var_2_limit[1]) &
       (inputs_df.date_time >= time_proverka_limit[0]) &
       (inputs_df.date_time <= time_proverka_limit[1])
       ].copy()
    print(vibrannie_vvodi)


def input_keyboard():
    res_input=namedtuple('res_input', ['input', 'time_exceeded', 'time_sec'])
    result = res_input(input(), 7, 3)
    return result

def generaceya_primerov(operation, mnogetel_1, mnogetel_2):
    if operation=='mul_1':
        pass




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
        # 2 Строчки ниже означает, если sumaнеравна переменной с:напечатать ("Неправильно")
    else:
        print (Fore.RED + "Неправильно. Будет ", suma, Fore.WHITE)
        net=net+1
        

for d in range (1,3): # запустить цикл 16-1 раз
	# вызов функции diablo_sum которую я определила выше
	diablo_sum()
	 # Строчка ниже означает,напечатать сколько Правильных а сколько Неправильных
print(f"Правильных {da} Неправильных {net}")
print(inputs_df_src)
save_inputi()
