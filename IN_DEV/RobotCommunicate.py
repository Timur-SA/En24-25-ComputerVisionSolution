import requests
import time
from os import run


print("Для запуска введите 2 последние цифры IP")
ipBytes = [input("Первое число: "), input("Второе число: ")]
ip = f"192.168.{ipBytes[0]}.{ipBytes[1]}"


def Timer(timerTime, deltaTime):
    while(timerTime>0):
        timerTime -= deltaTime
        print(".")
        time.sleep(deltaTime)

def MoveForward():
    response = requests.get(f"http://{ip}/f")
    print(f"Вперёд")

def MoveForward():
    response = requests.get(f"http://{ip}/f")
    print(f"Вперёд")

def MoveForward():

def MoveForward():

def MoveForward():



def standartTest():
    while True:
        response = requests.get(f"http://{ip}/f")
        print(f"http://{ip}/f")
        Timer(2, 0.5)

        response = requests.get(f"http://{ip}/b")
        print(f"http://{ip}/b")
        Timer(2, 0.5)

        response = requests.get(f"http://{ip}/r")
        print(f"http://{ip}/r")
        Timer(2, 0.5)

        response = requests.get(f"http://{ip}/l")
        print(f"http://{ip}/l")
        Timer(2, 0.5)

        response = requests.get(f"http://{ip}/s")
        print(f"http://{ip}/s")
        Timer(2, 0.5)

def manualControl():
    while True:
        direction = input()

        if(direction == "в"):
        
        elif(direction == "н"):
        
        elif(direction == "п"):
        
        elif(direction == "л"):
        
        elif(direction == "с"):
        
        else:
            continue


def main():
    run("cls")
    print("=== Д/У - En24 - byRitme ===")
    mode = int(input("Выбор режима (0 - Тест моторов, 1 - Ручное Д/У, -1 - Выход): "))
    
    if(mode == 0):
        standartTest()
    elif(mode == 1):
        ()
    elif(mode == -1):
        exit()
    else:
        return


while(__name__ == "__main__"):
    main()