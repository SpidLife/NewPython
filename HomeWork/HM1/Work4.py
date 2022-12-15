# 4. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
# *Пример:*

# - 1 -> x > 0, y > 0
# - 8 -> нет такой четверти
import random
user_num = int(input("Введите номер четверти: "))
x = 0
y = 0

if user_num == 1:
    x = random.randint(0, 999)
    y = random.randint(0, 999)
    print(f"x = {x}\ny = {y}")
elif user_num == 2:
    x = random.randint(-999, -1)
    y = random.randint(0, 999)
    print(f"x = {x}\ny = {y}")
elif user_num == 3:
    x = random.randint(-999, -1)
    y = random.randint(-999, -1)
    print(f"x = {x}\ny = {y}")
elif user_num == 4:
    x = random.randint(0, 999)
    y = random.randint(-999, -1)
    print(f"x = {x}\ny = {y}")
else:
    print("Нет такой четверти!")
