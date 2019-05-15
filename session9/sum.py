number1 = int(input("enter the 1st number: "))
number2 = int(input("enter the 2nd number: "))
number3 = int(input("enter the 3rd number: "))
number4 = int(input("enter the 4th number: "))

numbers = []

numbers.append(number1)
numbers.append(number2)
numbers.append(number3)
numbers.append(number4)

print(*numbers, sep="'")
b = sum(numbers)
print(b)




