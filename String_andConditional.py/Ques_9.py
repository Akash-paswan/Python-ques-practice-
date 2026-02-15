word = input("enter a word :" )
if word == word[:: -1]:  # word[:: -1] is used to reverse the string
    print("palindrome")
else :
    print("not palindrome ")