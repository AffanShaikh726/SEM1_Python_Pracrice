from lvl1 import sum_of_sequence
from lvl1 import sequence_Generator
import os

# def clear_terminal():
#     # For Windows
#     if os.name == 'nt':
#         os.system('cls')
#     # For macOS and Linux
#     else:
#         os.system('clear')

# # Clear the terminal
# clear_terminal()

def descendingNumbers() :
    seq = sequence_Generator()
    descendingElements = []
    digits = []
    sameDigitsFlag = 0 # eg. 22 , 333

    for i in range(3,len(seq)):
        for j in str(seq[i]):
            digits.append(j)

        for k in range(len(digits)):
            if digits[0] == digits[k]:
                sameDigitsFlag += 1

        if digits == sorted(digits, reverse=True) and sameDigitsFlag != len(digits):
            descendingElements.append(seq[i])
        
        sameDigitsFlag = 0    
        digits = []

    return descendingElements

sum2 = sum_of_sequence(descendingNumbers())
print(f"SUM2 = {sum2}")