# 4 - Реализуйте выдачу случайного числа (или алгоритм перемешивания списка)
# не использовать random.randint и вообще библиотеку random
# Можете использовать xor, биты, библиотеку time (миллисекунды или наносекунды) - для задания случайности

# Случайное число вариант 1: 
from time import time 
num = int(input('Введите число от 1 до 1000000:'))
x = time()                       #  число из библ time 
strNum = str(num)                  
strNum = strNum.replace('.','')    
number = int(strNum)
rnd_num = x // number
print(f'Результат:{rnd_num}')

# вариант 2: 
from time import time # используем библиотеку time
def time_random():
 return time() - float(str(time()).split('.')[0]) 
print(time()) 
print(str(time_random()))

def gen_random_range(min, max): # генерируем промежуток выдачи числа 
 return int(time_random() * (max - min) + min) #умножаем число на разность минимального и иаксимального значения плюс минуты 

if __name__ == '__main__':
 for i in range(1): # выдаем число из заданного промежутка
     print (gen_random_range(10,100000))





#from functools import reduce
#import operator

#lst_1=[1,2,3]
#lst_2=['test1','test2','test3']

#res = reduce(operator.add, zip(lst_2,lst_1))
#print(f'Результат: {res}')


