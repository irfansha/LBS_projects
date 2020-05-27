# Irfansha Shaik, 27.05.2020, Aarhus
import os
import sys


'''
Now allowing multiple solver choices:
  1: STP
  2: Z3
  3: cex solver
  4: independent-solver
'''
# Calls symbolic attack with optimisation and various solvers:
def call_solver_symbolic_attack(rb, k, heur):
	if (heur == 1):
		solver_option = "-solver-backend=stp"
		dir_name = "stp"
	elif (heur == 2):
		solver_option = "-solver-backend=z3"
		dir_name = "z3"
	elif (heur == 3):
		solver_option = "-use-cex-cache"
		dir_name = "cex"
	elif (heur == 4):
		solver_option = "-use-independent-solver"
		dir_name = "ind"
	os.system("klee " + solver_option + " --optimize -write-no-tests --output-dir=performance_solver_data/solver_run_data_" + dir_name + "_" + str(rb) + "_" + str(k) +  " symbolic_attack.bc " + str(rb) + " " + str(k))

def main(argv):
	rb = int(sys.argv[1])
	max_k = int(sys.argv[2])
	solver = int(sys.argv[3])

	# Looping through each k:
	for k in range(8, max_k+1, 2):
		call_solver_symbolic_attack(rb, k, solver)

if __name__ == "__main__":
   main(sys.argv[1:])
