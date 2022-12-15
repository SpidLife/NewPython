# 5. Напишите программу, которая принимает на вход число и проверяет,
#    кратно ли оно 5 и 10 или 15, но не 30

user_num = int(input())

if (user_num % 5 == 0 and user_num % 10 == 0 or user_num % 15 == 0) and user_num % 30 != 0:
    print('Yes')
else:
    print("No")