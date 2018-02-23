import math
import time
import random

def stooge(arr, low, high):
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

#Timing functionality 

#generate lists of ints of size size with values from 1-10000
def rando(arr, size):
    i = 0
    while i < size:
        arr.append(random.randint(1, 10000))
        i+=1
    return arr

#7 lists containing unsorted values from 1-10000
list1k = []
list1k = rando(list1k, 32);

list2k =[]
list2k = rando(list2k, 64);

list4k =[]
list4k= rando(list4k, 128);

list8k =[]
list8k = rando(list8k, 256);

list16k =[]
list10k = rando(list16k, 512);

list32k =[]
list20k = rando(list32k, 1024);

list48k =[]
list40k = rando(list48k, 2048);

#Add all lists to a larger list
megalist =[list1k, list2k, list4k, list8k, list16k, list32k, list48k]
j = 1

for i in megalist:
    print ("***MERGE SORT***")
    start_time = time.time()
    stooge(i, 0, len(i)-1)
    print("Time for a list of ", len(i), " elements:")
    print(time.time() - start_time)