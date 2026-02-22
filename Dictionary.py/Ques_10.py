original = {"a": 1, "b": 2}

reversed_dict = {}

for key, value in original.items():
    reversed_dict[value] = key

print(reversed_dict)