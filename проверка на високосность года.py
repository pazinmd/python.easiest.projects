def is_year_leap(x):
    if int(x)<0:
        return('Год не может быть отрицательным')
    elif int(x)%400 == 0:
        return('Год является високосным')
    elif  int(x)%100 == 0:
        return('Год НЕ является високосным')
    elif  int(x)%4 == 0:
        return('Год является високосным')
    else:
        return('Год НЕ является високосным')
