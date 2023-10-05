#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    def print_arguments():
        num_args = len(sys.argv) - 1

        if num_args == 0:
            print("Number of argument(s): 0.")
            print(".")
        elif num_args == 1:
            print("Number of argument: 1.")
            print("1:", sys.argv[1])
        else:
            print(f"Number of argument(s): {num_args}.")
            for i in range(1, num_args + 1):
                print(f"{i}:" sys.argv[i])
