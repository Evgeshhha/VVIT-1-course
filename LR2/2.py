""" 
Лабораторная 2. Задание 2
Напишите функцию describe_person, принимающую имя и возраст человека,
и печатающую эту информацию в читаемом виде. 
Сделайте возраст опциональным аргументом со значением по умолчанию 30.
"""
def describe_person(name, age=30):
    print(f'Ваше имя {name}, возраст {age}')

name = input("Введите свое имя: ")
age = input("Введите возраст: ")    
while not age.isdigit():
    print('Неправильные данные')
    age = input("Введите возраст: ")
describe_person(name, age)

