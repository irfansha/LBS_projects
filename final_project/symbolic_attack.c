/* Irfansha Shaik, 16.05.2020, Aarhus.
 */

#include <klee/klee.h>

//#include<string.h>
#include<stdio.h>
#include<stdlib.h>


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


/**
  * The main function
  */
int
main (int argc, char *argv[])
{
	int step = 0;    //Step number
        int k = 2;	// number of total steps
	int public_inputs[k];

        int total_cost = 0;

        int lb = atoi(argv[1]);   // left bound of secret domain size
        int rb = atoi(argv[2]);   // right bound of secret domain size

        // Making the secret symbolic as it is unknown:
        klee_make_symbolic(&secret, sizeof(secret), "secret");
        //secret = 4;

        // Making the public inputs symbolic:
	klee_make_symbolic(public_inputs,k * sizeof(int),"public inputs");

        if (secret >= lb && secret <= rb) {
	        /* Iterate and run 'vulnerable function'
		   we only consider the sequence of inputs which are within current bounds
		   i.e. learning from previous observations
		*/
	        while(step < k && public_inputs[step] >= lb && public_inputs[step] <= rb) {
			int cost = vulnerable_function(public_inputs[step]);
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
		        //increment iteration
		        step++;
	        }
          }
}
