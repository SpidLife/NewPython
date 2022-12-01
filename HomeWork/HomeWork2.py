# Задание 1
# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# *Пример:*

# - 6782 -> 23
# - 0.56 -> 11

# sum = 0
# input_num = input('Введите число: ')

# for a in input_num:
#     if a.isdigit():
#         sum += int(a)

# print(sum)

# Задание 2
# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# *Пример:*

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
# Запрещено использовать функцию factorial из библиотеки math

# N = int(input('Введите число '))

# f = 1
# for i in range(N):
#     i = i + 1
#     f = i * f
    
#     print(f, end=" ")

# Задание 3
# Задайте список из n чисел последовательности (1 + 1 / n)**n и выведите на экран их сумму.

# *Пример:*

# - Для n = 6: [2.0, 2.25, 2.37, 2.44, 2.488, 2.52]     ->       14.072    (Округлять не обязательно)

# n = int(input('Введите число: ')) 

# def sequence(n):

#     return[round((1 + 1 / x)**x, 2) for x in range (1, n + 1)]   
        
# print(sequence(n))
# print(round(sum(sequence(n))))

# Задание 4
# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции вводятся с клавиатуры.

# from random import Random, randint


# N = int(input('Введите число: '))
# numbers = []
# for i in range(N):
#     numbers.append(randint(-N,N+1))
    
# print(numbers)
# print(numbers[1] * numbers[3])

# f = open('file.txt', 'w')
# while True:
#     s = input('Укажите позицию для вычисления - ')
#     if s == "":
#         break
#     f.write(s+"\n")
# f.close()

# result = 1
# f = open('file.txt', 'r')
# for line in f:
#     if line == "":
#         break
#     result *= numbers[int(line)]
# f.close()
# print(result)


# Задание 5
# Реализуйте алгоритм перемешивания списка.
# Из библиотеки random использовать можно только randint

# import random
# lst = [random.randint(0,10) for i in range(random.randint(5,20))]
# print(f"исходный список:\n {lst}")
# random.shuffle(lst)
# print(f"список после перемешивания:\n{lst}")