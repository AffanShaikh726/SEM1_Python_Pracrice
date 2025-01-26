#print 2,-4,6,-8,10 ... N
counter = 1
nterms = int(input("Enter the number of terms: "))

while counter <= nterms:
    print((counter*2)*((-1)**(counter-1)),end=" , ")
    counter += 1

    