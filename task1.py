# 1 - Напишите программу, которая принимает 
# на вход вещественное число и показывает сумму его цифр.
# *Пример:*

# - 6782 -> 23
# - 0,56 -> 11 


num = str(input('Введите вещественное число:')) 
def is_number(num): #проверка Try-Except(если строка содержит отрицательное число и число с плавающей точкой )
    try:
        float(num)
        return True
    except ValueError:
        return False # если строка кроме цифр,знака минуса и точки содержит другие символы 
x = num.split(',')
res_x = str(num).replace('-', '') # убираем минус 
print(res_x)
part1 = int(x[0])
part2 = int(x[1])
sum = 0
while (part1 != 0):
    sum = sum + (part1 % 10)
    part1 = part1 // 10
while (part2 != 0):
    sum = sum + (part2 % 10)
    part2 = part2 // 10
print(f'Резултат: {sum}')    



