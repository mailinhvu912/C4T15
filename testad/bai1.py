# 1
a = int(input('enter a number: '))
b = int(input('enter a number: '))
print('sum = ', a, '+', b, '=', a + b)

# 2
year = int(input('enter a year: '))
if year%4 == 0:
    print(year, 'is a leap year')
else:
    print(year, 'is not a leap year')

# 3
x = input('enter a number: ')
print(x, 'has', len(x), 'digits')

# 4
for i in range(1):
    print(*range(3,21,3))

# 5
list = [1, 4, 5, 7, 8, 9]
new = int(input('enter new number: '))
list.append(new)
print(list)
x = int(input('enter a number at the head: '))
list.insert(0, x)
print(list)
dele = input('which number do u want to delete: ')
if dele == 'head':
    list.pop(0)
    print(list)
else:
    list.pop(-1)
    print(list)