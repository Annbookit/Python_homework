def month_to_season (n):
    
    if n == 1 or n == 2 or n == 12:
        return "Зима"
    elif n == 3 or  n == 4 or n == 5:
        return "Весна"
    elif n == 6 or n == 7 or n == 8:
        return "Лето"
    elif n == 9 or n == 10 or n == 11:
        return "Осень"
    else:
        return 0

v = month_to_season (8)
a = str (v)
print ("Сезон: " + a)