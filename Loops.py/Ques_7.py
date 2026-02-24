num = int(input("Enter number: "))
total = 0

while num > 0:
    digit = num % 10   # num ka last digit nikal liya
    total += digit
    num = num // 10   # num ko 10 se divide kar ke uska last digit hata diya

print("Sum of digits:", total) 