#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Jay Schroeder
#Sep 27th, 2025
#Sigrej Function for Homework Five


# In[4]:


import numpy as np

def sigrej( data, limits, mask=None):
    ''' A function which takes in a data array and returns a sigma rejection on said array.

    Parameters
    ----------
    data : array_like
        Variable which takes in an array of data to be sigma clipped.

    limits : tuples
        Variable which takes in a tuple containing the rejection limit in terms of
        number of standard deviations the mask will use. 

    mask : array_like of bool, optional 
        Variable which takes in an optional Boolean mask of the same shape as the 
        data. This mask indicates which data is initially 'good' with a simple test
        where False=bad and True=good. If no mask is input, then the all data defaults
        to initially 'good'.

    Returns
    -------
    mask : numpy.ndarray 
        This returns a Boolean mask after sigma rejection. A return of 'True' indicates 
        a 'good' data point and 'False' indicates a 'bad' data point.

    Example
    --------
    >>> sigrej( np.array([10,11,10,12,100]), (5., 5.) )
    array( [True, True, True, True, False] )

    Updates
    -------
    Tab for updates if and when they are made. 

    '''

    data = np.asarray(data)

    if mask is None:
        mask = np.ones( data.shape, dtype=bool )
    else: 
        mask = np.array( mask, dtype=bool, copy=True )

    for limit in limits:
        good_data = data[mask]
        mean = np.mean(good_data)
        sig = np.std(good_data)
        mask = mask & ( np.abs(data - mean) <= limit*sig )

    return mask


# In[ ]:





# In[ ]:




