#  ques Count how many even numbers are in a list

numbers = [1, 4, 7, 8, 10, 13]
count = 0

for num in numbers:
    if num % 2 == 0:
        count += 1

print("Even numbers count:", count)