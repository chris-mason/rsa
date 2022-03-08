# Python implementation of Carmichael's Function

import time

def main():
    value = input('Enter value at which to determine the Carmichael function: ')
    start_time = time.time()
   
    try:
        carmichaels = find_carmichaels(int(value))
    except ValueError:
        print('Error: Please provide an integer value')
        raise SystemExit

    print(f'\u03bb({value}) = {carmichaels}')
    print(f'{time.time() - start_time} seconds elapsed')


def is_valid(coprimes, m, n):
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
    m = 1
    coprimes = []

    for i in range(1, n):
        if is_coprime(i, n):
            coprimes.append(i)

    while True:
        for coprime in coprimes:
            while ((coprime**m) % n) != 1:
                m += 1
        
        if is_valid(coprimes, m, n):
            return m

    return -1


if __name__ == '__main__':
    main()

