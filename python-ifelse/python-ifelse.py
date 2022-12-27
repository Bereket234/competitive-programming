#!/bin/python3
def find_weird_num(n):
    if n%2 != 0 or 6<= n <=20:
        return 'Weird'
    else:
        return 'Not Weird'

if __name__ == '__main__':
    n = int(input().strip())
    
    print(find_weird_num(n))

