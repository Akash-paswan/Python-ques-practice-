# question 6: Write a Python program that creates a list of numbers from 1 to 20 and prints only the even numbers from the list.
nums = list(range(1, 21))
even = []

for n in nums:
    if n % 2 == 0:
        even.append(n)

print(even)

