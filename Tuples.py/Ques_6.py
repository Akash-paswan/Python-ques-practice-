#  ques 6  Create a tuple of 5 numbers from the user  and find their sum

nums = []     # creatre a empty list to store the numbers

for i in range(5):
    n = int(input("enter a number: "))
    nums.append(n) 
    
    
    
t = tuple(nums)   #    list is converted into tuple
print(t)
print("sum of the numbers is ",sum(t))