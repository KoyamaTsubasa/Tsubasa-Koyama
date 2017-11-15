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


def TsubasaMachine():
    return 0


def EpsilonGreedyMachine(currentRecord, myPs, epsilon = 0.2):
    Maxval = np.max(currentRecord)
    gachaIndex = range(len(myPs))
    theBest = random.choice(np.where(currentRecord == Maxval)[0])

    GreedyOrEpsilon = np.random.multinomial(1,[epsilon, 1-epsilon])[0]
    if GreedyOrEpsilon == 1:
        select = random.choice(gachaIndex)
    else:
        select = theBest

    return select


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



    for j in range(numExps):
        # Machine chooses the lever to pull
        if mode == 'EG':
            machineSelect = EpsilonGreedyMachine(currentRecord, myPs, epsilon = myEpsilon)
        elif mode =='Tsubasa':
            machineSelect =  TsubasaMachine()
        else:
            raise NotImplementedError

        oldRecord = copy.copy(currentRecord)
        #Update the record according to the decision
        currentRecord = G.UpdateRecord(currentRecord, myPs, machineSelect)

        #History of outcomes Up to now
        #outcomeThisRound = currentRecord - oldRecord
        #RecordHistoryList = RecordHistoryList + [outcomeThisRound]
        #RecordHistory = np.array(RecordHistoryList)


        #if j > 100:
        #    pdb.set_trace()

        numLeverPulled[machineSelect]+=1



        if np.mod(j, 100) ==0 :
        #Report!
            print("%s th pull made"%j)
            print("Number of Pulls:%s"%numLeverPulled)
            print("Current Score:%s"%currentRecord)
    FinalScore= np.sum(currentRecord)

    return FinalScore
