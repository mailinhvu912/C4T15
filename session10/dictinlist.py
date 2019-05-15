Huy = {
    "name" : "Huy",
    "role" : "Waiter",
    "hours_of_work" : 12,
    "salary_per_hour" : 0.8
}
Duc = {
    "name" : "Duc",
    "role" : "Chief",
    "hours_of_work" : 12,
    "salary_per_hour" : 1.5
}
Linh = {
    "name" : "Linh",
    "role" : "Manager",
    "hours_of_work" : 12,
    "salary_per_hour" : 2
}

wages = [Huy, Duc, Linh]
wages[0] = {
    'name' : 'Huyen',
    'role' : 'Waitress',
    'hours_of_work' : 14,
    'salary_per_hour' : 1
}

money0 = wages[0]["salary_per_hour"]*wages[0]["hours_of_work"]
wages[0]['money'] = money0
money1 = Duc["salary_per_hour"]*Duc["hours_of_work"]
Duc['money'] = money1
money2 = Linh["salary_per_hour"]*Linh["hours_of_work"]
Linh['money'] = money2

for i, wage in enumerate(wages):
    print(wage)

total = [money0, money1, money2]
print(sum(total))

