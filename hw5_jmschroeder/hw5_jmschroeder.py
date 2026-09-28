#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Jay Schroeder
#Sep 27th, 2025
#Homework Five

import numpy as np
import matplotlib.pyplot as plt


# In[13]:


print( 'Problem Two' )

#this code is copied from 'practicum3_jmschroeder'

#N number of photons
N = 10000

#draws from a poisson distribution for N photons, and a uniform distribution between 0 and 10^6
pix_poi = np.random.poisson( N, 396 )
pix_uni = np.random.uniform( 0, 10**6, 4 )

#concatenates the two samples and perscribes then variable 'sample', before taking the mean and median
#and printing the result
sample = np.concatenate( (pix_poi, pix_uni) )
mean = np.mean(sample)
med = np.median(sample)

#standard deviation of 'sample'
sig = np.std(sample)

#creating a mask for this data using a subsample within 5sigma called 'subsample'
subsample = sample[ np.abs(sample - med) <= 5*sig ]
print( f"Standard Deviation: {sig}" )
print( f"Sample Mean: {np.mean(subsample)}, Sample Median: {np.median(subsample)}" )
print( f"Subsample Stardard Deviation: {np.std(subsample)}" )



# In[15]:


#assigning variables to the median and std. dev. of 'subsample'
submed = np.median(subsample)
subsig = np.std(subsample)

#creating a second mask for this data using a subsample of subsample again within 5sigma called 'sub_sub'
sub_sub = subsample[ np.abs(subsample - submed) <= 5*subsig ]
print( f"Standard Deviation: {subsig}" )
print( f"Subsample Mean: {np.mean(sub_sub)}, Subsample Median: {np.median(sub_sub)}" )
print( f"Sub-subsample Stardard Deviation: {np.std(sub_sub)}" )

''' This new clipping removes additional extraneous points in the tails, in turn making the the standard
    deviation smaller and thus closer to the Poisson distribution. The new mean and median are closer to 
    N = 10000, and the sub-sample standard deviation is closer to 100. This method will not always remove
    bad pixels because if for example a bad pixel exists within the 5sigma clipping range, it will not be 
    removed. '''


# In[ ]:




