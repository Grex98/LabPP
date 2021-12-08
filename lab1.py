from multiprocessing import Pool

def doubler(massiv):
    print(massiv)
    result = 1
    for index in massiv:
        #print(index)
        element = [ int(c) for c in str(index)]
        first = element[0]
        second = element[1]
        #print(first)
        #print(second)
        if first % 2 == second % 2:
            result *= first
            print(result)
    return result




if __name__ == '__main__':
    numbers = [[165, 531, 884, 416],
    [494, 256, 779, 948],
    [398, 589, 832, 538],
    [416, 756, 432, 895]]

    pool = Pool(processes=5)
    result_process = pool.map(doubler, numbers)
    r = 1
    for k in result_process:
        r*=k
    print(r)