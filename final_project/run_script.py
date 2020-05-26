# Irfansha Shaik, 22.05.2020, Aarhus
import os
import sys

# Calls symbolic attack on x:
def call_symbolic_attack(rb, k):
	os.system("klee " + "--external-calls=all --only-output-states-covering-new --output-dir=data_new/run_data_" + str(rb) + "_" + str(k) + " explicit_symbolic_attack.bc " + str(rb) + " " + str(k) + " ./data_new/run_" + str(rb) + "_" + str(k) + ".txt")

'''
Now allowing multiple heuristic choices
  1: dfs - use Depth First Search (DFS)
  2: random-state - randomly select a state to explore
  3: random-path - use Random Path Selection (see OSDI'08 paper)
  4: nurs:covnew - use Non Uniform Random Search (NURS) with Coverage-New heuristic
  5: nurs:md2u - use NURS with Min-Dist-to-Uncovered heuristic
  6: nurs:depth - use NURS with 2^depth heuristic
  7: nurs:icnt - use NURS with Instr-Count heuristic
  8: nurs:cpicnt - use NURS with CallPath-Instr-Count heuristic
  9: nurs:qc- use NURS with Query-Cost heuristic
  10: All heuristics interleaved
'''
# Calls symbolic attack on x with optimisation and random state heuristics:
def call_heu_symbolic_attack(rb, k, heur):
	if (heur == 1):
		heur_option = "--search=dfs"
		dir_name = "dfs"
	elif (heur == 2):
		heur_option = "--search=random-state"
		dir_name = "rs"
	elif (heur == 3):
		heur_option = "--search=random-path"
		dir_name = "rp"
	elif (heur == 4):
		heur_option = "--search=nurs:covnew"
		dir_name = "covnew"
	elif (heur == 5):
		heur_option = "--search=nurs:md2u"
		dir_name = "md2u"
	elif (heur == 6):
		heur_option = "--search=nurs:depth"
		dir_name = "depth"
	elif (heur == 7):
		heur_option = "--search=nurs:icnt"
		dir_name = "icnt"
	elif (heur == 8):
		heur_option = "--search=nurs:cpicnt"
		dir_name = "cpicnt"
	elif (heur == 9):
		heur_option = "--search=nurs:qc"
		dir_name = "qc"
	else:
		heur_option = "--search=dfs --search=random-state --search=random-path --search=nurs:covnew --search=nurs:md2u --search=nurs:depth --search=nurs:icnt --search=nurs:cpicnt --search=nurs:qc"
		dir_name = "all"
	os.system("klee --external-calls=all " + heur_option + " --optimize --output-dir=data_new/run_data_" + dir_name + "_" + str(rb) + "_" + str(k) + " explicit_symbolic_attack.bc " + str(rb) + " " + str(k) + " ./data_new/run_"+ dir_name + "_" +str(rb) + "_" + str(k) + ".txt")

def main(argv):
	rb = int(sys.argv[1])
	max_k = int(sys.argv[2])
	heur = int(sys.argv[3])

	if heur == 0:
		# Looping through each k:
		for k in range(1, max_k+1):
			call_symbolic_attack(rb, k)
	else:
		# Looping through each k:
		for k in range(1, max_k+1):
			call_heu_symbolic_attack(rb, k, heur)

if __name__ == "__main__":
   main(sys.argv[1:])
