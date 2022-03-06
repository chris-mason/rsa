# Python implementation of Carmichael's Function

import time

def check(coprimes, m, n):
    for coprime in coprimes:
        if ((coprime**m) % n) != 1:
            return False
    return True

def is_coprime(x, y):
    for i in range(2, max(x,y)):
        if (x % i == 0 and y % i == 0):
            return False;

    return True;

def find_carmichaels(n):
    coprimes = []

    for i in range(1, n):
        if is_coprime(i, n):
            coprimes.append(i)
            
    m = 1
    while True:
        for coprime in coprimes:
            while ((coprime**m) % n) != 1:
                m += 1
        
        if check(coprimes, m, n):
            return m

    return -1

start_time = time.time()

v = 100000
carmichaels = find_carmichaels(v)
print(f'Carmichaels function of {v} is: {carmichaels}')
print("--- %s seconds ---" % (time.time() - start_time))
