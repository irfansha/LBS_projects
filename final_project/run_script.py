# Irfansha Shaik, 22.05.2020, Aarhus
import os
import sys

# Calls symbolic attack on x:
def call_symbolic_attack(rb, k):
	os.system("klee " + "--external-calls=all --output-dir=data/run_data_" + str(rb) + "_" + str(k) + " symbolic_attack.bc " + str(rb) + " " + str(k) + " ./data/run_" + str(rb) + "_" + str(k) + ".txt")

# Calls symbolic attack on x with optimisation and random state heuristics:
def call_opt_rs_symbolic_attack(rb, k):
	os.system("klee " + "--external-calls=all --search=random-state --optimize --output-dir=data/run_data_opt_rs_" + str(rb) + "_" + str(k) + " symbolic_attack.bc " + str(rb) + " " + str(k) + " ./data/run_opt_rs_" + str(rb) + "_" + str(k) + ".txt")

def main(argv):
	rb = int(sys.argv[1])
	max_k = int(sys.argv[2])
	choice = sys.argv[3]

	if choice == "opt-rs":
		# Looping through each k:
		for k in range(1, max_k+1):
			call_opt_rs_symbolic_attack(rb, k)
	else:
		# Looping through each k:
		for k in range(1, max_k+1):
			call_symbolic_attack(rb, k)

if __name__ == "__main__":
   main(sys.argv[1:])
