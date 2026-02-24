num = int(input("Enter number: "))
total = 0

while num > 0:
    digit = num % 10   # num ka last digit nikal liya
    total += digit
    num = num // 10   # num ko 10 se divide kar ke uska last digit hata diya

print("Sum of digits:", total) 



# 🔹 First Round
# digit = 123 % 10

# 👉 % 10 last digit deta hai
# 123 % 10 = 3

# total = 0 + 3 = 3
# num = 123 // 10

# 👉 // 10 last digit hata deta hai
# 123 // 10 = 12

# 🔹 Second Round
# digit = 12 % 10 = 2
# total = 3 + 2 = 5
# num = 12 // 10 = 1
# 🔹 Third Round
# digit = 1 % 10 = 1
# total = 5 + 1 = 6
# num = 1 // 10 = 0