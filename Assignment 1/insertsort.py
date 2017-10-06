############################################################################################
# Name: Peter Moldenhauer
# Class: CS 325-400
# Date: 9/25/17
# Description: This program implements the insertion sort algorithm.
# It reads in input data from data.txt and outputs data to insert.out
#
# Note: To complete this implementation of the insertion sort algorithm,
# I used the following resources:
# 1) The "Analysis of Sorting" class lecture video
# 2) The website: https://en.wikipedia.org/wiki/Insertion_sort
#############################################################################################

# used to get programs execution time
import time
startTime = time.time()

# insertionSort function
def insertSort(theArray):
    # since the 1st element is already sorted, start looping at 2nd element to the last element
    for i in range(1, len(theArray)):
        # key is the next item to be inserted into the leading sorted section of the array
        key = theArray[i]
        # lastItem is the last item to compare to
        lastItem = i - 1
        while lastItem >= 0 and theArray[lastItem] > key:
            theArray[lastItem + 1] = theArray[lastItem]
            lastItem = lastItem - 1
        theArray[lastItem + 1] = key
    return theArray

# open the input file and create the output file
input_file = open('data.txt', 'r')
output_file = open('insert.out', 'w')

# convert the string from input file to an array of characters
arrayIn = input_file.readline().split(' ')

# loop through the array, sort it and get another array to sort (if applicable)
while arrayIn != ['']:
    # convert array of characters to an array of of integers
    arrayIn = map(int, arrayIn)

    # discard the first number, first number is array length (for C++ users)
    arrayIn = arrayIn[1:]

    # sort the array with insertSort
    sortedArray = insertSort(arrayIn)

    # output the sorted array to the output file
    output_file.write(' '.join(map(str, sortedArray)))
    output_file.write('\n')

    # get the next array in data.txt (if applicable)
    arrayIn = input_file.readline().split(' ')

# close both of the files
input_file.close()
output_file.close()

# print the programs execution time
print("--- %s seconds ---" % (time.time() - startTime))