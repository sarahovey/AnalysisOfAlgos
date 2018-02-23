def insert_sort(numbers):
    #n-1 passes for n items
    #O(n^2)
    for i in range(1, len(numbers)):
        currentVal = numbers[i]
        pos = i
        
        #sorted sublist
        #if pos is greater than the thing before it, swap them
        while pos > 0 and numbers[pos-1] > currentVal:
            numbers[pos] = numbers[pos-1]
            pos = pos-1
            
        numbers[pos] = currentVal

#Reading from file
with open('data.txt', 'r') as fIn:
    count =1
    line = fIn.readline()
    while line:
        #Get the first number
        #numbersIn = fIn.readline()
        numbersIn = line
        toSort = numbersIn[0]
        int(toSort)
        print("Numbers to sort:")
        print toSort
        
        #get the remaining numbers into a list as integers
        numStrIn = numbersIn[1:]
        #print (numStr)
        
        numbers = [int(s) for s in numStrIn.split()]
        print("Unsorted values:")
        print(numStrIn)
        
        #Call function
        insert_sort(numbers)
        
        #Write to file
        with open('insert.out', 'a') as fOut:
            #format sorted values for writing
            numStrOut = ' '.join(str(e) for e in numbers)
            fOut.write("%s\n" % (numStrOut))
            print("Sorted values:")
            print(numStrOut)
        line = fIn.readline()
        count +=1