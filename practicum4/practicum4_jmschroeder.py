#!/usr/bin/env python
# coding: utf-8

# In[16]:


#Jay Schroeder
#Oct 4th, 2026
#Practicum 4


# In[17]:


import numpy as np
from astropy.io import fits
import os


# In[18]:


#assigning file directory to variable 'datadir' and file type to variable 'fext' 
#as to not hardcode this program
datadir = 'hw6_data/'
fext = '.fits'


# In[19]:


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

print('Data Directory: ', datadir)
print('FITS Extension: ', fext)
print('Last Object File: ', objfile[-1])
print('Last Dark File: ', darkfile[-1])


# In[15]:


#assembles the file, attributes the data of the completed file to variable 'data',
#and calls its shape
filename = datadir + objfile[0] + fext
data = fits.getdata( filename )
ny, nx = data.shape

#calls the length of files and assigns to variables 'nobj' and 'ndark'
nobj = len( objfile )
ndark = len( darkfile )

print( 'Number of Pixels y: ', ny )
print( 'Number of Pixels x: ', nx )
print( 'Number of Object Files: ', nobj )
print( 'Number of Dark Files: ', ndark )


# In[21]:


# creates 3D arrays from 'nobj' and 'ndark' and attributes them to variables 
#'objcube' and 'darkcube' before printing them
objcube = np.zeros( (nobj, ny, nx), dtype=np.float64 )
darkcube = np.zeros( (ndark, ny, nx), dtype=np.float64 )

print( 'Object Cube Shape: ', objcube.shape )
print( 'Dark Cube Shape: ', darkcube.shape )

#assembles file names from lists 'objfile and 'darkfile', assigns them
#to variable 'filename', and then reads the data header
for i in range(nobj): 
    filename = datadir + objfile[i] + fext
    objcube[i], objhead = fits.getdata( filename, header=True )

for i in range(ndark): 
    filename = datadir + darkfile[i] + fext
    darkcube[i], darkhead = fits.getdata( filename, header=True )

#prints the date on which observations were made from object files and dark files
print( 'Object DATE-OBS: ', objhead['DATE-OBS'])
print( 'Dark DATE-OBS: ', darkhead['DATE-OBS'])


# In[ ]:


''' The reason we don't print TIME-OBS is most likely because it is not guaranteed that 
    there is a time present in the header of file. It could also be an issue of redundancy, 
    where some data may include a time in the header, in which case printing TIME-OBS would
    be largely pointless. '''

