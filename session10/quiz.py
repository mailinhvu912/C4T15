quiz1 = {
    'question1' : 'how many legs does the frog have?',
    'answer1' : ['A. 4', 'B. 5', 'C. 2', 'D. 1']
}
print(quiz1)
result1 = input('enter your answer here: ').upper()

if result1 == 'A': 
    print('correct')
else:
    print('incorrect')

question2 = input('enter your question here: ')
answer2 = [input('A. '), input('B. '), input('C. ')]

print(question2, answer2)
quiz2 = {
    'question2' : question2,
    'answer2': answer2
}
print(quiz2)
correct = input('enter the correct answer: ').upper()
result2 = input('enter your friend answer here: ').upper()

if result2 == correct:
    print('correct')
else:
    print('incorrect')

if result1 == 'A' and result2 == correct:
    print('you answered correctly 2/2 = ', 2/2 *100, '%')

# em viet code hoi dai dong nma de nho em quen thi mai ngay em doc lai ah!
