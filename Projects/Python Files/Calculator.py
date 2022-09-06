import math
from colorama import Fore, Back, Style
from colorama import init

init()

print( Fore.BLACK )
print("Calculator V1 by Omar Ilyasov")
print ( Fore.BLUE )
#переменные
select = input("Выберите действие (- , + , * , /) :")
a = float
b = float
c = 0
select = select
#аргументы переменной select
if select == "-" :
    a = float(input("Введите первое число :"))
    b = float(input("Введите второе число :"))
    c = a - b
    print(

    )
    print( Fore.GREEN )
    print("Ответ: "+str(c))
elif select == "+" :
    a = float(input("Введите первое число :"))
    b = float(input("Введите второе число :"))
    c = a + b
    print(

    )
    print(Fore.GREEN)
    print("Ответ: "+str(c))
elif select == "*" :
    a = float(input("Введите первое число :"))
    b = float(input("Введите второе число :"))
    c = a * b
    print(

    )
    print(Fore.GREEN)
    print("Ответ: "+str(c))
elif select == "/" :
    a = float(input("Введите первое число :"))
    b = float(input("Введите второе число :"))
    c = a / b
    print(

    )
    print(Fore.GREEN)
    print("Ответ: " + str(c))
else:
    print( Fore.RED)
    print("Выбрана неверная операция!")