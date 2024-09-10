import math


def variant_5_1():
    print("Задание №1:\n\n")

    x = float(input("Введите значение x --> "))
    y = float(input("Введите значение y --> "))
    a = float(input("Введите значение a --> "))
    k = float(input("Введите значение k --> "))

    print('\n')


    result_temp = math.cos(math.pow(x, 2) + math.degrees(44))
    result_temp += ( a * math.pow(math.sin(k * y), 2))
    result_temp = math.sqrt(math.fabs(result_temp))
    result_temp = result_temp - 0.6 * math.pow(y, 3) + ( math.log2(8) / 4 * a )

    print("Результат: ", result_temp, '\n')


def variant_5_2():
    print("Задание №2:\n\n")

    x = float(input("Введите значение x --> "))
    y = float(input("Введите значение y --> "))

    print('\n')

    numerator = math.fabs(4*y - 0.5)

    result_temp = math.exp(numerator)
    b = x + 1
    result_temp = math.pow(x, 3) * math.pow(math.tan(math.pow(b, 2)), 2)
    

    print("Результат: ", result_temp, '\n')


def variant_6_1():
    print("Задание №1:\n\n")

    x = float(input("Введите значение x --> "))
    b = math.sin(math.degrees(20))
    a = float(input("Введите значение a --> "))
    k = float(input("Введите значение k --> "))

    print('\n')


    result_temp = math.pow(x, 3) * math.pow(math.tan(math.pow(x + b, 2)), 2)
    result_temp += (0.25 * a) / (k * math.sqrt(math.fabs(x - b)))

    
    print("Результат: ", result_temp, '\n')


def variant_6_2():
    print("Задание №2:\n\n")

    x = float(input("Введите значение x --> "))
    a = float(input("Введите значение a --> "))
    b = float(input("Введите значение B --> "))

    print('\n')


    result_temp = ( b * math.pow(x, 2) - a ) / ( math.exp(a*x) - 1 )
    result_temp += 0.1 + math.log2(4) 

    
    print("Результат: ", result_temp, '\n')


print("Вариант 5:\n")
variant_5_1()
variant_5_2()

print('\n')

print("Вариант 6:\n")
variant_6_1()
variant_6_2()



