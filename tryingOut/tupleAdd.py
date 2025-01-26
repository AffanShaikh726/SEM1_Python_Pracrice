def tupleAdd(T): 
    L = list(T)
    L.append(int(input("Enter the new element : ")))
    T = tuple(L)
    return T

# T = (2, 3, 4, 5, 6)
# print("Tuple before adding new element")
# print(T)
# L = list(T)
# L.append(int(input("Enter the new element : ")))
# T = tuple(L)
# print("Tuple After adding the new element")
# print(T)

T = (2, 3, 4, 5, 6)
print("Tuple before adding new element")
print(T)
T = tupleAdd(T)
print("Tuple After adding the new element")
print(T)