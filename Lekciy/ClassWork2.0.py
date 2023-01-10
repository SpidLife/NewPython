# 1. Напишите программу, которая принимает на вход число N и 
# выдаёт последовательность из N членов.
#  1, -3, 9, -27, 81


number = int(input('Введите размер списка '))
list = []
sum = 0
for i in range(number):
    list_number = int(input(f'Введите число {i+1} '))
    list.append(list_number)
    if i % 2 != 0:
        sum += list[i]


print(list)
print(f'Сумма нечетных чисел равна {sum}')