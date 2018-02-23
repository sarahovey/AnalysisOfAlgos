import math

def stooge(arr, low, high):
    # #print("It's sorting time")
    # n = len(arr)
    # #Base case
    
    # if low >= high:
    #     return
    
    # if n == 2:
        
    #     if arr[0] > arr[1]:
    #         temp = arr[0]
    #         arr[0] = arr[1]
    #         arr[1] = temp
   
    # elif n>2:
    #     #Get points at 1/3 and 2/3 through the array
    #     m = int(math.ceil(((2*n)/3)))
    #     #Recursively sort first 2/3
    #     stooge(arr, low, (m-1))
    #     #Recursively sort last 2/3
    #     stooge(arr, n-m, n-1)
    #     #Check first 2/3 again
    #     stooge(arr, low,(m-1))
    
    n = high-low +1
    if n == 2 and arr[low] > arr[high]:
        temp = arr[low]
        arr[low] = arr[high]
        arr[high] = temp
        
    elif n >2:
        m = int(math.ceil(n/3))
        stooge(arr, low, high-m)
        stooge(arr, low+m, high)
        stooge(arr, low, high-m)
    
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
        length = len(numbers)
        stooge(numbers, 0, length -1)
        
        #Write to file
        with open('stooge.out', 'a') as fOut:
            #format sorted values for writing
            numStrOut = ' '.join(str(e) for e in numbers)
            fOut.write("%s\n" % (numStrOut))
            print("Sorted values:")
            print(numStrOut)
        line = fIn.readline()
        count +=1