def sequence_Generator():
    numberArray = [2]
    element = numberArray[0]
    for i in range(100):
        
        if (2*(i+1)) % 10 != 0:
            element += 2*(i+1)
            numberArray.append(element)

    # print(numberArray)
    return numberArray

def sum_of_sequence(sequence) :
    seq = sequence
    sum = 0
    for i in range(len(seq)):
        sum += seq[i]

    return sum

sum = sum_of_sequence(sequence_Generator())
print(f"SUM = {sum}")

