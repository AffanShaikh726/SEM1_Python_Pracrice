#print 2,3,5,7,11 ... N
print("Prime1")
counter = 2
limit = int(input("Enter the limit: "))
innerLoopIterationCounter = 1
outerLoopIterationCounter = 1

while counter <= limit:
    dBY = 0          #divisibility counter
    outerLoopIterationCounter += 1
    
    for i in range(1, counter + 1):
        innerLoopIterationCounter += 1        
        if counter % i == 0:
            dBY += 1 #Increasing the divisibility counter by 1 to  tell us how many divisors the number has

    if dBY == 2:     #We know that a prime number is divisible by 1 and itself therefore if the divisibility counter is 2, then the number is prime
        print(counter, end=",")

    counter += 1

print("\n\nInner loop iterations: ", innerLoopIterationCounter)
print("Outer loop iterations: ", outerLoopIterationCounter)