#!/usr/bin/env python
# coding: utf-8

# In[18]:


#Jay Schroeder
#Oct 11th, 2026
#Homework 7


# In[79]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import curve_fit


# In[80]:


print( 'Problem Three' )

#reads the transit data provided
data = pd.read_csv( 'hw7_synthetic_transit_lightcurve.csv' )

#defining the columns of the data
time = data['Time (days)']
flux = data['Normalized Flux']

#building the plot and formating to make it publication ready
fig, ax = plt.subplots( figsize=(8,5) )

ax.scatter( time, flux, marker='.' )
ax.set_xlabel( 'Time (days)', fontsize=12 )
ax.set_ylabel( 'Normalized Flux', fontsize=12 )
ax.set_title( 'Transit Light Curve of an Exoplanet', fontsize=12 )
ax.tick_params( direction='in', top=True, right=True )

fig.tight_layout()
plt.show()


# In[81]:


#function for the box window of this graph
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
    '''

    x = np.asarray(x)
    window = np.zeros(x.shape)
    window[ np.abs(x - center) <= width / 2 ] = height

    return window


# In[82]:


#initial guess of transit parameters
center_guess = (time[in_transit].min() + time[in_transit].max()) / 2
height_guess = flux.min() - 1
width_guess = time[in_transit].max() - time[in_transit].min()
p0 = [center_guess, width_guess, height_guess]

print('Initial guesses:', p0)

#fitting the box function to the data and extracting the best-fit parameter
popt, pcov = curve_fit( box_function, time, flux - 1, p0=p0, bounds=( [-0.05, 0.005, -0.011], [0.01, 0.04, 0.0] ) )
center_fit, width_fit, height_fit = popt

transit_depth = -height_fit
print('Transit depth:', transit_depth)

#calculating the planet's radius and fitting this to the model
fig, ax = plt.subplots( figsize=(8,5) )

model = 1 + box_function(time, *popt)

#plotting the data and the model
ax.scatter( time, flux, marker='.' )
ax.plot( time, model, color='black', linewidth=2, label='Best-fit box model' )

ax.set_xlabel( 'Time (days)', fontsize=12 )
ax.set_ylabel( 'Normalized Flux', fontsize=12 )
ax.set_title( 'Transit Light Curve of an Exoplanet', fontsize=12 )
ax.tick_params( direction='in', top=True, right=True )
ax.set_ylim(0.985, 1.005)

fig.tight_layout()
plt.show()

print('Center:', center_fit)
print('Width:', width_fit)
print('Height:', height_fit)
print('Fitted parameters:', popt)
print('Box model range:',
      box_function(time, *popt).min(),
      box_function(time, *popt).max())


# In[83]:


#Problem 3, part bii and biii
''' This fit is hard to believe since the lower bounds do not actually lie within 
    the data. Since the rectangular window function is discontinuous, curve_fit()
    not be the right right approach given the center and width. I could try a
    different initial guess or use an alternative fitting approach to check the
    parameters.
'''

''' The bes-fit window-function properties are the center at t = 0.00days, the width at 
    w = 0.01984days, the height at h = -0.01088, and the transit depth is 0.01088. The
    radius of the exoplanet can be found by using the formula for transit depth, giving
    us R_p = (R_*)*sqrt(deltaF/F) which is roughly equal to 0.119R_sun.
'''


# In[84]:


print( 'Problem Four' )

#setting variables to calulate the error in teh planetary radius
R_star = 1.14
sig_R_star = 0.01

depth = transit_depth
sig_depth = 0.002
R_planet = R_star * np.sqrt(depth)

#calculating the planetary radius and the error of this value before 
#printing the found values
term_star = np.sqrt(depth) * sig_R_star
term_depth = ( R_star / (2 * np.sqrt(depth)) ) * sig_depth

sig_R_planet = np.sqrt( term_star**2 + term_depth**2 )

print( 'Planetary Radius:', R_planet, 'R_sun' )
print( 'Total Radius Uncertainty:', sig_R_planet, 'R_sun' )
print(f"Result: ({R_planet:.3f} ± {sig_R_planet:.3f}) R_sun")


# In[ ]:




