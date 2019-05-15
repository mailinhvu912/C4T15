districts = ["ST", "BD", "BTL", "CG", "DD", "HBT"]
populations = [150300, 247100, 333300, 266800, 420900, 318000]
area = [117.43, 9.224, 43.35, 12.04, 9.96, 10.09]

matdo = [populations[0]/area[0], populations[1]/area[1], populations[2]/area[2], populations[3]/area[3], populations[4]/area[4], populations[5]/area[5]]
average = sum(matdo)/len(districts)
zipped = zip(districts, area, populations, matdo)

print(list(zipped))
print("The average people on a kilometer are: ", average)

if min(populations) == populations[0]:
    print("The district has the smallest population is: ", districts[0], "with", min(populations))
elif min(populations) == populations[1]:
    print("The district has the smallest population is: ", districts[1], "with", min(populations))
elif min(populations) == populations[2]:
    print("The district has the smallest population is: ", districts[2], "with", min(populations))
elif min(populations) == populations[3]:
    print("The district has the smallest population is: ", districts[3], "with", min(populations))
elif min(populations) == populations[4]:
    print("The district has the smallest population is: ", districts[4], "with", min(populations))
elif min(populations) == populations[5]:
    print("The district has the smallest population is: ", districts[5], "with", min(populations))

if max(populations) == populations[0]:
    print("The district has the biggest population is: ", districts[0], "with", max(populations))
elif max(populations) == populations[1]:
    print("The district has the biggest population is: ", districts[1], "with", max(populations))
elif max(populations) == populations[2]:
    print("The district has the biggest population is: ", districts[2], "with", max(populations))
elif max(populations) == populations[3]:
    print("The district has the biggest population is: ", districts[3], "with", max(populations))
elif max(populations) == populations[4]:
    print("The district has the biggest population is: ", districts[4], "with", max(populations))
elif max(populations) == populations[5]:
    print("The district has the biggest population is: ", districts[5], "with", max(populations))
