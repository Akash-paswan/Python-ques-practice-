#  ques Write a function that takes name and age as arguments and prints them using keyword arguments.

def students(name,age):
    print("name:",name)
    print("age:",age)
    
students( age = 20 ,name = "akash")    # yah nkeyword argument hai jisme name aur uski value likhna hota hai 
# students("Akash",20)      # normal argument 


#   keyword argument me order important nhi hota hai