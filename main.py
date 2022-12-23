#!/usr/bin/env python3
import argparse


parser = argparse.ArgumentParser(
                            prog='fractionkiller',
                            description='add and subtract fractions without reducing!',
                            epilog='made by gwim')
parser.add_argument('-l', '--add', action='store_true', help='Add two fractions')
parser.add_argument('-s', '--sub', action='store_true', help='Subtract two fractions')
args = parser.parse_args()


class style():
    BOLD = '\033[1m'
    END = '\033[0m'

def add(a, b, c, d):
    numerator = a + c
    #if numerator > 32:
    #    print('Error: Number too big')
    #    exit()
    denominator = 32
    return print(f'{numerator}/{denominator}')

def sub(a, b, c, d):
    numerator = a - c
    if numerator < 0:
        print('Error: Negative number')
        exit()
    denominator = 32
    return print(f'{numerator}/{denominator}')
    
def check_input():
    if args.add:
        check_var_add()
    elif args.sub:
        check_var_sub()
    else:
        print('Error: No arguments')
        exit()


def check_var_add():
    a = str(input('a: '))    
    print('/')
    b = str(input('b: '))   
    a = a.split('/')[0]
    b = b.split('/')[0] 
    a = int(a)
    b = int(b)
    return add(a, 32, b, 32)

def check_var_sub():
    a = str(input('a: '))    
    print('/')
    b = str(input('b: '))
    a = a.split('/')[0]
    b = a.split('/')[0] 
    a = int(a)
    b = int(b)
    return sub(a, 32, b, 32)


if __name__ == '__main__':
    try:
        check_input()
    except KeyboardInterrupt:
        print('\n' + style.BOLD + 'Exiting...' + style.END)
        exit()
