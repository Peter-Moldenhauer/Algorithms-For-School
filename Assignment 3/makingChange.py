############################################################################################
# Name: Peter Moldenhauer
# Class: CS 325-400
# Date: 10/11/17
# Description: This program implements the "making change" algorithm.
# It reads in input data from amount.txt and outputs data to change.txt
#
# Note: To complete this implementation of this algorithm, I used the following resource:
# https://www.youtube.com/watch?v=NJuKJ8sasGk
#############################################################################################

# used to get programs execution time
import time
startTime = time.time()

# MakingChange algorithm
def MakingChange(V, A):
    # array of size 0 - A to hold how many coins are needed per element
    # to start, initialize each element to infinity
    T = [float('Inf')]*(A+1)
    # array of size 0 - A to hold the last coin used on the corresponding T element
    # to start, initialize each element to -1
    R = [-1] * (A + 1)
    # array of length V to hold total amount of each coin used
    C = [0] * len(V)
    # initialize first element of T, with a value of 0, 0 coins are needed
    T[0] = 0

    # loops through the array of coins and makes change if possible
    for j in range(len(V)):
        for i in range(1, A+1):
            # if the number for change to be made for is greater than the selected coin value
            if i >= V[j]:
                # if the newly selected coin value plus 1 is less than the current coin value
                if (T[i-V[j]] + 1) < T[i]:
                    T[i] = 1 + T[i-V[j]]
                    R[i] = j

    # count how many coins were used per element
    while A != 0:
        C[R[A]] += 1
        A = A - V[R[A]]

    # return the array of total amount of each coin used
    return C

# open the input file
input_file = open('amount.txt', 'r')

# create the output file
output_file = open('change.txt', 'w')

# convert the string to a array of characters, trim off whitespace first!
V = input_file.readline().strip()
V = V.split(' ')
# get the next line to get the amount A, trim off whitespace first!
A = input_file.readline().strip()

while V != [''] and A != ['']:
    # convert V to an array of integers
    V = map(int, V)
    # convert the string A to an int
    A = int(A)

    # call the MakingChange algorithm
    change = MakingChange(V, A)
    # total number of coins
    totalCoins = sum(change)

    # output the results to the output file, format described in HW3 description
    output_file.write(' '.join(map(str, V)))
    output_file.write('\n')
    output_file.write(str(A))
    output_file.write('\n')
    output_file.write(' '.join(map(str,change)))
    output_file.write('\n')
    output_file.write(str(totalCoins))
    output_file.write('\n')

    # convert the string to a array of characters
    V = input_file.readline().split(' ')
    # get the next line
    A = input_file.readline()

# close the files
input_file.close()
output_file.close()

# print the programs execution time
print("--- %s seconds ---" % (time.time() - startTime))