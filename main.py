"""
COP4533 Algorithm Abstraction & Design Programming Assignment 3
Highest Value Longest Common Sequence

Main program main.py

Alejandro Velez & Marco Fernandez
"""
import sys
import time
import matplotlib.pyplot as plt


def read_input_file(filename):
    """
    Obtains all possible characters, their values, and the two strings being compared
    :param filename: An input filename string
    :return: Character-value dict, string A, string B
    """
    character_values = {}
    with open(filename, "r") as f:
        line = f.readline().strip()
        if line != '':
            num_characters = int(line)
        else:
            print("ERROR: Empty input file.")
            sys.exit(0)
        for i in range(num_characters):
            line = f.readline().strip()
            if line != '':
                character, value = line.split()
                value = int(value)
                character_values[character] = value
            else:
                print("ERROR: Not enough characters provided.")
                sys.exit(0)
        line = f.readline().strip()
        if line != '':
            a = line
        else:
            print("ERROR: String A not provided.")
            sys.exit(0)
        line = f.readline().strip()
        if line != '':
            b = line
        else:
            print("ERROR: String B not provided.")
            sys.exit(0)

    return character_values, a, b


def max_val_substring(character_values, a, b):
    """
    Computes the maximum value substring
    :param character_values: character value dict
    :param a: substring a
    :param b: substring b
    :return: Maximum value substring
    """
    n = len(a)
    m = len(b)

    memory = [[0] * (m + 1) for _ in range(n + 1)]

    # Fill Memory 2d array
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                memory[i][j] = memory[i - 1][j - 1] + character_values[a[i - 1]]
            else:
                memory[i][j] = max(memory[i - 1][j], memory[i][j - 1])

    # Backtracking to obtain substring
    i, j = n, m
    result = []
    while i > 0 and j > 0:
        if a[i - 1] == b[j - 1]:
            result.append(a[i - 1])
            i -= 1
            j -= 1
        elif memory[i - 1][j] > memory[i][j - 1]:
            i -= 1
        else:
            j -= 1

    result.reverse()

    return memory[n][m], "".join(result)

# output function 
def write_output(value, subsequence):
    with open("output.txt", "w") as f:
        f.write(str(value) + "\n")
        f.write(subsequence + "\n")


def main():
    # Input handling
    filename = input("Type the name of the txt file to use as input\n")
    character_values, a, b = read_input_file(filename)

    # Runtime clock
    start = time.perf_counter()
    value, substring = max_val_substring(character_values, a, b)
    end = time.perf_counter()

    runtime_ms = (end - start) * 1000

    # Output handling
    print(value)
    print(substring)

    write_output(value, substring)

    print("\nRuntime (ms):", runtime_ms)

    # Question 1 Graph Calculation (for only input1.txt ... input10.txt)

    # len(string a) * len(string b)
    nm = [625, 900, 1225, 1600, 2025, 2500, 3600, 4900, 6400, 8100]
    # Corresponding runtimes
    T = [0.2716000000000385, 0.3689000000002274, 0.6675999999998794, 0.726199999999011, 0.811200000000234, 0.8929000000001963, 1.5366999999999464, 1.6791999999998808, 1.3974999999994964, 2.933199999999747]  # replace with your times

    plt.scatter(nm, T, label="Measured runtime")
    plt.plot(nm, T, linestyle='--', alpha=0.5)

    plt.xlabel("n * m (problem size)")
    plt.ylabel("Runtime (ms)")
    plt.title("Runtime vs n*m for common subsequence DP")
    plt.grid(True)
    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()
