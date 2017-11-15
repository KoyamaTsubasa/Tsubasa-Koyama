import numpy as np
import scipy as sp
import Gacha as G
import pdb
import random



def mygacha(myP):
    GachaResult = np.random.multinomial(1,myP)
    return GachaResult[0]

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
