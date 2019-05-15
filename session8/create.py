names = ["Hydra", "Glad", "Kronos", "C+"]
print(names)

New = input("Tên đội mới là: ")
names.append(New)
print(*names, sep=', ')
print(*names, sep='| ')

x = int(input("Đội ", ))
print(names[x])
print(names[0].upper())
print(names[-1].upper())
print(names[-2].upper())


