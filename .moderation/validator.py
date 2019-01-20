from __future__ import print_function
from subprocess import PIPE, run, TimeoutExpired
from time import time
from argparse import ArgumentParser
import sys
import os

version = (0, 0, 2)

# This function parses one section of a test case,
# from "xxxx_lines: N" to the Nth line after
def parse_lines(lines, section, test_num):
    try:
        # Skip any empty lines (between sections) or lines that start with '#'
        while not lines[0] or lines[0].startswith("#"):
            lines = lines[1:]
        num = int(lines[0].lower().split(section+"_lines:")[1])
        lines = lines[1:]
        return "\n".join(lines[:num]), lines[num:]
    except:
        print("{}: error: Parsing error on test case {}. Expected \"{}_lines:\" followed by an integer, but received \"{}\".".format(sys.argv[0], test_num, section, lines[0] if lines else ""))
        raise

# This function reads all the test cases out of the text,
# returning a list of (input,ouput) tuples, or an empty list
# in the case of a parsing error
def parse_tests(text):
    lines = text.rstrip("\n").splitlines()
    test_cases = []
    # Parse individual tests from the text, one by one
    while any(lines):
        try:
            test_input, lines = parse_lines(lines, "input", len(test_cases))
            test_output, lines = parse_lines(lines, "output", len(test_cases))
            test_cases.append((test_input, test_output))
        except Exception as e:
            print(e)
            return list()
    return test_cases

# Spawn a new process to execute {command}, piping in {test_input}
# Return the results after the process terminates
def execute_test(test_input, command, timeout):
    test_input = test_input.encode("ascii")
    run_output = run(command, stdout=PIPE, input=test_input, timeout=timeout)
    return run_output.stdout.decode(sys.stdout.encoding).replace(os.linesep, "\n").rstrip("\n")

# This function is responsible for recording and displaying the
# results of each test case as they are executed
def run_tests(test_cases, command, timeout):
    passed_tests = 0
    start_time = time()
    for i, (test_input, test_output) in enumerate(test_cases):
        try:
            run_output = execute_test(test_input, command, timeout)
            if run_output == test_output:
                passed_tests += 1
                print("[PASS] Test {0} passed.".format(i))
            else:
                print("[FAIL] Test {0} failed.\n-- Expected --\n{1}\n-- Received --\n{2}\n---- End -----".format(i, test_output, run_output))
        except TimeoutExpired:
            print("[FAIL] Test {0} timed out after {1} seconds.".format(i, timeout))

    # Print an overall summary of the execution
    print("\nSummary: {0} out of {1} tests passed over {2:.3f}sec".format(passed_tests, len(test_cases), time() - start_time))

# Parse the command line options, return the result
def parse_options():
    parser = ArgumentParser()
    parser.add_argument('-t', metavar="TIMEOUT", dest="timeout", type=int, default=60, help="Abort test case after <TIMEOUT> seconds")
    parser.add_argument('-v', action="store_true", dest="version", help="Print the version number")
    parser.add_argument('-f', metavar="FILENAME", dest="filename", type=str, default=None, help="Name of the test cases file")
    parser.add_argument('command', help="Shell command to run the solver program") 
    parser.add_argument('args', nargs="*", help="Arguments supplied to solver program")
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_options()
    
    if args.version:
        print("Version: {0}".format(".".join(map(str, version))))
        sys.exit(0)

    try:
        with open(args.filename, "r") if args.filename else sys.stdin as tests_file:
            test_cases = parse_tests(tests_file.read())
            if test_cases:
                run_tests(test_cases, [args.command] + args.args, args.timeout)
    except FileNotFoundError:
        print("{}: error: no such file '{}'".format(sys.argv[0], args.filename))
