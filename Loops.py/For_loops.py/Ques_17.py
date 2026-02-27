# list1 = [1, 2, 3, 4]
# list2 = [3, 4, 5, 6]

# for num in list1:
#     if num in list2:
#         print(num)


#  isko aur kisi method sw kar skte haiu 

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

# Convert lists to sets and find intersection
common = set(list1).intersection(set(list2))

print("Common elements:", common)

