#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np 

def box_function( x, center, width, height ):
    ''' A function which returns a rectangular window function for 
        exoplanet transit data.

    Parameters
    ----------
    x : array_like 
        Variable which takes in an array of observational times.

    center : float 
        The time at the center of the rectangular window.

    width : float 
        The total width of the rectangular window.

    height : float
        The value ascribed to the height of the window within set boundaries.

    Returns
    -------
    window : numpy.ndarray
        An array containing the rectangular window function. Values beyond 
        the window are attributed to zero, while values inside the window 
        are set equal to a specified height. 

    Example
    -------
    >>> box_function( np.array([0, 1, 2, 3, 4]), 2.0, 2.0, -0.01 )
    array( [0.0, -0.01, -0.01, -0.01, 0.0] )

    Updates
    -------
    No updates as of 02:19:31 Oct 12, 2026
    '''

    x = np.asarray(x)

    window = np.zeros( x.shape )
    window[ np.abs(x-center) <= width/2 ] = height

    return window


# In[ ]:





# In[ ]:




