import numpy as np
import Gacha as G
import pdb

def main():

    numExps = 1000
    myEpsilon = 0.2
    gachaPs = np.array([0.3, 0.4, 0.8, 0.2, 0.9])
    mymode = 'EG'

    '''
    If mode == 'EG',  This will run Epsilon Greedy.
    If mode == 'Tsubasa', This will run YOURS
    '''

    FinalScore = G.run_experiment(gachaPs,numExps,myEpsilon, mode = mymode)

    print("Final Score was %s"%(FinalScore))




if __name__ == '__main__':
    main()
