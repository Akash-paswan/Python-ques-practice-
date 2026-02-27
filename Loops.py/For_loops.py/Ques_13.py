num = 12345
count = 0

for digit in str(num):   # 🔥 Kyu str(num) use kiya?

                        #     👉 num ek integer (number) hai
                        #   👉 For loop directly integer par nahi chal sakta

  count += 1
print("Total digits:", count)




# #  Iterable Kya Hota Hai?

# For loop sirf un cheezon par chal sakta hai jo iterable ho:

# ✔ String
# ✔ List
# ✔ Tuple
# ✔ Set

# Number iterable nahi hota.