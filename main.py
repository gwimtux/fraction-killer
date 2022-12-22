import os



class style():
    BOLD = '\033[1m'
    END = '\033[0m'

def main_logo():
    print(style.BOLD + '''
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@ FRACTION KILLER (by gwim) @@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    ''' + style.END + '''         
              [l] - Add
              [s] - Subtract''')

os.system('clear')
def add(a, b, c, d):
    numerator = a + c
    #if numerator > 32:
    #    print('Error: Number too big')
    #    exit()
    denominator = 32
    return print(f'{numerator}/{denominator}')

os.system('clear')
def sub(a, b, c, d):
    numerator = a - c
    if numerator < 0:
        print('Error: Negative number')
        exit()
    denominator = 32
    return print(f'{numerator}/{denominator}')
    
os.system('clear')
def check_input():
    main_logo()
    print('''
    ''')
    i = input('> ')
    if i == 'l':
        check_var_add()
    elif i == 's':
        return check_var_sub()

def check_var_add():
    a = str(input('1: '))    
    b = str(input('2: '))   
    a = a.split('/')[0]
    b = b.split('/')[0] 
    a = int(a)
    b = int(b)
    return add(a, 32, b, 32)

def check_var_sub():
    a = str(input('1: '))    
    b = str(input('2: '))   
    a = a.split('/')[0]
    b = b.split('/')[0] 
    a = int(a)
    b = int(b)
    return sub(a, 32, b, 32)


if __name__ == '__main__':
    try:
        check_input()
    except KeyboardInterrupt:
        print('\n' + style.BOLD + 'Exiting...' + style.END)
        exit()
