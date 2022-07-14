# 1 - Напишите программу, которая принимает 
# на вход вещественное число и показывает сумму его цифр.
# *Пример:*

# - 6782 -> 23
# - 0,56 -> 11 

#while True:
#    num = input('Введите число:')
#    if num.isdigit():
#        break
#    else:
#       print('не число')
# print(num)
num = (input('Введите число:'))
x = num.split(',')
a = int(x[0])
b = int(x[1])
sum = 0
while (a != 0):
    sum = sum + (a % 10)
    a = a // 10
while (b != 0):
    sum = sum + (b % 10)
    b = b // 10
print(sum)    



