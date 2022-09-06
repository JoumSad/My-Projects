#WheaZiyy BOT V1.0


# module "TIME"
import time
# module "PYTHON-WEATHER"
import python_weather
import asyncio
import os
# module "COLORAMA"
from colorama import Fore, Back, Style
from colorama import init
init()

async def getweather():
    async with python_weather.Client(format=python_weather.IMPERIAL) as client:
        print(Fore.LIGHTBLACK_EX)
        print("WheaZiyy by Omar Ilyasov")
        print(Fore.RED)
        print("Предупреждение! "
              "Пиши имя своего города на АНГЛИЙСКОМ ЯЗЫКЕ !(Пример: Москва- Moscow)")

        print(Fore.LIGHTGREEN_EX)
        time.sleep(1)

        print(

        )
        weather = await client.get(str(input('В каком городе ты живешь? :')))
        ce = (weather.current.temperature - 32) * 5 / 9
        if ce <= 10:
            print("Подождите. Идет подсчет...")
            time.sleep(1)
            print("Подождите. Идет подсчет..")
            time.sleep(1)
            print("Подождите. Идет подсчет...")
            time.sleep(1)
            print(

            )
            print("Оденься потеплее,так как на улице "+str(round(ce))+"° градусов (Это довольно холодно)")
            inport()
        elif ce <= 0 :
            print("Подождите. Идет подсчет...")
            time.sleep(1)
            print("Подождите. Идет подсчет..")
            time.sleep(1)
            print("Подождите. Идет подсчет...")
            time.sleep(1)
            print(Fore.RED)
            print("Не выходи на улицу,так как на улице " + str(round(ce)) + "° градусов (Это СЛИШКОМ холодная погода")
            inport()
        elif ce > 10:
            print("Подождите. Идет подсчет...")
            time.sleep(1)
            print("Подождите. Идет подсчет..")
            time.sleep(1)
            print("Подождите. Идет подсчет...")
            time.sleep(1)
            print(

            )
            print("Оденься как хочешь,так как на улице " + str(round(ce)) + "° градусов(Это умеренная температура)")
            inport()
        elif ce >= 20:
            print("Подождите. Идет подсчет...")
            time.sleep(1)
            print("Подождите. Идет подсчет..")
            time.sleep(1)
            print("Подождите. Идет подсчет...")
            time.sleep(1)
            print(

            )
            print("Оденься как хочешь,так как на улице "+ str(round(ce))+"° градусов (Это жаркая погода)")
            inport()
        else:
            print("Подождите. Идет подсчет...")
            time.sleep(1)
            print("Подождите. Идет подсчет..")
            time.sleep(1)
            print("Подождите. Идет подсчет...")
            time.sleep(1)
            print(Fore.RED)
            print("Не выходи на улицу,так как на улице "+ str(round(ce))+"° градусов (Это СЛИШКОМ жаркая погода")
            inport()

if __name__ == "__main__":
    # see https://stackoverflow.com/questions/45600579/asyncio-event-loop-is-closed-when-getting-loop
    # for more details
    if os.name == "nt":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    asyncio.run(getweather())
