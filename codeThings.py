my_list = [-5,52,-6,95,-3]

positive = []
for n in my_list:
    if n >= 0:
        positive.append(n)
print(positive)


double_positive = [x *2 for x in my_list if x >=0]
print(double_positive)


positive = [x for x in my_list if x >=0]
print(positive)

words = ['hi' , 'hello', 'world', 'python']
# make a list with uppercase

upperWord = [l.title() for l in words]
print(upperWord)

language = ['JS', 'C#', 'Java', 'Visual Basic.net']
# make a new list with strings longer than 3 letters

languageThree = [w for w in language if len(w) > 3]
print(languageThree)
