import numpy as np
import matplotlib.pylab as plt
import scipy.stats
mv=np.genfromtxt('cumulos_globulares.dat',skip_header=1,usecols=6)
indx=~np.isnan(mv)
mv=mv[indx]
alfa=0.5
a1=alfa/2.
a2=(1.-a1)

B=15000
medias=np.array([],dtype=float)

for i in range(B):
	random=np.random.choice(mv,size=148)	
	#random.mean() ->me da la medias
	medias=np.append(medias,random.mean())

plt.hist(medias,bins=100)
#plt.show()
sigma=np.std(medias)
media=np.mean(medias)

#ECM=np.sum(medias-np.mean(mv))/B

L=scipy.stats.norm.ppf(a1,media,sigma)
R=scipy.stats.norm.ppf(a2,media,sigma)


