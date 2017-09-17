#Clarence Pine
#CS325
#4/29/17
#Project2

#!/usr/bin/env python
from __future__ import print_function
from __future__ import print_function
import sys


myArray = [1, 2, 6, 12, 24, 48, 60]
myTotalVal = 50

def changegreedy(V, A):
    """ Greedy Solution to the to finding min number of coins needed to make change.  Take the highest denomination, floor
            divide target value by it, save it in solution.  New target value is the old target value, less the product of
            the old target value divided by the highest denomination and the highest denomination.
            @param  {array} V   - Values to choose from
            @param  {int}   A   - Amount of change to make
            @return {array} solutionArray   - Number of coins needed for values of V
            @return {int}   sum   - Minimum number of coins needed
    """

    solutionArray = []
    newTarget = A
    maxIndex = len(V)
    sum = 0


    for i in range(maxIndex-1, -1, -1):

        solutionArray.append(A // V[i])
        sum += A // V[i]


        A = A - (A // V[i]) * V[i]
        newTarget = newTarget % V[i]

    return list(reversed(solutionArray)), sum




def change_dp(V, A):
    """ Dynamic Programing solution to finding min number of coins needed to make change.
        Builds a look up table of smallest number of coins and their associated coins.
        @param  {array} V   - Values to choose from
        @param  {int}   A   - Amount of change to make
        @return {array} C   - Number of coins needed for values of V
        @return {int}   m   - Minimum number of coins needed
    """

    T = [] # min number of coins total coins required
    T.append(0)
    C = [[0 for x in range(len(V))] for y in range(A+1)] # total change amount j; total # of coins of type i

    for j in range(1, A+1):  # A+1 because T[0] already present
        i=0
        jMin = float("inf")  # current min # of coins for the j.  initialized to infinity
        while i < len(V) and (j - V[i] >= 0):
            innerCj = j - V[i]              # will be finding minimum of T[v-V[i]] iterating through different change denominations
            if T[innerCj] + 1 < jMin:       # lookup in table a minimum of T[v-V[i]], add a coin V[i]
                jMin = T[innerCj] + 1       # save this as a local minimum
                C[j] = C[innerCj][:]        # copy the change combination to our table for looking up later
                C[j][i] += 1                # also add the additional coin we had to add
            i += 1                          # try more T[i]'s
        T.append(jMin)                      # Save this as our minimum for the amount of change j

    return C[j], T[j]


def fromFile(inputFname, outputFname):
    """ This reads and parses the input file and outputs it to the output file
            @param  {string} inputFname  - input filename of choice
            @param  {string} outputFname - output filename of choice
            @return None
        """
    evenCounter = 0

    with open(inputFname) as f:
        for line in f:
            if evenCounter == 1:   # if we are on the even line of the file
                changeTarget = int(line)  # read the amount of change to make
                evenCounter -= 1
                outFile = open(outputFname, "a")  # append only to the file
                outFile.write(str(changeTarget))
                outFile.write("\n")
                returnedArray = changegreedy(integerArray, changeTarget)  # function call for greedy
                coinCounts = str(returnedArray[0])
                coinCounts = coinCounts.replace(",", " ")
                coinCounts = coinCounts[1:]
                coinCounts = coinCounts[:-1]
                amountChange = str(returnedArray[1])
                amountChange = amountChange.replace(",", " ")  # format to spaces instead of commas to match input file
                outFile.write(str(coinCounts))
                outFile.write("\n")
                outFile.write(str(amountChange))
                outFile.write("\n")
                outFile.write("Dynamic Programming Algorithm: ")
                outFile.write(str(changeTarget))
                outFile.write("\n")
                returnedArray = change_dp(integerArray, changeTarget)  # function call for dynamic
                coinCounts = str(returnedArray[0])
                coinCounts = coinCounts.replace(",", " ")
                coinCounts = coinCounts[1:]
                coinCounts = coinCounts[:-1]
                amountChange = str(returnedArray[1])
                amountChange = amountChange.replace(",", " ")
                outFile.write(str(coinCounts))
                outFile.write("\n")
                outFile.write(str(amountChange))
                outFile.write("\n\n")
                continue
            outFile = open(outputFname, "a")
            outFile.write(line)
            outFile.write("Greedy Algorithm: ")
            fileArray = line.split()
            integerArray = []
            for i in fileArray:   # reading file line and turning it into an integer array
                integerArray.append(int(i))
            evenCounter += 1





def main():
    fromFile(sys.argv[1], sys.argv[2])


if __name__ == '__main__':
    main()

