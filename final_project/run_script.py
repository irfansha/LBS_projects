# Irfansha Shaik, 22.05.2020, Aarhus
import os
import sys

def clean_up(integer_list, rb, k):
	completed_list = []
	# looping through each active integer and checking if "error" found:
	for x in integer_list:
		f = open("./data/run_" + str(x) + "_" + str(rb) + "_" + str(k) + "/messages.txt","r")
		lines = f.readlines()
		for line in lines:
			if "ASSERTION FAIL: 0" in line:
				completed_list.append(x)
				break
	# Now collecting remaining intergers to be explored:
	remaining_list = []
	for x in integer_list:
		if x not in completed_list:
			remaining_list.append(x)
	return remaining_list

# Calls symbolic attack on x:
def call_symbolic_attack(x, rb, k):
	os.system("klee -exit-on-error-type=Assert --output-dir=data/run_" + str(x) + "_" + str(rb) + "_" + str(k) + " symbolic_attack.bc " + str(x) + " " + str(rb) + " " + str(k))

def main(argv):
	rb = int(sys.argv[1])
	max_k = int(sys.argv[2])
	integer_list = []
	# Initially contains all the numbers:
	for i in range(1, rb + 1):
		integer_list.append(i)
	# Looping through each k until an "error" is raised:
	for k in range(1, max_k+1):
		if len(integer_list) == 0:
			break
		else:
			# Looping for each active integer that to be "found":
			for x in integer_list:
				call_symbolic_attack(x, rb, k)
			# call clean up:
			integer_list = clean_up(integer_list, rb, k)

if __name__ == "__main__":
   main(sys.argv[1:])
