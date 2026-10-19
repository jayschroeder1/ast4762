#!/usr/bin/env python
# coding: utf-8

# In[9]:


#Jay Schroeder
#Oct 17th, 2026
#Practicum 5
import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits


# In[3]:


print( 'Problem One' )
#copying all of the routines from hw7_jmschroeder into this file
#this is the FIXED version of the file
from hw7_jmschroeder import *


# In[5]:


print( 'Problem Two' )
#I built the function 'normmedcomb()' in a separate file called 
#'p5_jmschroeder_support_functions.py'
from p5_jmschroeder_support_functions import normmedcomb


# In[27]:


print( 'Problem Three' )

skydata, skyhead = fits.getdata( 'hw6_jmschroeder_prob2_graph1.fits', header=True)

skymednorm, normfactor = normmedcomb( skydata, normreg=((225, 225), (-225, -225)) )
print(normfactor)

skyhead['HISTORY'] = "Normalized, Median-Combined Sky Image"

fits.writeto( 'sky_13s_mednorm.fits', skymednorm, skyhead, overwrite=True )


# In[ ]:





# In[ ]:





# In[ ]:




