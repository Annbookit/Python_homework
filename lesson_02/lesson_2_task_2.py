d = input ("Введите год:")

def is_year_leap (l):
    x = int (l)
    if (x % 4 == 0):
        return True
    else:
        return False

c = is_year_leap(d)
a = str (c)
print("Год " + d + ": " + a) 
