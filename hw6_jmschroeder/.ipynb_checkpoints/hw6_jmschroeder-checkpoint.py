#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Jay Schroeder
#Oct 7th, 2026
#Homework 6


# In[4]:


import numpy as np
from astropy.io import fits
import os


# In[16]:


#This is the code from Practicum 4, I am reusing it for this assignment so that everything 
#stays together and works properly
datadir = 'hw6_data/'
fext = '.fits'

#creates lists for object files and dark files
objfile = []
darkfile = []

#looks through a folder ascribed to 'datadir' for files ending in 'fext', assigns them 
#to a list, and before prints the last element of the of the list
for filename in os.listdir(datadir):
    if filename.startswith('rdpharocor_stars_13s_') and filename.endswith(fext):
        objfile.append(filename[:-len(fext)])

    if filename.startswith('rdpharocor_dark_13s_') and filename.endswith(fext):
        darkfile.append(filename[:-len(fext)])

#assembles the file, attributes the data of the completed file to variable 'data',
#and calls its shape
filename = datadir + objfile[0] + fext
data = fits.getdata( filename )
ny, nx = data.shape

#calls the length of files and assigns to variables 'nobj' and 'ndark'
nobj = len( objfile )
ndark = len( darkfile )

# creates 3D arrays from 'nobj' and 'ndark' and attributes them to variables 
#'objcube' and 'darkcube' before printing them
objcube = np.zeros( (nobj, ny, nx), dtype=np.float64 )
darkcube = np.zeros( (ndark, ny, nx), dtype=np.float64 )

#assembles file names from lists 'objfile and 'darkfile', assigns them
#to variable 'filename', and then reads the data header
for i in range(nobj): 
    filename = datadir + objfile[i] + fext
    objcube[i], objhead = fits.getdata( filename, header=True )

for i in range(ndark): 
    filename = datadir + darkfile[i] + fext
    darkcube[i], darkhead = fits.getdata( filename, header=True )

print( 'Object Cube Shape: ', objcube.shape )
print( 'Dark Cube Shape: ', darkcube.shape )


# In[19]:


print( "Problem 2" )

#uses the NumPy function 'median' to median-combine the data and returns a 2D array
darkmed = np.median( darkcube, axis=0 )

#prints the value of pixel index [217, 184]
print( darkmed[217, 184] )

#creates a HISTORY entry to the dark header before writing a file called 'dark_13s_med.fits'
darkhead[ 'HISTORY' ] = 'Median-Combined Dark Frame'
fits.writeto( 'dark_13s_med.fits', darkmed, darkhead, overwrite=True )

#prints the value of pixel index [217, 184] before the dark frame is subtracted
print( 'Before Dark Subtraction: ', objcube[0, 217, 184])

#subtracts the dark frame from 'objectcue', writes it to file 'hw6_jmschroeder_prob2_graph1.fits'
#and prints the the pixel index [217, 184] after the dark frame is subtracted
objsub = objcube - darkmed 
fits.writeto( 'hw6_jmschroeder_prob2_graph1.fits', objsub[0], objhead, overwrite=True )
print( 'After Dark Subtraction: ', objsub[0, 217, 184])


# In[ ]:




