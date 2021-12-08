from multiprocessing import Pool
from random import randint


def doubler(number):
    #print(number)
    result = 1
    #for index in massiv:
    #print(index)
    element = [ int(c) for c in str(number)]
    first = element[0]
    second = element[1]
    #print(first)
    #print(second)
    if first % 2 == second % 2:
        #result = first
        print(number)
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
    pool = Pool(processes=2)
    result_process = (pool.map(doubler, lst))
    result = 1
    for k in result_process:
        result *= k
    if result == 1:
        print('Not foud valid numbers in matrix')
    else:
        print('Product of valid numbers: ' + str(result))