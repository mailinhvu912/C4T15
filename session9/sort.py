scores = [43, 56, 98, 23, 50]
new_score = int(input("Enter your new highscore: "))
scores.append(new_score)

highscore = sorted(scores, reverse = True)[:5]
print(*highscore)

for i, hi in enumerate(highscore):
    print(i, hi)