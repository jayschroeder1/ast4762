#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Jay Schroeder
#Homework 4
#Sep 20, 2026


# In[4]:


print( 'Problem 2, Parts a-c' )

import numpy as np

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


# In[ ]:





# In[ ]:




