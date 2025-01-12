import math
def disc(a, b, c):
    d = int(b) ** 2 -  (4 * int(a) * int(c))
    
    x1 = (int(-b) + math.sqrt(int(d))) / (2 * int(a))
    x2 = (int(-b) - math.sqrt(int(d))) / (2 * int(a))
    return x1

x1 = disc(1, 2 , 4)
print(x1)
