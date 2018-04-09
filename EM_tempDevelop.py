

## EM example:

import itertools
import numpy as np
from scipy import linalg
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
from importADNI_develop import *

from sklearn import mixture

color_iter = itertools.cycle(['navy', 'c', 'cornflowerblue', 'gold',
                              'darkorange'])


def plot_results(X, Y_, means, covariances, index, title):
    splot = plt.subplot(2, 1, 1 + index)
    for i, (mean, covar, color) in enumerate(zip(
            means, covariances, color_iter)):
        v, w = linalg.eigh(covar)
        v = 2. * np.sqrt(2.) * np.sqrt(v)
        u = w[0] / linalg.norm(w[0])
        # as the DP will not use every component it has access to
        # unless it needs it, we shouldn't plot the redundant
        # components.
        if not np.any(Y_ == i):
            continue
        plt.scatter(X[Y_ == i, 0], X[Y_ == i, 1], .8, color=color)

        # Plot an ellipse to show the Gaussian component
        angle = np.arctan(u[1] / u[0])
        angle = 180. * angle / np.pi  # convert to degrees
        ell = mpl.patches.Ellipse(mean, v[0], v[1], 180. + angle, color=color)
        ell.set_clip_box(splot.bbox)
        ell.set_alpha(0.5)
        splot.add_artist(ell)

#    plt.xlim(-9., 5.)
#    plt.ylim(-3., 6.)
    plt.xticks(())
    plt.yticks(())
    plt.title(title)
    plt.xlabel('abeta')
    plt.ylabel('FDG')


# Number of samples per component
n_samples = 500
#
#
###########################################3



DataSet = pd.read_csv('DataNone.csv',low_memory=False)

NewDataSet = DataSet

NewDataSet = NewDataSet.replace('-4',np.NaN)
NewDataSet = NewDataSet.replace(' ',np.NaN)
NewDataSet,NumeriColumns = fixBrokenDataSet(NewDataSet,'TurnNaN')

axislabels = list(NewDataSet.columns[NumeriColumns])

[uu, vv] = NewDataSet.shape

#
X = NewDataSet.iloc[:,[1,2]]
X = X.dropna(axis = 'rows',how = 'any')
X = X.values
X = X.astype(float)

###########################################

# Fit a Gaussian mixture with EM using five components
gmm = mixture.GaussianMixture(n_components=3, covariance_type='full').fit(X)
plot_results(X, gmm.predict(X), gmm.means_, gmm.covariances_, 0,'Gaussian Mixture')

# Fit a Dirichlet process Gaussian mixture using five components
#dpgmm = mixture.BayesianGaussianMixture(n_components=3,                                       covariance_type='full').fit(X)
#plot_results(X, dpgmm.predict(X), dpgmm.means_, dpgmm.covariances_, 1,
#             'Bayesian Gaussian Mixture with a Dirichlet process prior')

#plt.show()
plt.savefig('GaussianMixture_abeta_FDG.svg')



################################# Missing Data Implementation ##############

from numpy import linalg as LA

import numpy as np
from scipy import linalg
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
from importADNI_develop import *
from sklearn import mixture

DataSet = pd.read_csv('DataNone.csv',low_memory=False)

NewDataSet = DataSet

NewDataSet = NewDataSet.replace('-4',np.NaN)
NewDataSet = NewDataSet.replace(' ',np.NaN)
NewDataSet,NumeriColumns = fixBrokenDataSet(NewDataSet,'TurnNaN')

axislabels = list(NewDataSet.columns[NumeriColumns])

X = NewDataSet.iloc[:,NumeriColumns]
X = X.dropna(axis = 'rows',how = 'any')
X = X.values
X = X.astype(float)


[uu, vv] = NewDataSet.shape

gmm = mixture.GaussianMixture(n_components=3, covariance_type='full').fit(X)


Means = gmm.means_
Covs = gmm.covariances_


##

NumericalData = NewDataSet.iloc[:,NumeriColumns]

Identification = np.array(NewDataSet.loc[:,'RID'])

uniqueID = np.unique(Identification)

CorrectLaterMemory = [None]*len(uniqueID)

for u,ID in enumerate(uniqueID):    
    
    ## Find all the row indices that are equal to ID in uniqueID
    idx = list((Identification==ID).nonzero())
    ## Treat Variable
    idx = idx[0]
    
    ## Get values
    tempData = NumericalData.iloc[idx,:].values
    
    ## True = it is missing data, i.e. NaN     
    MissingData = np.isnan(tempData.astype(float))
    
    ## True = it is numeric
    MissingDataInverse = np.invert(MissingData)
    
    ## Allocate
    dist = [None]*Means.shape[0]
    SomeNaN = 1 
    
    for i in range(len(idx)):
           ## If all values are numeric: 
        if MissingDataInverse[i,:].all():
            
            SomeNaN == 0
            CorrectLaterMemory[u] = None
            
            ## Find the the Mixture that the best approximates the Feature vector of ID
            for j in range(Means.shape[0]):
                dist[j] = LA.norm(NumericalData.iloc[idx[i],:].values - Means[j,:])
            
            # Parameters of the distribution in which
            #the tested feature lies
            mu = Means[np.argmin(dist),:]
            SIGMA = Covs[np.argmin(dist)]
            
            # Generate and replace NaNs from the mixture of Gaussians
            for jj in range(len(idx)):
                NumericalData.iloc[idx[jj],MissingData[jj,:]] = GenerateSamplefromMixture(mu,SIGMA)
            
            break
        
    ## If none of the rows are numeric (i.e. contain some NaNs on it)    
    if SomeNaN == 1:
        
    ## Look for other IDS with similar DX and correct them later
    CorrectLaterMemory[u] = i
        
            
    
    
################################# Missing Data Implementation ##############


def GenerateSamplefromMixture(mu,SIGMA):
    ## Generate a feature to replace NaN values
    repetition = 10
    tempsample = np.zeros(repetition,Means.shape[0])
    for r in range(repetition)
        tempsample[r,:] = np.random.multivariate_normal(mu,SIGMA,1)
                    
    sample = np.median(tempsample,0)
    
    return(sample)


