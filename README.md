# COP4533-Programming-Assignment-3---Highest-Value-Longest-Common-Sequence

Implements a dynamic programming solution to compute the Highest Value Longest Common Subsequence (HVLCS) between two strings. The program calculates the maximum possible value of a common subsequence based on assigned character weights and reconstructs one optimal subsequence.

Authors:

Alejandro Velez 28126838

Marco Fernandez 96258471

Instructions:

 - Run `git clone https://github.com/alexjvd4/COP4533-Programming-Assignment-3---Highest-Value-Longest-Common-Sequence.git` in your preferred directory

   HVLCS Algorithm Instructions:
    - Sample input .txt files are provided such as `input.txt`, `empty.txt`, `one_string_empty.txt`, `no_subsequence.txt`, `multi_answer.txt`
        - Add any input .txt files you would like in the main folder `\COP4533-Programming-Assignment-3---Highest-Value-Longest-Common-Sequence`
    - Run `python main.py`
    - The program will ask the user to type the name of the preffered input file such as `input.txt`
    - The `output.txt` file will be generated in the same folder `\COP4533-Programming-Assignment-3---Highest-Value-Longest-Common-Sequence` containing the maximum value and corresponding subsequence
    - The runtime of the current input will also be printed to the console. Utilizing the `matplotlib` library, the graph for the first written question will also be generated which utilizes input1.txt through input10.txt, not what was currently inputted.

----------------------------------------

Example Input (`input.txt`):

3

a 2 

b 4

c 5

aacb

caab

Example Output (`output.txt`):

9 

cb

----------------------------------------

Written Component Questions:

QUESTION 1:

We tested the algorithm using multiple input files where both strings had lengths of at least 25 characters. As expected, the runtime increased as the size of the input strings increased. This is because the algorithm uses a dynamic programming table that compares every character in string A with every character in string B.

From our observations, the runtime growth follows an O(n*m) pattern, where n and m are the lengths of the two strings. When plotted on a graph, the runtime increases steadily and predictably as input size grows, confirming the expected time complexity behavior of the algorithm.

<img width="2880" height="1872" alt="image" src="https://github.com/user-attachments/assets/6e1ca9b6-4452-48a5-91b4-aca726c28d6d" />


----------------------------------------

QUESTION 2:

Let OPT[i][j] represent the maximum value of a common subsequence between the first i characters of string A and the first j characters of string B.

Base cases:
OPT[0][j] = 0  
OPT[i][0] = 0  

If A[i-1] == B[j-1]:  
OPT[i][j] = OPT[i-1][j-1] + value(A[i-1])  

Else:  
OPT[i][j] = max(OPT[i-1][j], OPT[i][j-1])  

This works because each subproblem builds on previously computed optimal solutions, ensuring that the final result is the highest possible value subsequence.

----------------------------------------

QUESTION 3:

Pseudocode:

```txt
for i = 0 to n:
    M[i][0] = 0
for j = 0 to m:
    M[0][j] = 0
for i = 0 to n:
    for j = 0 to m:
        if i == 0 or j == 0:
            M[i][j] = 0
        else if A[i-1] == B[j-1]:
            M[i][j] = M[i-1][j-1] + value(A[i-1])
        else:
            M[i][j] = max(M[i-1][j], M[i][j-1])

Time Complexity: O(n * m)
