dict = {
    "MANAGER" : "In charge of scheduling and team building",
    "CAPTAIN" : "In charge of leading the trainings",
    "COACH" : "In charge of trainings and choosing 12 players"
}
while True:
    for i in range(0,4):
        search = input("enter your position here: ")
        print(dict[search. upper()])