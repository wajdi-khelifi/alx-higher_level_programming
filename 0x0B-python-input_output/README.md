# 0x0B. Python - Input/Output

## Description

This project is part of the Holberton School curriculum and focuses on Python input/output operations. It covers reading and writing files, working with JSON data, and creating, loading, and saving objects.

## Project Details

- **Author**: Guillaume
- **Weight**: 1
- **Project Start Date**: Nov 7, 2023 4:00 AM
- **Project End Date**: Nov 8, 2023 4:00 AM
- **Checker Release Date**: Nov 7, 2023 10:00 AM
- **Auto Review Deadline**: The auto review will be launched at the deadline.

## Resources

- [7.2. Reading and Writing Files](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
- [8.7. Predefined Clean-up Actions](https://docs.python.org/3/tutorial/errors.html#predefined-clean-up-actions)
- [Dive Into Python 3: Chapter 11. Files](https://diveinto.org/python3/files.html) (until "11.4 Binary Files" (included))
- [JSON encoder and decoder](https://docs.python.org/3/library/json.html)
- [Learn to Program 8: Reading / Writing Files](https://www.learnpython.org/en/File_I/O)
- [Automate the Boring Stuff with Python (ch. 8 p 180-183 and ch. 14 p 326-333)](https://automatetheboringstuff.com/2e/chapter8/)
- [All about py-file I/O](https://docs.python.org/3/library/io.html)
  
## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General
- Why Python programming is awesome
- How to open a file
- How to write text in a file
- How to read the full content of a file
- How to read a file line by line
- How to move the cursor in a file
- How to make sure a file is closed after using it
- What is and how to use the with statement
- What is JSON
- What is serialization
- What is deserialization
- How to convert a Python data structure to a JSON string
- How to convert a JSON string to a Python data structure

## Copyright - Plagiarism

You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives. You will not be able to meet the objectives of this or any following project by copying and pasting someone else's work. You are not allowed to publish any content of this project. Any form of plagiarism is strictly forbidden and will result in removal from the program.

## Requirements

### Python Scripts

- **Allowed Editors**: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use pycodestyle (version 2.8.*)
- All your files must be executable
- The length of your files will be tested using `wc`

### Python Test Cases

- **Allowed Editors**: vi, vim, emacs
- All your files should end with a new line
- All your test files should be inside a folder `tests`
- All your test files should be text files (extension: .txt)
- All your tests should be executed by using this command: `python3 -m doctest ./tests/*`
- All your modules should have documentation (python3 -c 'print(__import__("my_module").__doc__)')
- All your classes should have documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
- All your functions (inside and outside a class) should have documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
- A documentation is not a simple word, it's a real sentence explaining what's the purpose of the module, class or method (the length of it will be verified)
- We strongly encourage you to work together on test cases, so that you don't miss any edge case

## Tasks

1. [Read file](./0-read_file.py)
2. [Write to a file](./1-write_file.py)
3. [Append to a file](./2-append_write.py)
4. [To JSON string](./3-to_json_string.py)
5. [From JSON string to Object](./4-from_json_string.py)
6. [Save Object to a file](./5-save_to_json_file.py)
7. [Create object from a JSON file](./6-load_from_json_file.py)
8. [Load, add, save](./7-add_item.py)
9. [Class to JSON](./8-class_to_json.py)
10. [Student to JSON](./9-student.py)
11. [Student to JSON with filter](./10-student.py)
12. [Student to disk and reload](./11-student.py)
13. [Pascal's Triangle](./12-pascal_triangle.py)
14. [Search and update](./100-append_after.py)
15. [Log parsing](./101-stats.py)

## Author
- Author: Wajdi Khelifi
- Email: khelifi.wajdi@hotmail.com
- GitHub: [https://github.com/wajdi-khelifi]

### Additional Information
- Ensure your code follows PEP 8 style guidelines.
- Include appropriate documentation (docstrings) for classes and methods.
- Plagiarism is strictly forbidden and will result in removal from the program.
