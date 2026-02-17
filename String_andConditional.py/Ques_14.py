    #  question 14: Write a Python program that takes a word as input and checks if it ends with a vowel or a consonant.
word = input("Enter a word: ").lower()

if word[-1] in "aeiou":
    print("Ends with vowel")
else:
    print("Ends with consonant")
