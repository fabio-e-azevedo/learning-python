""" https://lynn-kwong.medium.com/how-to-debug-python-scripts-and-api-code-in-the-console-and-in-vs-code-a0b825ad7d41 """

import argparse

def echo_func(*args, **kwargs):
    for index, value in enumerate(args):
        print(f"LIST VALUE {index} ===>>> {value}")

    for key, value in kwargs.items():
        print(f"KEY ===>>> {key}, VALUE ===>>> {value}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser("Check the options.")

    parser.add_argument(
        "-n",
        "--numbers",
        dest="numbers",
        metavar="N",
        type=int,
        nargs="*",
        default=[],
        help="The numbers to check.",
    )

    parser.add_argument(
        "-e",
        "--even",
        dest="even",
        action="store_true",
        help="Only check even numbers.",
    )

    parser.add_argument(
        "-l",
        "--level",
        dest="level",
        type=str,
        default="INFO",
        help="The logging level.",
    )

    arguments = parser.parse_args()
    
    echo_func(*arguments.numbers, even=arguments.even, level=arguments.level)
    