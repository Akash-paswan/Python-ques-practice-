    
word = input("Enter a word: ").lower()

if word[-1] in "aeiou":
    print("Ends with vowel")
else:
    print("Ends with consonant")
