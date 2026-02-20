# ques 2 create a dictionary that stores the name of 5 fruits and their prices and ask the user to enter a fruit name and print the price of that fruit if it is present in the dictionary otherwise print fruit not found
fruits ={
    "apple" : 240,
    "banana": 70,
    "orange":120,
    "Grapes": 150,
    "pineapple":200 
}
fruit_name =input("enter fruit name :")
if fruit_name in fruits:
    print("the price of fruit_name is:",fruits[fruit_name])
else :
    print("fruit not found ")