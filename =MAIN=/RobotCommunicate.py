import requests
import time
import os

class NetControl:
    ip = "192.168.4.1"
    def __init__(self, ip="192.168.4.1"):
        self.ip = ip

    #def DefineIP(self, ip):
    #    self.ip = ip


    def MoveForward(self):
        requests.get(f"http://{self.ip}/f")
        print(f"Вперёд")

    def MoveBack(self):
        requests.get(f"http://{self.ip}/b")
        print(f"Назад")

    def MoveRight(self):
        requests.get(f"http://{self.ip}/r")
        print(f"Вправо")

    def MoveLeft(self):
        requests.get(f"http://{self.ip}/l")
        print(f"Влево")

    def MoveStop(self):
        requests.get(f"http://{self.ip}/s")
        print(f"Стоп")

    def Command(self):
        requests.get(f"http://{self.ip}/s")
        print(f"Стоп")

def Timer(timerTime, deltaTime):
        while(timerTime>0):
            timerTime -= deltaTime
            print(".")
            time.sleep(deltaTime)

# def standartTest(nc):
#     while True:
#         requests.get(nc.MoveForward())
#         print(f"http://{ip}/f")
#         Timer(2, 0.5)

#         response = requests.get(f"http://{ip}/b")
#         print(f"http://{ip}/b")
#         Timer(2, 0.5)

#         response = requests.get(f"http://{ip}/r")
#         print(f"http://{ip}/r")
#         Timer(2, 0.5)

#         response = requests.get(f"http://{ip}/l")
#         print(f"http://{ip}/l")
#         Timer(2, 0.5)

#         response = requests.get(f"http://{ip}/s")
#         print(f"http://{ip}/s")
#         Timer(2, 0.5)

def manualControl(nc):
    while True:
        direction = input()

        if(direction == "в"):
            nc.MoveForward()
        elif(direction == "н"):
            nc.MoveBack()
        elif(direction == "п"):
            nc.MoveRight()
        elif(direction == "л"):
            nc.MoveLeft()
        elif(direction == "с"):
            nc.MoveStop()
        else:
            continue


def main():
    os.system("cls")
    print("=== Д/У - En24 - byRitme ===")

    if(input("Выберете настройки [Enter - Точка Доступа (стд. IP), 1 - WiFi (каст. IP)]: ") == "1"):
        print()
        print("Для запуска введите 2 последние цифры IP")
        ipBytes = [input("Первое число: "), input("Второе число: ")]
        ip = f"192.168.{ipBytes[0]}.{ipBytes[1]}"
        nc = NetControl(ip)
    else:
        nc = NetControl()

    mode = int(input("Выбор режима [0 - Тест моторов, 1 - Ручное Д/У, -1 - Выход]: ")) 
    if(mode == 0):
        #standartTest(nc)
        pass
    elif(mode == 1):
        manualControl(nc)
    elif(mode == -1):
        exit()
    else:
        return


while(__name__ == "__main__"):
    main()