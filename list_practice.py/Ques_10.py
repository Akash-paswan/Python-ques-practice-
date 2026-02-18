num = [1,2,3,2,4,1,5,3]
unique =[]
for i in num:
    if i not in unique:
        unique.append(i)
print("list without duplicate elements:", unique)