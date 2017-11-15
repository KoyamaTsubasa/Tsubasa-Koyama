import numpy as np
import scipy as sp
import pdb



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
    myval = mygacha(myPs[select])
    return myval
