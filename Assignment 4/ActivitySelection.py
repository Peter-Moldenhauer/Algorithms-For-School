############################################################################################
# Name: Peter Moldenhauer
# Class: CS 325-400
# Date: 10/18/17
# Description: This program implements the last-to-start activity selection greedy algorithm
# It reads in input data from act.txt and then outputs the results to the terminal.
#############################################################################################

# mergeSort function
def mergesort(theArray):
    # if the array has only one element just return the array
    if len(theArray) == 1:
        return theArray
    # otherwise recursively call mergeSort on both parts of theArray
    else:
        # get the midpoint of theArray
        midpoint = len(theArray)/2
        firstHalf = mergesort(theArray[:midpoint])
        secondHalf = mergesort(theArray[midpoint:])
        return merge(firstHalf, secondHalf)

# merge helper function for mergeSort
def merge(firstHalf, secondHalf):
    # empty array to hold sorted values
    sortedArray = []
    # add to sortedArray until either firstHalf or secondHalf of the array is empty
    while len(firstHalf) != 0 and len(secondHalf) != 0:
        if firstHalf[0][1] > secondHalf[0][1]:
            sortedArray.append(firstHalf[0])
            firstHalf.remove(firstHalf[0])
        else:
            sortedArray.append(secondHalf[0])
            secondHalf.remove(secondHalf[0])
    # add the remaining value to sortedArray
    if len(firstHalf) == 0:
        sortedArray += secondHalf
    else:
        sortedArray += firstHalf
    return sortedArray

# create schedule of activities based on last activity to start
def scheduleActivities(activities):
    n = len(activities)
    schedule = [activities[0]]
    k = 0
    for m in range(1, n):
        if activities[m][2] <= schedule[k][1]:
            schedule.append(activities[m])
            k += 1
    return schedule

# open the input file
input_file = open('act.txt','r')

# variable to keep track of the number sets
setCount = 0

while True:
    # read a line from the input file
    line = input_file.readline()
    line = line.strip()
    line = line.split(' ')
    # break out of loop if the end of input file is reached
    if line == ['']:
        break
    # convert the line into integers
    line = map(int, line)
    if len(line) == 1:
        # keep track of what number set it is
        setCount += 1
        # counter variable is used to determine how long to loop for to get all of the nums in the set
        counter = line[0]
        # list to hold the activities to run the algorithm on
        activities = []
    for i in range(0, counter):
        # build up the list of activities
        line = input_file.readline()
        line = line.strip()
        line = line.split(' ')
        line = map(int, line)
        activity = [line[0], line[1], line[2]]
        activities.append(activity)
    # sort the activities for this set of numbers
    sortedActivities = mergesort(activities)
    # schedule the activities for this set of numbers
    schedule = scheduleActivities(sortedActivities)
    # output the results to terminal for this set of numbers
    print "Set", setCount
    print "Number of activities selected =", len(schedule)
    a = "Activities:"
    for i in reversed(range(0, len(schedule))):
        a = a + " " + str(schedule[i][0])
    print a
    print "\n"

input_file.close()