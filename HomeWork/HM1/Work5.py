# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

print('Введите координату тoчки А:')
x_A = float(input('X: '))
y_A = float(input('Y: '))
print("Введите координату точки B:")
x_B = float(input('X: '))
y_B = float(input('Y: '))
from math import sqrt
print('Дистанция между А и В: ',round(sqrt((x_A - x_B)**2 + (y_A - y_B)**2), 2))