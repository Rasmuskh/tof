import numpy as np

#A = rdr.load_events('wave0.txt')
def inv(Samples):
    #B=bl.baseliner2(Samples)
    #Samples=Samples-B
    shift=2
    frac=0.40
    invsig=np.zeros(len(Samples))
    invsig[0:-shift]=-frac*Samples[shift:]
    #invLead=np.zeros(len(Samples))
    #invLead[shift:]=-frac*Samples[0:-shift]
    return invsig+Samples#Samples+invLag, Samples+invLead



def zerocrosser(invsig):
    crossing = np.argmin(invsig)
    #cross_right = cross_left+np.argmin(inv2[cross_left:-1])
    #if cross_right<cross_left:
    #    print('!!!!!!!!!!!!!!!!!!!!!!!!!')
    return crossing#_left, cross_right
