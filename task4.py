# 4 - Реализуйте выдачу случайного числа (или алгоритм перемешивания списка)
# не использовать random.randint и вообще библиотеку random
# Можете использовать xor, биты, библиотеку time (миллисекунды или наносекунды) - для задания случайности

from functools import reduce
import operator

lst_1=[1,2,3]
lst_2=['test1','test2','test3']

res = reduce(operator.add, zip(lst_2,lst_1))
print(res)

import time

sting_time = str(time.time_ns())

list_of_numbers = [1,2,3,4,5,6,7,8,9,10]# Специально его просто задал тут что бы были видны изменения каждый раз при обновлении 
print(list_of_numbers)
for i in range(0,len(list_of_numbers)):
    for j in sting_time:
        if int(j) < len(list_of_numbers):
            list_of_numbers[i],list_of_numbers[int(j)] = list_of_numbers[int(j)],list_of_numbers[i]

print(list_of_numbers)
