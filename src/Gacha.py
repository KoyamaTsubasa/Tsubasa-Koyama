import numpy as np
import scipy as sp
import Gacha as G
import pdb
import random
import copy

'''
numLeverPulled is not used in Epsilon Greedy!!!

RecordHistory  is not used in Epsilon Greedy!!

'''



def mygacha(myP):
    GachaResult = np.random.multinomial(1,myP)
    GachaResult = np.where(GachaResult ==0)[0][0]
    return GachaResult

def gachaRepeat(numPull, myP):
    record = np.zeros(numPull)
    for k in range(numPull):
        record[k] = mygacha(myP)

    return record


def myPull(select,myPs):
    myval = G.mygacha(myPs[select])
    return myval


def UpdateRecord(currentRecord, myPs, select):
    val = myPull(select, myPs)
    currentRecord[select]+=val
    return currentRecord


'''
Create your own Tsubasa Machine here!!!
'''

def TsubasaMachine():

    return 0


'''
Epsilon Greedy Machine will take a look at the currentRecord of each Gacha and decide which Gacha to pull in the next round.
'''
def EpsilonGreedyMachine(currentRecord, myPs, epsilon = 0.2):

    #Find the Gacha with the best Score
    Maxval = np.max(currentRecord)
    gachaIndex = range(len(myPs))
    theBest = random.choice(np.where(currentRecord == Maxval)[0])

    #If this is one, EXPLORE.  Otherwise, pick the best Gacha
    GreedyOrEpsilon = np.random.multinomial(1,[epsilon, 1-epsilon])[0]
    if GreedyOrEpsilon == 1:
        select = random.choice(gachaIndex)
    else:
        select = theBest

    return select

'''
run experiment will take in the information of Gacha, name of the machine, and run the experiment
'''

def run_experiment(gachaPs,numExps,myEpsilon, mode = 'EG'):
    numGacha = len(gachaPs)
    myPs = np.zeros([numGacha ,2])


    for k in range(numGacha):
        myPs[k,0] = gachaPs[k]
        myPs[k,1]= 1- gachaPs[k]

    #This is for Debugging purpose!!!
    #pdb.set_trace()

    currentRecord = np.zeros(numGacha)
    RecordHistoryList = []
    numLeverPulled = np.zeros(numGacha)


    '''
    Pull the Gacha for numExps number of times!
    iteration is the number of pulls you have made so far.
    '''
    for iteration in range(numExps):

        '''
        Machine choose the lever here!! mode will decide the type of the machine!
        '''
        if mode == 'EG':

            '''
            Epsilon Greedy Mode!
            '''
            machineSelect = EpsilonGreedyMachine(currentRecord, myPs, epsilon = myEpsilon)
        elif mode =='Tsubasa':

            '''
            Tsubasa Machine MODE!!! You need to change HERE!!
            '''
            machineSelect =  TsubasaMachine()
        else:
            raise NotImplementedError

        '''
        Pull the lever, and Update the record according to the decision
        '''
        oldRecord = copy.copy(currentRecord)
        currentRecord = G.UpdateRecord(currentRecord, myPs, machineSelect)
        numLeverPulled[machineSelect]+=1


        #History of outcomes Up to now! Use it at your own discretion
        #outcomeThisRound = currentRecord - oldRecord
        #RecordHistoryList = RecordHistoryList + [outcomeThisRound]
        #RecordHistory = np.array(RecordHistoryList)


        '''
        Report the intermediate result at every 100 iterations
        '''
        if np.mod(iteration, 100) ==0 :
            print("%s th pull made"%iteration)
            print("Number of Pulls:%s"%numLeverPulled)
            print("Current Score:%s"%currentRecord)
    FinalScore= np.sum(currentRecord)

    return FinalScore
