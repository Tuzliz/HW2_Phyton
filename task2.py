# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#*Пример:*

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def num_biger_then_zero(text):

    int_num = True
    while int_num:
        n = input(f"{text}")
        if n.isdigit():
            n = int(n)
            if n <= 0:
                print("Введите число > 0")
            else:
                int_num = False
        else :
            print("Не число, попробуйте еще раз")
    return n
n = num_biger_then_zero("Введите n : ") 
list = [1]
for i in range(1, n):
    list.append(list[i-1] * (i+1)) # [0] - 1 , 2 * (2 + 1) = 6, 6 * 4 = 24
print(f'Результат: {list}')  

