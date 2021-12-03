def season(q):
    if q<0:
        return 'Номера месяца в диапазоне 0-12'
    elif q>0 and q<3:
        return 'Это зима,чел'
    elif q>2 and q<6:
        return 'Это весна,ну'
    elif q>5 and q<9:
        return 'Это лето кста,ага'
    elif q>8 and q<11:
        return 'Не ну это ба..осень всм'
    elif q>10 and q<13:
        return 'Зима,брр'
    
    
