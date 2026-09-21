#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Jay Schroeder
#Homework 4
#Sep 20, 2026


# In[1]:


print( 'Problem 2, Parts a-c' )

import numpy as np
import matplotlib.pyplot as plt

#values of mu, sigma, and N corresponding to Problem 2
mu = 55
sig = 13
N = 10000

#draws a random sample of N draws from a Gaussian distribution of mean mu=55
#and standard deviation sigma=13
#assigns variable 'sample' to draw
sample = np.random.normal(mu, sig, N)

#prints 'sample' as a check 
print(sample)

#creates histogram of 'sample' with limits 'bins'
bins = np.arange( 0,101, 1 )
plt.hist( sample, bins=bins )

#creates a plot of the Gaussian distribution, scales it to N, and plots it accordingly
x = np.arange( 0.5, 100, 1 )
gaussian = ( 1 / (sig*np.sqrt(2*np.pi)) ) * np.exp( -0.5*((x-mu)/sig)**2 )
gaussian = gaussian * N
plt.plot( x, gaussian)

#organizes and presents the histogram of 'sample'
plt.xlabel( 'x' )
plt.ylabel( 'N(x)' )
plt.title( 'Histogram of a Gaussian' )

#displays and shows the histogram as a png
plt.savefig( 'hw4_jmschroeder_plotofgaussiansample.png' , dpi = 300 )
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:




