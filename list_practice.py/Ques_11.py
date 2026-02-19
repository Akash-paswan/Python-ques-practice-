#  ques 11: Write a Python program to count the number of elements in a list that are greater than 10

nums = [5,15,25,8,12]
count = 0
for n in nums :
    if n > 10:
        count += 1 
print("Count of numbers greater than 10:", count)