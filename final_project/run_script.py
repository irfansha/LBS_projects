# Irfansha Shaik, 22.05.2020, Aarhus
import os
import sys

# Calls symbolic attack on x:
def call_symbolic_attack(rb, k):
	os.system("klee " + "--external-calls=all symbolic_attack.bc " + str(rb) + " " + str(k) + " ./data/run_" + str(rb) + "_" + str(k) + ".txt")

def main(argv):
	rb = int(sys.argv[1])
	max_k = int(sys.argv[2])

	# Looping through each k:
	for k in range(1, max_k+1):
		call_symbolic_attack(rb, k)

if __name__ == "__main__":
   main(sys.argv[1:])
