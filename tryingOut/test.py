import os
def clear_terminal():
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For macOS and Linux
    else:
        os.system('clear')

clear_terminal()
print("OUTPUT :")


thisset = {"apple", True, 89, "cherry"}
# print(thisset)
# print(len(thisset))
# print(type(thisset))

# for x in thisset:
#     print(x)    

# print("apple" in thisset)

# thisset.add("banana")
# print(thisset)

# tropical = {"pineapple", "mango", "papaya"}
# thisset.update(tropical)
# print(thisset)

# thisset.remove("banana")
# print(thisset)

thisdict = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
print(thisdict)
print(thisdict["brand"])

# thistuple = ("apple", "banana", "cherry", "apple")
# print(thistuple)