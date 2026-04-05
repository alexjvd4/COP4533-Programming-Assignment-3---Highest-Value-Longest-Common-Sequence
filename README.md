COP4533 Programming Assignment 3
Highest Value Longest Common Subsequence

Marco Fernandez
Alejandro Velez

----------------------------------------

How to Run:
python main.py

The program automatically reads from:
input.txt

It outputs results to:
output.txt

----------------------------------------

Example Input (input.txt):
3
a 2
b 4
c 5
aacb
caab

Example Output (output.txt):
9
cb

----------------------------------------------------------------------------

Question 1:
We tested the algorithm using multiple input files where both strings had lengths of at least 25 characters. As expected, the runtime increased as the size of the input strings increased. This is because the algorithm uses a dynamic programming table that compares every character in string A with every character in string B.
From our observations, the runtime growth follows an O(n*m) pattern, where n and m are the lengths of the two strings. When plotted on a graph, the runtime increases steadily and predictably as input size grows, confirming the expected time complexity behavior of the algorithm.
----------------------------------------------------------------------------

Question 2:
Let DP[i][j] represent the maximum value of a common subsequence
between the first i characters of A and the first j characters of B.

Base cases:
DP[0][j] = 0
DP[i][0] = 0

If A[i-1] == B[j-1]:
DP[i][j] = DP[i-1][j-1] + value(A[i-1])

Else:
DP[i][j] = max(DP[i-1][j], DP[i][j-1])

----------------------------------------

Question 3:
Pseudocode:

for i = 0 to n:
    for j = 0 to m:
        if i == 0 or j == 0:
            DP[i][j] = 0
        else if A[i-1] == B[j-1]:
            DP[i][j] = DP[i-1][j-1] + value(A[i-1])
        else:
            DP[i][j] = max(DP[i-1][j], DP[i][j-1])

Time Complexity: O(n * m)