        """
Created on Wed Nov 19 22:08:29 2018

@author: Chandler Long  

Demonstration of the famous Pagerank Algorithm by Google
"""


import numpy as np
import scipy as sc
import pandas as pd
from fractions import Fraction
 
webMatrix = np.matrix([[0,0,1, Fraction(1,2)],
        [Fraction(1,3),0,0,0],
        [Fraction(1,3), Fraction(1,2),0,Fraction(1,2)],
         [Fraction(1,3), Fraction(1,2),0,0]])

pageProbablity = Fraction(1,4)

V = np.zeros((4,4))
V[:] = pageProbablity
 
dampingFactor = 0.7
 

googleMatrix = dampingFactor * webMatrix + ((1 - dampingFactor) * V)

rankVector = np.matrix([[pageProbablity], 
                       [pageProbablity],
                       [pageProbablity], 
                       [pageProbablity]])

currentIterations = 0
maxIterations = 100

previousRValue = rankVector

while(currentIterations <= maxIterations):
    
    rankVector = googleMatrix * rankVector
    if(previousRValue == rankVector).all():
        break
    previousRValue = rankVector
    currentItterations += 1
    
print("Final Page Rank: \n", rankVector)
print("Sum of Pages: ", np.sum(rankVector))

