# # Bai1:
# print(*range(3,13,1))

# # Bai2:
# n = int(input("enter a number:", ))
# if int(n%2) == 0:
#     print(*range(n-1,-1,-2))
# else:
#     print(*range(n,-1,-2))

# Bai3:
from turtle import *

n = int(input("Enter the number of sides:"))
shape("turtle")
for i in range(n):
    forward(100)
    left(360/n)
mainloop()