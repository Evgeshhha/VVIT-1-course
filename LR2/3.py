""" 
Лабораторная 2. Задание 3
Напишите функцию is_prime, которая определяет, 
является ли число простым, и возвращает True или False соответственно.

!!!Если число делится на любое число в диапазоне от 3 до квадратного корня, то оно не является простым.
"""
import math

def is_prime(number):
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(number)) + 1, 2):
        if number % i == 0:
            return False
    return True

print(is_prime(1))  
print(is_prime(2))  
print(is_prime(3))  
print(is_prime(4))  
print(is_prime(29)) 
print(is_prime(100))