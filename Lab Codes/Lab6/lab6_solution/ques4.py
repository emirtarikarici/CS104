##
# Simulate rolling two dice many times and 
# compare the simulated results to the results
# expected by probability theory.
#
from random import randrange

NUM_RUNS   = 1000
D_MAX  = 6

def twoDice():
    """ Simulate rolling two six-sided dice
        @return the total from rolling two simulated dice
    """
    d1  = randrange(1,       D_MAX   +  1)
    d2  = randrange(1,       D_MAX   +  1)

    return d1 + d2

def main():
    """ Simulate many rolls and display the result
    """
    # Create a dictionary of expected proportions
    expected   = {2: 1/36, 3: 2/36, 4: 3/36, 5: 4/36, 6: 5/36, 7: 6/36, 8: 5/36, 9: 4/36, 10: 3/36, 11: 2/36, 12: 1/36}

    # Create a dictionary that maps from the total of two dice to 
    # the number of occurrences
    counts  = {value: 0 for value in range(2,13)} 

    # Simulate NUM RUNS rolls, and count each roll
    for i in range (NUM_RUNS):
        t = twoDice()
        counts[t] = counts[t] + 1
    # Display the simulated proportions and the expected proportions
    print("Total          Simulated        Expected")
    print("                  Percent         Percent")
    for i in sorted (counts.keys()):
        print ("%5d %11.2f       %8.2f"  % (i,counts[i] / NUM_RUNS  * 100,   expected[i]      *  100))

main()
