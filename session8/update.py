names = ["hydra", "glad", "kronos"]

names[1] = "C+"
print(*names, sep=", ")

position = int(input("Đội số: ", ))
names[position] = input("Tên đội mới: ", )
print(*names, sep=", ")
