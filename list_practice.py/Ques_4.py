# Question 4: Write a Python program that creates a list of numbers and prints the list in reverse order.
num = [5,6,1,4,25,89]
# print(num[-1:-7:-1])
            # (start:stop:step)    step ,means reverse the list
# print(num[::-1])
print(num.reverse())   # ye bhi list ko reverse kar dega, lekin ye None return karega. kyuki ye list ko modify karta hai, aur kuch return nahi karta.
print(num)

