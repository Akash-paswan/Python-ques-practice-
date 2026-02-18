# ques 14 Check if all numbers in a list are positive.

nums = [5, 10,3, 8, 2]

all_positive = True    # Shuru me maan liya ki sab positive hain

for n in nums:
    if n <= 0:               # Agar koi bhi number zero ya negative mila, to all_positive ko False kar do
        all_positive = False
        break

if all_positive:
    print("All numbers are positive")
else:
    print("Not all numbers are positive")

