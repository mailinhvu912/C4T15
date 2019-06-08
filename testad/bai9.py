import math
def quadro(a,b,c):
    delta = b**2 - 4*a*c
    if delta > 0:
        x1 = (-b + math.sqrt(b**2 - 4*a*c))/ (a*2)
        x2 = (-b - math.sqrt(b**2 - 4*a*c))/ (a*2)
        print('equation has 2 solutions, ', x1, x2)
        return x1,x2
        # tuple
    if delta == 0:
        x = -b/(2*a)
        print('equation has 1 solution, ', x)
        return x
    else:
        print('equation has no solution')
        return None
a = quadro(1,2,-3)
print(a)
# lệnh print tuple (print cái return)
   


