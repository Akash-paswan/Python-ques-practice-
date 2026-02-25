num = int(input("enter number "))
i = 2 
is_prime = True 


while i <num:
    if num% i == 0: 
        is_prime = False
        break 
    i +=1
    
if is_prime and num>1:
    print("prime")   
else :
    print("not prime")      