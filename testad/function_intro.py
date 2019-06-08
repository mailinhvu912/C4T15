# declare func -> ngắn gọn 
def introduce(name,age):
    # print("I'm", name, ',', age)
    return "I'm" + name + ',' + str(age)
    # print(1) unreachable code vì return end code

# call func
a = introduce("Linh", 18)
print(a)