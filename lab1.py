from multiprocessing import Pool


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
    #print(first)
        return first
    else:
        return 1






if __name__ == '__main__':
    matrix = [[165, 531, 884, 416],
    [494, 256, 779, 948],
    [398, 589, 832, 538],
    [416, 756, 432, 895]]
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
