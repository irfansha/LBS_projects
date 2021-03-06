/* Irfansha Shaik, 16.05.2020, Aarhus.
 */

#include <klee/klee.h>

//#include<string.h>
#include<stdio.h>
#include<stdlib.h>
#include <assert.h>


int secret;

/**
  * Return execute and return cost:
  */
int vulnerable_function(int public_input)
{

        if (secret >= public_input) {
		return 2;   // returning cost 2:
        }
	else {
		return 1;   //returning cost 1:
	}
}


int is_valid(int lb, int rb, int *public_inputs, int step) {
	if (public_inputs[step] >= lb && public_inputs[step] <= rb) {
		// return false if input is a reoccurance:
		for (int i = 0; i<step; ++i) {
			if (public_inputs[i] == public_inputs[step]) { return 0; }
		}
		return 1;
	}
	return 0;
}

/**
  * The main function
  */
int
main (int argc, char *argv[])
{

        int lb = 1;   // fixing left bound to 1
        int rb = atoi(argv[1]);   // right bound of secret domain size
	int domain_size = rb;     // domain size
	int step = 0;    //Step number
        int k = atoi(argv[2]);	// number of total steps
	int public_inputs[k];
	int cost_observations[k];  // array for storing cost observations

        int total_cost = 0;

	// Resetting public inputs:
	for (int i = 0; i < k; i++) {
		public_inputs[i] = 0;
	}

	// Resetting cost observations:
	for (int i = 0; i < k; i++) {
		cost_observations[i] = 0;
	}

        // Making the secret symbolic:
	klee_make_symbolic(&secret,sizeof(int),"secret");

        // Making the public inputs symbolic:
	klee_make_symbolic(public_inputs,k * sizeof(int),"public inputs");

        if (secret >= lb && secret <= rb) {
	        /* Iterate and run 'vulnerable function'
		   we only consider the sequence of inputs which are within current bounds
		   i.e. learning from previous observations
		*/
	        for(int step = 0; step < k && is_valid(lb, rb, public_inputs, step) && rb > lb; step++) {
			int cost = vulnerable_function(public_inputs[step]);
			cost_observations[step] = cost;
			/*
			Here we update the domain boundaries secret input
			*/
			if (cost == 1) {
				rb = public_inputs[step] - 1;   // updating with current public_input -1 (as less than)
			}
			else {
				lb = public_inputs[step];   // updating with current public input
			}
			// Cumulating cost:
			total_cost = total_cost + cost;
	        }
          }
	assert(lb <= rb);
}
