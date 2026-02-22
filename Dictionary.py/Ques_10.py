#  ques 10: Write a Python program to reverse the key-value pairs of a dictionary.


original = {"a": 1, "b": 2}

reversed_dict = {}

for key, value in original.items():
    reversed_dict[value] = key

print(reversed_dict)