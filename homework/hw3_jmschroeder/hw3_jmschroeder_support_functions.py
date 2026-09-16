#!/usr/bin/env python
# coding: utf-8

# In[3]:


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
print('Problem 2 parts a through g')
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

    Updates
    -------
    Commented out test statements at the bottom of cell.

    Rewrote print statement containing problem number and part
    >>> print('Problem 2')
    >>> print('Problem 2 parts a through g')

    """
    return x * x
    #exits the function, 

#print( square(5) )
#print(square(np.array( [20, 4] )))
#print(square(np.array( [[20, 4], 
                       #[5, 10]] )))


# In[6]:


#3
print( 'Problem 3 parts a through d' )
#prints the problem number

import numpy as np
import matplotlib.pyplot as plt

def squareplot(low, high, npoints, saveplot=False):
#defining the function 'square' 
    """ A function designed to plot the squares of numbers.

    Parameters
    ----------
    low : float,
    This is a variable which detemines the lower end of the range of the plot
    of the function.

    high : float, 
    This is a variable which determines the upper end of the range of the plot
    of the function.

    npoints : int,
    This is a variable which constitutes the number of points the funcition will plot
    on the resulting graph. 

    saveplot : str or bool, optional argument
    This is a filename and is an optional argument which will determine whether or not 
    the function saves the plot. If False, the plot is not saved. If True, the function must
    save the ploted image as PDF.

    #these are our variable, there are more than in function 'square' but if we can describe
    them in detail then it should be easy to keep track of them.

    Returns
    -------
    None : this function has no return, it simple displays the square function may save it
    depending on the status of the variable 'saveplot'

    #there are no returns here because no values are spit out, only a graph

    Examples
    --------
    >>> squareplot( 1, 7, 5 "squareplot_example.pdf")

    #example of what to input and expect from squareplot

    Updates
    -------
    Fixed an issue with the structure of the if statement:
    >>> if saveplot is False:
    >>> if saveplot is not False:

    Added imports:
    >>> import numpy as np
    >>> import matplotlib.pyplot as plt

    Fixed a bug where 'plt.savefig' was misspelled as 'plt.savfig'

    """

    x = np.linspace( low, high, npoints )
    y = square(x)
    #defines the range and number of points on the graph as variable 'x', before 
    #calling the square function to square these values and save then as variable 'y'

    plt.plot( x, y )
    plt.xlabel( "Input" )
    plt.ylabel( "Output" )
    plt.title( "Square Function Plot" )
    #plots and labels the graph of the function accordingly

    if saveplot is not False: 
        plt.savefig(saveplot, format="pdf")
        #presents a condition regarding when to save the graph as a PDF

    plt.show()



# In[ ]:





# In[ ]:




