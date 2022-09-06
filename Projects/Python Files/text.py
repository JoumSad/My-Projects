import math
import time
from colorama import Fore, Back, Style
from colorama import init

init()

#переменные
print(Fore.LIGHTBLACK_EX)
name = str(print('Привет меня зовут Гери! Я создан для того чтобы помочь именно тебе и порекомендовать как одется в ту или иную температуру))'))
time.sleep(1)
print(

)
print(Fore.LIGHTBLUE_EX)
time.sleep(0)
temp = int(input('Сколько градусов у тебя на улице? :'))
while temp == 0 :
    temp = int(input('Сколько градусов у тебя на улице? :'))
country = str(input('В каком городе ты живешь? :'))
while country == 0 :
    country = str(input('В каком городе ты живешь? :'))
#аргументами + основная часть

print(Fore.LIGHTGREEN_EX)
if temp >= 20:
    print('На улице тепло , оденься как хочешь)')
    input()
elif temp >= 50:
    print('Не выходи на улицу , расстаешь)')
    input()
elif temp < 20:
    print('На улице холодно оденься потеплее')
    input()
elif temp < 0 :
    print('Не выходи на улицу включи печь и сиди дома , на улице очень холодно! Ты точно заболеешь')
    input()
else:
    prinds