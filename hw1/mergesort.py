#Sort
#Merge Sort
def merge_sort(numbers):
    #Divide the list into halves recursively
    if len(numbers) > 1:
        #get midpoint of list
        mid = len(numbers)/2
        left = numbers[:mid]
        right = numbers[mid:]
        
        merge_sort(left)
        merge_sort(right)
        
        #index variables
        i = 0 #left half
        j = 0 #right half
        k = 0 #final numbersay
        
        #Sorting
        #Make sure that the index falls in the bounds of the respective halves
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                numbers[k] = left[i]
                
                #increment
                i=i+1
            else:
                numbers[k] = right[j]
                j += 1
            k +=1
            
        #Merging
        while i < len(left):
            numbers[k] = left[i]
            i += 1
            k += 1
            
        while j < len(right):
            numbers[k] = right[j]
            j += 1
            k += 1

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
        merge_sort(numbers)
        
        #Write to file
        with open('merge.out', 'a') as fOut:
            #format sorted values for writing
            numStrOut = ' '.join(str(e) for e in numbers)
            fOut.write("%s\n" % (numStrOut))
            print("Sorted values:")
            print(numStrOut)
        line = fIn.readline()
        count +=1

    