"""
COP4533 Algorithm Abstraction & Design Programming Assignment 3
Highest Value Longest Common Sequence

Main program main.py

Alejandro Velez & Marco Fernandez
"""
import sys


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
                character, value = map(int, line.split())
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


def main():
    # Input handling
    filename = input("Type the name of the txt file to use as input\n")
    character_values, a, b = read_input_file(filename)


if __name__ == '__main__':
    main()
