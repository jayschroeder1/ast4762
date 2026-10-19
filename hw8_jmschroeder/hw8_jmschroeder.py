#!/usr/bin/env python
# coding: utf-8

# In[13]:


#Jay Schroeder
#Oct 18th, 2026
#Homework 8
import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits


# In[14]:


print( 'Problem One' )
#including the solutions from Practicum 5
#copying all of the routines from hw7_jmschroeder into this file
#this is the FIXED version of the file
from hw7_jmschroeder import *

#I built the function 'normmedcomb()' in a separate file called 
#'hw8_jmschroeder_support_functions.py'
from hw8_jmschroeder_support_functions import normmedcomb

skydata, skyhead = fits.getdata( 'hw6_jmschroeder_prob2_graph1.fits', header=True)

skymednorm, normfactor = normmedcomb( skydata, normreg=((225, 225), (-225, -225)) )
print(normfactor)

skyhead['HISTORY'] = "Normalized, Median-Combined Sky Image"

fits.writeto( 'sky_13s_mednorm.fits', skymednorm, skyhead, overwrite=True )



# In[25]:


print( 'Problem Two' )
#importing support function
from hw8_jmschroeder_support_functions import skycormednorm


objcube, objhead = fits.getdata( 'hw6_jmschroeder_prob2_graph1.fits', header=True )   #defining variables for the 3D array and header  
nobj = objcube.shape[0]                                                               #defining variable for the shape of the object cube
skysubcube = np.empty_like(objcube, dtype=float)

for i in range(nobj):
    skysubcube[i] = hw8spf.skycormednorm( objcube[i], skymednorm )     #creates a loop which applies the normalized sky frame

stars_nosky = skysubcube[-1]              #assigns the subtracted array to a variable
print( stars_nosky[217, 184] )            #prints the value of pixel [217, 184]

objhead['HISTORY'] = 'Normalized, Sky-Subtracted Object Frame'                   #adds a history 
fits.writeto( 'stars_13s_9_nosky.fits', stars_nosky, objhead, overwrite=True )   #saves the file as 'stars_13s_9_nosky.fits'



# In[ ]:





# In[ ]:




