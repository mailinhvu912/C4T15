from random import randint
while True:
    a = int(randint(0,20))
    print(a)
    b = int(randint(0,20))
    print(b)
    
    c = a + b
    d = a - b
    Answer = int(input("a + b = "))
    if Answer == c:
        print("correct")
        Answer_2 = int(input("a - b = "))
        if Answer_2 == d:
            print("correct")
        else:
            print("incorrect")
            break
    else:
        print("incorrect")
    break





