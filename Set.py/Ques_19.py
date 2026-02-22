text = input("Enter string: ")
vowels = {'a', 'e', 'i', 'o', 'u'}

found = {ch for ch in text.lower() if ch in vowels}

print("Unique vowels:", found)
print("Count:", len(found))