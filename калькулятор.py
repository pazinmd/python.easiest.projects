print('Введите два числа и необходимое вычисление в формате ЧИСЛО1,ЧИСЛО2,"ЗНАК ОПЕРАЦИИ"')
def arithmetic(x,y,z):

    if z=='+':
        return x+y
    elif z=='-':
        return x-y
    elif z=='*':
        return x*y
    elif z=='/':
        return x/y
    else:
        return 'Неизвестная операция'
