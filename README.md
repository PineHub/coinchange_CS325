This file provides two algorithms investigating the coin change problem.

The first algorithm is a greedy demonstration which takes the highest denomination, floor-divides the total change value by it, then saves that solution.  The new total change value is the old target value, less the product of the old target value divided by the highest denomination and the highest denomination.

The second is a dynamic programming algorithm based on the equation:
T[v]=  T[v]=   min┬(V[i}≤v)⁡ {T[v-V[i]]+1}
It incrementally builds a look up table of the smallest number of coins for a value and their associated coins.

To run the program, from the command line: `change.py your_input_file.txt your_output_file.txt`.

Example files are included in this repo- change1.txt and change2.txt. The changeout.txt file gives an example how your output will look.  Note the formatting in change1.txt and change2.txt- numbers on the first line are separated by spaces, the next line should be the target change amount you want.

>change2.txt:
>1 2 4 8
>15
>1 3 7 12
>29
>1 5 9 16 18 27 33 55
>1357
>1 7 33 45 66 67
>3255

>changeout.txt:
>1 2 4 8
>Greedy Algorithm: 15
>1  1  1  1
>4
>Dynamic Programming Algorithm: 15
>1  1  1  1
>4

>1 3 7 12
>Greedy Algorithm: 29
>2  1  0  2
>5
>Dynamic Programming Algorithm: 29
>0  1  2  1
>4

>1 5 9 16 18 27 33 55
>Greedy Algorithm: 1357
>4  0  0  0  0  0  1  24
>29
>Dynamic Programming Algorithm: 1357
>1  0  1  0  0  1  0  24
>27

>1 7 33 45 66 67
>Greedy Algorithm: 3255
>6  0  1  0  0  48
>55
>Dynamic Programming Algorithm: 3255
>0  0  0  1  6  42
>49




