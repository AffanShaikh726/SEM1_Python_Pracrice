# print("Prime2")
# def isPrime (n) :
#     j = 2
#     iterationCounter = 1

#     while j < n/2:
#         iterationCounter += 1

#         if n % j == 0:
#             return False ,iterationCounter

#         j += 1

#     return True, iterationCounter

# counter = 2
# limit = int(input("Enter the limit: "))
# innerLoopIterationCounter = 0
# outerLoopIterationCounter = 1

# while counter <= limit:
#     outerLoopIterationCounter += 1

#     prime, iterations = isPrime(counter)
#     innerLoopIterationCounter += iterations

#     if prime:
#         print(counter,end=",")

#     counter += 1

# print("\n\nInner loop iterations: ", innerLoopIterationCounter)
# print("Outer loop iterations: ", outerLoopIterationCounter)

print("Prime2")

def isPrime (n) :
    j = 2

    while j < n/2:
        if n % j == 0:
            return False

        j += 1

    return True

counter = 2
limit = int(input("Enter the limit: "))

while counter <= limit:
    if isPrime(counter):
        print(counter,end=",")

    counter += 1




