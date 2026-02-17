# question 8: Write a Python program that creates a list of numbers and prints only the even numbers from the list.
nums = [1, 2, 3, 4, 5, 6]
even = []
for n in nums:
    if n % 2 == 0:
        even.append(n)
print(even)