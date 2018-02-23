def selectLast(set_number, activities):
    #set of completed activities
    completed = []
    
    #Sorting
    #print("sorting:")
    #Sorting by start time, since we're looking for last to start
    activities.sort(reverse = True, key = lambda x: x[1])
    last_start = activities[0]
    
    current_activity = last_start
    completed = [current_activity]
    #Find all compatible activities
    #skip the first activity
    #print(activities)
    i = 1
    for i in activities:
         #Check if compatible
         #Check activity[i] 's end time to see if it is less than current's start time
        if i[2] < current_activity[1]:
            #Add to schedule
            completed.append(i)
            #print(current_activity)
            #print(i)
            #Jump out of loop, reset current_activity to i
            current_activity = i
            
        
    print("Set:")
    print(set_number)
    print("Number of activities selected:")
    print(len(completed))
    print("Activities:")
    for i in completed:
        print(i[0])
    print("****")
    print("  ")
            

#File I/O
with open('act.txt', 'r') as file:
    line = file.readline()
    act_num = 0
    activities = []
    set_number = 0
    count = 0
    while line:
        #stick current line into new list as an int or set of ints
        cur_line = [int(s) for s in line.split()]
        #print (len(cur_line))
        #Representing when the current line is a sinle integer with the number of activities following
        #rint("len of cur line:")
        #print(len(cur_line))
        if len(cur_line)  <=1:
            #Call scheduling function
            #Because now we know the last set is complete
            if len(activities) > 0:
                set_number +=1
                selectLast(set_number, activities)
            #The start of a new set    
            if len(cur_line) == 1:
                #set up a new set of activities
                act_num = cur_line[0]
                #reset activities set in case there was anything in it
                activities = []
                # print("number of activities:")
                # print(act_num)
            
        if len(cur_line) >1:
            #There are multiple sets in the same file,
            #this handles only examining from one set at a time
            #print(cur_line)
            new_activity = cur_line
            #add list containing activity number, start and end times
            #to a set of all activities
            activities.append(new_activity)
        count +=1
        #print("Count:")
        #print(count)
        line = file.readline()