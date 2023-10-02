0x00 Python Hello World
This project contains a series of Python and Shell scripts designed to help you get familiar with Python programming and basic scripting in Linux. The tasks in this project cover various aspects of Python, from basic print statements to more complex problems like checking for a cycle in a linked list.

Table of Contents
Tasks
Requirements
Usage
Credits
Tasks
0. Run Python file
Write a Shell script that runs a Python script.

1. Run inline
Write a Shell script that runs Python code.

2. Hello, print
Write a Python script that prints a specific string using the print function.

3. Print integer
Complete a Python script to print an integer followed by a string.

4. Print float
Complete a Python script to print a float with two digits of precision.

5. Print string
Complete a Python script to print a string three times and then print its first 9 characters.

6. Play with strings
Complete a Python script to print a specific string.

7. Copy - Cut - Paste
Complete a Python script to manipulate a string.

8. Create a new sentence
Complete a Python script to create a new sentence from two strings.

9. Easter Egg
Write a Python script that prints "The Zen of Python" by Tim Peters.

10. Linked list cycle
Write a C function to check if a singly linked list has a cycle.

11. Hello, write
Write a Python script that prints to stderr and exits with a specific status code.

12. Compile
Write a script to compile a Python script file and generate a bytecode file.

13. ByteCode -> Python #1
Write a Python function that performs the same operations as a given Python bytecode.

Requirements
Python Scripts: You should use Python 3.8.5 and follow specific coding standards mentioned in the task descriptions.
Shell Scripts: Shell scripts should be tested on Ubuntu 20.04 LTS.
C Scripts: C scripts should be compiled on Ubuntu 20.04 LTS using GCC with specific options.
Follow specific instructions mentioned in each task description for script execution and file naming.
Usage
To execute the Python scripts, use the following format:

bash
Copy code
./script_name.py
For example, to run "2-print.py," you would use:

bash
Copy code
./2-print.py
To compile a Python script as mentioned in task 12, use:

bash
Copy code
./101-compile
For the C script "10-check_cycle.c," a sample usage is provided in "10-main.c." Compile and run it using:

bash
Copy code
gcc -Wall -Werror -Wextra -pedantic -std=gnu89 10-main.c 10-check_cycle.c 10-linked_lists.c -o cycle
./cycle
Credits
This project is part of the ALX Higher Level Programming curriculum and was created by Guillaume, with tasks inspired by real-world scenarios and challenges in Python programming.
