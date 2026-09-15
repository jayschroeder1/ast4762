#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Jay Schroeder
#Homework 3
#Sep 15, 2026

""" Support functions for HW3
    Jay Schroeder
    Sep 15, 2026

    This module is built to contain the function 'square'
"""

import numpy as np

#2
print('Problem 2')
#prints the problem number

def square(x):
#defining the function 'square' 
    """ A function which returns the square of inputs.

    Parameters
    ----------
    x : scalar or array_like,
    Variable which can be either a numeric input value or values. This 
    input may be a scalar or array of some specified dimension. 
    #description of parameters, ie variables, which will be used in this function

    Returns
    -------
    scalar or ndarray,
    This returns the square of each element within the input. The return type
    will match the input, and the results will be a product based of the 
    mathematic processes of the NumPy package.
    #desciption of expected returns

    Examples
    --------
    >>> square(4)
    16

    >>> square(np.array( [4, 6, 8] ))
    array( [16, 36, 64] )

    >>> square(np.array( [1, 4], [5,9] ))
    array( [1, 16],
           [25, 81] )
    #examples of what can be put into the function, and what can be expected out

    """
    return x * x
    #exits the function, 

#print( square(5) )
#print(square(np.array( [20, 4] )))
#print(square(np.array( [[20, 4], 
                       #[5, 10]] )))


# In[ ]:





# In[ ]:





# In[ ]:




