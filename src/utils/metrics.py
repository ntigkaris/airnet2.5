import numpy as np

def IoA(v,u):
    '''Index of Agreement'''
    return 1 - (np.sum((v-u)**2) )/( np.sum((np.abs(u-np.mean(v))+np.abs(v-np.mean(v)))**2))
