school = {
    "class": "12 Physics 2",
    "floor": "1st",
    "building": "A"
}
print(school)
# create
key = input("enter new section: ")
value = input("enter new description: ")
school[key] = value
# update
key2 = input("enter needed-update key: ")
value2 = input("enter updated info: ")
school[key2] = value2
# delete
del school['class']
# check
if "name" in school:
    print("'name' exist in school" )
else:
    print("'name' doesnt exist in school")
print(school)