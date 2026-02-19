#  ques 9 Remove duplicates from a tuple
t = (1, 2, 3, 2, 4, 1)

unique = []

for n in t:
    if n not in unique:
        unique.append(n)

t2 = tuple(unique)
print(t2)
