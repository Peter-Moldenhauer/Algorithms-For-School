############################################################################################
# Name: Peter Moldenhauer
# Class: CS 325-400
# Date: 9/25/17
# Description: This program implements the merge sort algorithm.
# It reads in input data from data.txt and outputs data to merge.out
#
# Note: To complete this implementation of the merge sort algorithm,
# I used the following resources:
# 1) The "using induction to prove the correctness of algorithms" class lecture video
# 2) The website: https://rosettacode.org/wiki/Sorting_algorithms/Merge_sort
# 3) The website: https://teamtreehouse.com/community/merge-sort-in-python
#############################################################################################

# used to get programs execution time
import time
startTime = time.time()

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
        if firstHalf[0] < secondHalf[0]:
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

# open input file and create output file
input_file = open('data.txt', 'r')
output_file = open('merge.out', 'w')

# convert the string from input file to an array of characters
arrayIn = input_file.readline().split(' ')

# loop through the array, sort it and get another array to sort (if applicable)
while arrayIn != ['']:
    # convert array of character to array of integers
    arrayIn = map(int, arrayIn)

    # discard the first number, first number is array length (for C++ users)
    arrayIn = arrayIn[1:]

    # call mergesort function to sort the array
    arrayOut = mergesort(arrayIn)

    # output the sorted array to the output file
    output_file.write(' '.join(map(str, arrayOut)))
    output_file.write('\n')

    # get the next array in data.txt (if applicable)
    arrayIn = input_file.readline().split(' ')

# close the files
input_file.close()
output_file.close()

# print the programs execution time
print("--- %s seconds ---" % (time.time() - startTime))
