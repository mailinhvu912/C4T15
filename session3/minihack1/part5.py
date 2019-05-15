from random import randint
Score = 0
while True:
    a = randint(0,20)
    b = randint(0,20)
    c = randint(0,40)
    print(a ,"+", b ,"=", c)

    Answer = input("Is this correct?", )

    if c == (a + b):
        if Answer == "yes":
            print("Well done")
            Score+=1
            print("Score =", Score)
        else:
            print("Game over")
            print("Score =", Score)
            break
    elif c != (a + b):
        if Answer == "no":
            print("Well done")
            Score+=1
            print("Score =", Score)
        else:
            print("Game over")
            print("Score =", Score)
            break

            