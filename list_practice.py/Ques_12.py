#ques 12: Write a Python program to find the maximum and minimum values in a list.
nums = [10, 5, 20, 3]
#   isme max pr main ek variable hai 
maximum = nums[0]    # kuki hume comparison start karne ke liye
minimum = nums[0]
                        # list ka koi ek real number chahiye

                             # Aur sabse easy hai pehla element (nums[0]).

for n in nums:
    if n > maximum:
        maximum = n
    if n < minimum:
        minimum = n

print("Max:", maximum)
print("Min:", minimum)
