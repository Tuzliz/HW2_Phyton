# обеспечивает наилучшие часы, присваивается time.time() или time.clock()
from random import random
from timeit import default_timer as timer
def sporadic_number():
    oper_moment = timer()
    textp = str(oper_moment).split('.')
    rndnum = (int(textp[0])^int(textp[1])) %10
    print(rndnum)
sporadic_number()    
# пример с timer и xor (или не) пример: 26ˆ3 -> 1
# проводит битовую операцию xor исключающее или не для 10(2) и 11(3) будет 01(1)

from datetime import datetime
def occasional_number():
    moment_date = datetime.datetime.today()
    random = int(f'{moment_date.year}' + f'{moment_date.month}' + f'{moment_date.day}')
print(random)