import numpy as np
import Gacha as G
import pdb

def main():

    numExps = 1000
    myEpsilon = 0.2
    gachaPs = np.array([0.3, 0.4, 0.8, 0.2, 0.9])


    FinalScore = G.run_experiment(gachaPs,numExps,myEpsilon, mode = 'EG')

    print("Final Score was %s"%(FinalScore))




if __name__ == '__main__':
    main()
