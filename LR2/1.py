""" 
Лабораторная 2. Задание 1
1. Напишите функцию greet, которая принимает имя пользователя в качестве аргумента и выводит приветствие с этим именем.
2. Создайте функцию square, которая возвращает квадрат переданного ей числа.
3. Реализуйте функцию max_of_two, которая принимает два числа в качестве аргументов и возвращает большее из них.
"""
def greet(name):
    print("Привет,", name)

def square(number):
    return number ** 2

def max_of_two(x,y):
    return(max(x,y))

#1
greet(input("Введите свое имя: ") )

#2
data = input("Введите число: ")    
print("Квадрат числа", square(int(data)))

#3
data1 = input("Введите первое число: ")    
data2 = input("Введите второе число: ")    

print("Большее число: ", max_of_two(int(data1),int(data2)))


