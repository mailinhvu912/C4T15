store = {
    'laptop' : ['HP', 'DELL', 'MACBOOK', 'ASUS'],
    'storage' : [20, 50, 12, 30]
}

store['laptop'].append(input('enter new brand: '))
store['storage'].append(int(input('enter numbers: ')))

print(sum(store['storage']))

y = int(input('enter laptop code: '))
print(store['laptop'][y], store['storage'][y])

store['price'] = [1500, 1000, 500, 430, 700]
price = int(input('enter your number of laptops: '))
print('pay =', store['price'][y] * price)

for x in range(0,5):
    print(store['laptop'][x], store['storage'][x], (store['storage'][x]) * (store['price'][x]))
