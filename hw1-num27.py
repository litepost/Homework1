import pandas as pd
import random as rand 
from numpy import mean

def main():
    rand.seed();
    block_size = 2048 * 8   # number of bits = 16,384
    trials = []

    for trial in range(0, 30):
        process_count = 0
        total_frag = 0
        for i in range(0, 10000):
            process_size = rand.randint(1, 20000)
            if process_size < block_size:
                process_count += 1
                total_frag += block_size - process_size
        # calc avg internal frag and store it
        trials.append(total_frag / process_count)

    output = '['
    for t in trials:
        if output == '[':
            output += '{0}'.format(round(t, 2))
        else:
            output += ', {0}'.format(round(t, 2))
            
    output += ']'
    print("avg internal fragmentations: " + output)
    print('overall avg internal fragmentation: {0}'.format(round(mean(trials), 2)))
    
        
if __name__ == '__main__':
    pd.set_option('display.width', 750)
    main()
