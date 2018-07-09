from subprocess import PIPE,run
from time import time
import sys

# This function may change for optimization problems
def validate(outp, output):
	return outp == output

# Execute tests
def run_tests(testcases, Timeout=None):
	passed = 0
	ttime = 0
	for i, (inp, outp) in enumerate(testcases):
		inp = inp.encode("ascii")
		duration = 0
		try:
			# Execute the program passed via command line args
			start = time()
			output = run(sys.argv[1:], stdout=PIPE, input=inp, timeout=Timeout)
			duration = time() - start
		except TimeoutExpired:
			# Test took longer than Timeout seconds to execute
			print("[FAIL] Test{0} timed out after {1:.4f}sec".format(i, Timeout))
			continue
		output = output.stdout.decode(sys.stdout.encoding)
		ttime += duration
		# Verify correctness of solution
		if validate(outp, output):
			passed += 1
			print("[PASS] Test{0} passed in {1:.4f}sec".format(i, duration))
		else:
			print("[FAIL] Test{0} failed after {1:.4f}sec\n--\nExpected:\n{2}\n--\nActual:\n{3}\n--".format(i, duration, outp, output))

	# Print an overall summary of the execution
	print("\nSummary: {0} out of {1} tests passed over {2:.4f}sec".format(passed, len(testcases), ttime))





if __name__ == "__main__":

	testcases = []
	
	testcases.append(("no", "Would you like to roll the dice? \nMaybe next time!\n"))



	# Ensure the user provided an input
	if not len(sys.argv[1:]):
		print("Please provide a solution program. Example usage:\n  python3 validator.py java JavaSolution")
		sys.exit(0)
	
	# Time in seconds before timing out on a testcase
	Timeout = 3
	
	run_tests(testcases, Timeout)
