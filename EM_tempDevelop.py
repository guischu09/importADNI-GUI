#import itertools
#
#import numpy as np
#from scipy import linalg
#import matplotlib.pyplot as plt
#import matplotlib as mpl
#import pandas as pd
#from importADNI_develop import *
#
#
#from sklearn import mixture
#
#color_iter = itertools.cycle(['navy', 'c', 'cornflowerblue', 'gold',
#                              'darkorange'])
#
#
#def plot_results(X, Y_, means, covariances, index, title):
#    splot = plt.subplot(2, 1, 1 + index)
#    for i, (mean, covar, color) in enumerate(zip(
#            means, covariances, color_iter)):
#        v, w = linalg.eigh(covar)
#        v = 2. * np.sqrt(2.) * np.sqrt(v)
#        u = w[0] / linalg.norm(w[0])
#        # as the DP will not use every component it has access to
#        # unless it needs it, we shouldn't plot the redundant
#        # components.
#        if not np.any(Y_ == i):
#            continue
#        plt.scatter(X[Y_ == i, 0], X[Y_ == i, 1], .8, color=color)
#
#        # Plot an ellipse to show the Gaussian component
#        angle = np.arctan(u[1] / u[0])
#        angle = 180. * angle / np.pi  # convert to degrees
#        ell = mpl.patches.Ellipse(mean, v[0], v[1], 180. + angle, color=color)
#        ell.set_clip_box(splot.bbox)
#        ell.set_alpha(0.5)
#        splot.add_artist(ell)
#
##    plt.xlim(-9., 5.)
##    plt.ylim(-3., 6.)
#    plt.xticks(())
#    plt.yticks(())
#    plt.title(title)
#    plt.xlabel('abeta')
#    plt.ylabel('FDG')
#
#
## Number of samples per component
#n_samples = 500
#
#
###########################################3
#DataSet = pd.read_csv('DataNone.csv',low_memory=False)
#
#NewDataSet = DataSet
#
#NewDataSet = NewDataSet.replace('-4',np.NaN)
#NewDataSet = NewDataSet.replace(' ',np.NaN)
#NewDataSet,NumeriColumns = fixBrokenDataSet(NewDataSet,'TurnNaN')
#
#axislabels = list(NewDataSet.columns[NumeriColumns])
#
#[uu, vv] = NewDataSet.shape
#
#
#X = NewDataSet.iloc[:,[1,2]]
#X = X.dropna(axis = 'rows',how = 'any')
#X = X.values
#X = X.astype(float)
#
############################################
#
## Fit a Gaussian mixture with EM using five components
#gmm = mixture.GaussianMixture(n_components=3, covariance_type='full').fit(X)
#plot_results(X, gmm.predict(X), gmm.means_, gmm.covariances_, 0,'Gaussian Mixture')
#
## Fit a Dirichlet process Gaussian mixture using five components
##dpgmm = mixture.BayesianGaussianMixture(n_components=3,
##                                        covariance_type='full').fit(X)
##plot_results(X, dpgmm.predict(X), dpgmm.means_, dpgmm.covariances_, 1,
#             'Bayesian Gaussian Mixture with a Dirichlet process prior')

#plt.show()
#plt.savefig('GaussianMixture_abeta_FDG.svg')



from numpy import linalg as LA
####

Means = gmm.means_
Covs = gmm.covariances_

NumericalData = NewDataSet.iloc[:,NumeriColumns]

Identification = np.array(NewDataSet.loc[:,'RID'])

uniqueID = np.unique(Identification)

for u,ID in enumerate(uniqueID):    
    
    idx = list((Identification==ID).nonzero())
    idx = idx[0]
    
    tempData = NumericalData.iloc[idx,:].values
        
    MissingData = np.isnan(tempData.astype(float))
    MissingDataInverse = np.invert(MissingData)
    
    dist = [None]*Means.shape[0])
    
    for i in range(idx):
        
        if MissingDataInverse[i,:].all():
        
            for j in range(Means.shape[0]):
                dist[j] = LA.norm(NumericalData.iloc[idx[i],:].values - Means[j,:])
            
            mu = Means[min(dist),:]
            SIGMA = Covs[min(dist)]
            
            x = np.random.multivariate_normal(mu,SIGMA,1)
            break
        
#        else:
            # Pensar o que fazer com os casos em que para todos os meses há missing data
            
    
    







