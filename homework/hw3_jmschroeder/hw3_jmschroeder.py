#!/usr/bin/env python
# coding: utf-8

# In[10]:


#2 
print( 'Problem 2 parts h and i' )

import numpy as np
from hw3_jmschroeder_support_functions import square
#imports the function named 'square' from the hw3_jschroeder_support_functions.py file

test_square_1 = np.arange(10)
print( square(test_square_1) )
#testing that this does what I want it to, that be squaring an array of values

test_square_2 = np.arange( 25, dtype=float).reshape(5, 5) 
print( square(test_square_2) )


# In[ ]:





# In[ ]:




