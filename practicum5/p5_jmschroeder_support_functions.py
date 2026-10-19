#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np


# In[1]:


def normmedcomb(data, normreg=None):
    """
    A function for performing normalized median combination on a 3D array of data.

    Parameters
    ----------
    data : 3D numpy.ndarray
        Variable that takes in a 3D array of dark-subtracted
        image data with dimensions (nframes, ny, nx)

    normreg : tuple, optional 
        Variable that determines how the data will be 
        treated. It takes in a normalization region
        specified by ( (y1, x1), (y2, x2) ) and calculates
        a normalization factor for each frame. If no region
        is specified, it defaults to taking in the entire image.

    Returns
    -------
    normmed : 2D numpy.ndarray
        An array which contains the normalized, median-combined 
        image with dimensions ( ny, nx ).

    normfactors : 1D numpy.ndarray
        An array which contains the normalization factor of each 
        frame of the image.

    Example
    -------
    >>> normmed, normfactor = normmedcomb(data)
    >>> normmed, normfactor = normmedcomb( data, normreg=( (100, 200), (200, 300))

    Updates
    -------
    """
    nframes, ny, nx = data.shape     #defining variables for the frame

    if normreg is None:               #determines how the frame will be treated depending on 
        y1, x1 = 0, 0                 #whether or not a region is defined
        y2, x2 = ny, nx
    else: 
        (y1, x1), (y2, x2) = normreg

    normfactor = np.median( data[:, y1:y2, x1:x2], axis=(1,2) )   #calculates normalization factors
    normdata = data / normfactor[:, np.newaxis, np.newaxis]       #normalizing each factor
    normmed = np.median( normdata, axis=0 )                       #performs median-combination on the normalized frames


    return normmed, normfactor


# In[ ]:




