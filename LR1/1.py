""" 
Лабораторная 1. Задание 1
Напишите программу, которая запрашивает у пользователя ввод числа и выводит на экран все числа от 1 до введенного числа включительно.
"""

data = input("Введите число от 1: ")    
while not data.isdigit() or (data.isdigit() and int(data) < 1):
    print('Неправильные данные')
    data = input("Введите число от 1: ")

for i in range (1, int(data) + 1):
    print(i)