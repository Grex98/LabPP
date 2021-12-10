from multiprocessing import Pool
from random import randint
import os

def potok(lst):
    potoks = len(lst)//10
    return potoks

def parser(number):
    #print(number)
    result = 1
    proc = os.getpid()
    #for index in massiv:
    #print(index)
    element = [ int(c) for c in str(number)]
    first = element[0]
    second = element[1]
    print('{0} find to {1} by process id: {2}'.format(
    number, first, proc))
    #print(first)
    #print(second)
    if first % 2 == second % 2:
    #result = first
        print(first)
        return first
    else:
        return 1

if __name__ == '__main__':
    n = randint(2, 10)
    matrix = [[randint(100, 999) for _ in range(n)] for _ in range(n)]
    print('Original matrix: ' + str(matrix))
    lst = []
    for line in matrix:
        lst += line
    print('Matrix elements: ' + str(lst))
    print (len(lst))
    print(len(lst)//10)
    print(potok(lst))
    current_potoks = potok(lst)
    pool = Pool(processes=current_potoks)
    result_process = (pool.map(parser, lst))
    result = 1
    for k in result_process:
        result *= k
    if result == 1:
        print('Not foud valid numbers in matrix')
    else:
        print('Product of valid numbers: ' + str(result))