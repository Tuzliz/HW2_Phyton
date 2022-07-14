# 4 - Реализуйте выдачу случайного числа (или алгоритм перемешивания списка)
# не использовать random.randint и вообще библиотеку random
# Можете использовать xor, биты, библиотеку time (миллисекунды или наносекунды) - для задания случайности

# Случайное число: 
from time import time 
num = int(input('Введите число от 1 до 1000000:'))
x = time()                       #  число из библ time 
strNum = str(num)                  
strNum = strNum.replace('.','')    
number = int(strNum)
rnd_num = number // x 
print(f'Результат:{rnd_num}')




#from functools import reduce
#import operator

#lst_1=[1,2,3]
#lst_2=['test1','test2','test3']

#res = reduce(operator.add, zip(lst_2,lst_1))
#print(f'Результат: {res}')


