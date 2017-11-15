import numpy as np
import Gacha as G
import pdb

def main():

    #Number of experiments

    numExperiment = 500

    #Number of pulls on each experiment
    numIter = 500
    myEpsilon = 0.2
    gachaPs = np.array([0.5, 0.4, 0.2, 0.45, 0.99])
    mymode = 'EG'

    '''
    If mode = 'EG',  This will run Epsilon Greedy.
    If mode = 'Tsubasa', This will run YOURS
    '''

    scores  = []

    for expIndx in range(numExperiment):

        FinalScore = G.run_experiment(gachaPs,numIter,myEpsilon, mode = mymode)

        scores += [FinalScore]
        print("Final Score was %s"%(FinalScore))

    '''
    Mean is the average.
    sqrt of variance is Standard Deviation
    '''
    print("average record of the final Scores:%s"%np.mean(scores))
    print("std of the record of the final Scores:%s"%np.sqrt(np.var(scores)))



if __name__ == '__main__':
    main()
