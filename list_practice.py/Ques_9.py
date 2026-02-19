#  ques 9: Write a Python program that takes 5 numbers as input from the user, stores them in a list, and then calculates and prints the average of those numbers.

num = []


for i in range(5):
    n = int(input("Enter a number: "))
    num.append(n)
    
    average = sum(num) / len(num)
    print("numbers are:",num)
    print("average is:",average)
           
           
      
        #  nums.append(n) kaa mtlab niche likha haun 
# Number ko list me add kar rahe hain.  
        