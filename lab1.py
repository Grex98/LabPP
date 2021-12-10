from multiprocessing import Pool
from random import randint
import os

def potok(massiv):
    potoks = len(massiv)//2+1
    return potoks

def doubler(massiv):
    #print(number)
    result = 1
    proc = os.getpid()
    for index in massiv:
        #print(index)
        element = [ int(c) for c in str(index)]
        first = element[0]
        second = element[1]
        #print(first)
        #print(second)
        if first % 2 == second % 2:
            result *= first
            print('{0} Product {1} by process id: {2}'.format(massiv, result, proc))
        if result == 0:
            return 1
    return result


if __name__ == '__main__':
    n = randint(2, 10)
    matrix = [[randint(100, 999) for _ in range(n)] for _ in range(n)]
    print('Original matrix: ' + str(matrix))
    lst = []
    for line in matrix:
        lst += line
    print('Matrix elements: ' + str(lst))
    current_potoks = potok(matrix)
    pool = Pool(processes=current_potoks)
    print(current_potoks)
    result_process = (pool.map(doubler, matrix))
    result = 1
    for result_numbers in result_process:
        result *= result_numbers
    if result == 1:
        print('Not found valid numbers in matrix')
    else:
        print('Product of valid numbers: ' + str(result))