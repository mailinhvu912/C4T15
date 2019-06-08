# Tìm ước số chung lớn nhất của 2 số bằng phương pháp Euclid, Link tham khảo:
# tìm min của dãy
# list = [1, 5, -8, 9 , 10]
# print(min(list))

# tìm fib
def fibbonacii(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    else:
        return fibbonacii(n-1) + fibbonacii(n-2)

n = int(input('enter a number'))
print(fibbonacii(n))

