############################################################################################
# Name: Peter Moldenhauer
# Class: CS 325-400
# Date: 10/4/17
# Description: This program implements the stooge sort algorithm.
# It reads in input data from data.txt and outputs data to stooge.out
#
# I used the following the website as a resource: https://en.wikipedia.org/wiki/Stooge_sort
#############################################################################################

# used to get programs execution time
import time
startTime = time.time()

# stoogeSort function
def stoogeSort(theArray, i, j):
    if theArray[j] < theArray[i]:
        theArray[i], theArray[j] = theArray[j], theArray[i]
    if (j - i + 1) > 2:
        m = (j - i + 1) / 3
        stoogeSort(theArray, i, j-m)
        stoogeSort(theArray, i+m, j)
        stoogeSort(theArray, i, j-m)
    return theArray

# open input file and create output file
input_file = open('data.txt', 'r')
output_file = open('stooge.out', 'w')

# convert the string from input file to an array of characters
arrayIn = input_file.readline().split(' ')

# loop through the array, sort it and get another array to sort (if applicable)
while arrayIn != ['']:
    # convert array of character to array of integers
    arrayIn = map(int, arrayIn)

    # discard the first number, first number is array length (for C++ users)
    arrayIn = arrayIn[1:]

    # call mergesort function to sort the array
    arrayOut = stoogeSort(arrayIn, 0, len(arrayIn) - 1)

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
