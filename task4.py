# 4 - Реализуйте выдачу случайного числа (или алгоритм перемешивания списка)
# не использовать random.randint и вообще библиотеку random
# Можете использовать xor, биты, библиотеку time (миллисекунды или наносекунды) - для задания случайности

from functools import reduce
import operator

lst_1=[1,2,3]
lst_2=['test1','test2','test3']

res = reduce(operator.add, zip(lst_2,lst_1))
print(f'Результат: {res}')


