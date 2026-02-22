#   Ques9    python is easy and python is powerful"
# Count how many times each word appears (Word Frequency Counter).



sentence = "python is easy and python is powerful"
words = sentence.split()
frequenct = {}
for word in words:
    if word in frequenct:
        frequenct[word] += 1
    else:
        frequenct[word] = 1
        
print(frequenct)        