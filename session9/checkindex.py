so = [1, 2, 6, -50]

item = int(input('Enter number: '))

# for i, item in enumerate(so):
#         if item in so:
#             print("found, position: ", so[?])
#         else:
#             print("unavailable")

# Phan chua cua mentor
if item in so:
    print("Position is", so.index(item))
else:
    print("not exist")
    
# em len tra google nhung van k lam dc cai hien index a :((((