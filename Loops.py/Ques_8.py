num = int(input("Enter number: "))
rev = 0
while  num >0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10
print("Reverse of the number:", rev)



    # 🔹 First Round
    # digit = 123 % 10

    # 👉 Last digit milega → 3

    # rev = 0 * 10 + 3

    # 👉 rev = 3

    # num = 123 // 10

    # 👉 12

    # 🔹 Second Round
    # digit = 12 % 10 = 2
    # rev = 3 * 10 + 2 = 32
    # num = 12 // 10 = 1
    # 🔹 Third Round
    # digit = 1 % 10 = 1
    # rev = 32 * 10 + 1 = 321
    # num = 1 // 10 = 0

    # Ab num = 0