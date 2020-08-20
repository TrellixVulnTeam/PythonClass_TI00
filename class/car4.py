class Car:
    """
    Car class
    Author : Park
    Date : 2020.08.13
    Description : Class 작성법 / 생성자 / 클래스 변수
    """

    car_count = 0

    def __init__(self, color, speed):
        self.color = color
        self.speed = speed
        Car.car_count += 1

    def upSpeed(self, value):
        self.speed += value

    def downSpeed(self, value):
        self.speed -= value

    def __del__(self):
        Car.car_count -= 1


# 객체 생성
myCar1 = Car("Red", 30)
myCar2 = Car("Blue", 20)
myCar3 = Car("Black", 50)

myCar1.upSpeed(20)
print("자동차1의 색상은 {} 이며, 현재 속도는 {:3d}km".format(myCar1.color, myCar1.speed))

myCar2.upSpeed(30)
print("자동차2의 색상은 {} 이며, 현재 속도는 {:3d}km".format(myCar2.color, myCar2.speed))


myCar3.upSpeed(40)
print("자동차3의 색상은 {} 이며, 현재 속도는 {:3d}km".format(myCar3.color, myCar3.speed))


print()
print("myCar1 주소 : ", id(myCar1))
print("myCar2 주소 : ", id(myCar2))
print("myCar3 주소 : ", id(myCar3))

print()
print(Car.__doc__)

print()
print('생산된 총 자동차 수 : {}'.format(Car.car_count))
