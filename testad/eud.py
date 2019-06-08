def gcd(x, y):
    print(x,y)
    # dòng này để hiện các bước làm
    if x > y:
        high = x
        low = y
    elif x < y:
        high = y
        low = x
    else:
        return x
    # return gcd(low, high-low ) 
    # không phải để như divisor vì nó là chia hết chứ chưa chắc bằng nhau
    divisor = high%low
    if divisor == 0:
        return low
    else:
        return gcd(low, high%low)

a = gcd(32,22)
print(a)

