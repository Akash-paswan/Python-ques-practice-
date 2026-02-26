#  ques ATM machine simulation (withdraw until balance becomes 0

balance = 1000

while balance > 0:
    withdraw = int(input("Enter amount to withdraw: "))
    
    if withdraw <= balance:
        balance -= withdraw
        print("Remaining balance:", balance)
    else:
        print("Insufficient balance")

print("Balance is 0. Thank you!")