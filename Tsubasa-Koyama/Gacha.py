import numpy as np
import scipy as sp
import Gacha as G




def mygacha(myP):
    GachaResult = np.random.multinomial(1,myP)
    GachaResult = np.where(GachaResult ==1)[0][0]
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
