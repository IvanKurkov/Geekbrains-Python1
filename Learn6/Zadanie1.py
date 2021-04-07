# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,
# зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего
# (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке

class TrafficLight:
    __color = "Red"

    def running(self):
        from time import sleep
        print(f"Цвет светофора: {TrafficLight.__color}")
        sleep(7)
        TrafficLight.__color = "Yellow"
        print(f"Цвет светофора: {TrafficLight.__color}")
        sleep(3)
        TrafficLight.__color = "Green"
        print(f"Цвет светофора: {TrafficLight.__color}")
        sleep(5)
        TrafficLight.__color = "Red"


a = TrafficLight()
a.running()
