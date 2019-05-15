character = {
    'name' : 'light',
    'age' : 17,
    'strength' : 8,
    'defense' : 10,
    'HP' : 100,
    'backpack' : ['shield', 'bread loaf'],
    'gold' : 100,
    'level' : 2
}

character['gold'] = 100 + 50
character['backpack'].append('flintstone')
character['pocket'] = ['monsterdex', 'flashlight']
print(character)

skill1 = {'name' : 'tackle', 'minimum level' : 1, 'damage' : 5, 'hit rate' : 0.3}
skill2 = {'name' : 'quick attack', 'minimum level' : 2, 'damage' : 3, 'hit rate' : 0.5}
skill3 = {'name' : 'strong kick', 'minimum level' : 4, 'damage' : 9, 'hit rate' : 0.2}

skill = [skill1, skill2, skill3]
for x in enumerate(skill):
    print(*x)

pick_skill = int(input("enter skill code: "))
if pick_skill <= character['level']:
    print('your level is strong enough to combat')
else:
    print('there will be damage at', skill[pick_skill]['damage'])

from random import randint
h = randint(0,1)
print('your hit rate: ', h)
if h <= skill[pick_skill]['hit rate']:
    print('there will be damage at', skill[pick_skill]['damage'])
elif h >= skill[pick_skill]['hit rate']:
    print('you misssed the target')




