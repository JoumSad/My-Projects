import math
from colorama import Fore, Back, Style
from colorama import init
init()


#переменные
print(Fore.BLUE)
age = input('Введи свой год рождения :')

while len(age) == 0:
    age = input('Введи свой год рождения :')

year = input('Какой сейчас год ? :')
while len(year) == 0:
    year = input('Какой сейчас год ? :')
if year == age :
    print("Год рождения и нынешьний год не могут совпадать!")

al = input('Хочешь я узнаю твой возраст ? :')

while len(al) == 0:
    al = input('Хочешь я узнаю твой возраст ? :')
i = 0
result = 0
#перевод
age = int(age)
year = int(year)
#аргументы переменных
if al == 'да' or 'Да':
    result = year - age

    print(Fore.GREEN)
    print('Тебе '+str(result)+' лет!')
elif al == 'нет' or 'Нет':
    result = 0

    print(Fore.RED)
    print('Ок тогда пока)')
elif al <= i:
    print(Fore.RED)
    print('Выбрана неверная операция!')