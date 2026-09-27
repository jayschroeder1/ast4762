#!/usr/bin/env python
# coding: utf-8

# In[29]:


#Jay Schroeder
#Sep 25th, 2025
#Practicum Three

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

print( 'Problem One-a' )

with open( "practicum3_1.dat", "r" ) as file:
    content = file.read()
    print(content)


# In[30]:


#data = np.genfromtxt('practicum3_1.dat')

#model_1 = data[0:len(data)//2]
#model_2 = data[len(data)//2:len(data)+1]

#this works too, this is a method a classmate used


# In[44]:


print( 'Problem One-b' )
import linfit

#uncertainty given in the procedure
y_unc = 0.5

#imports the data from Model 1; I had to look in the file to determine the number of columns, but I recognize
#that there is a way to do this without looking into the file
x_mod1, fx_mod1 = np.loadtxt( 'practicum3_1.dat', skiprows=2, max_rows=100, unpack=True)
#read csv from pandas also works here 

#calls linfit and establishes its parameters
a, b, a_unc, b_unc, chisq, prob, covar, yfit = linfit.linfit( fx_mod1, x_mod1, y_unc )
print( f"{a},{a_unc},{b},{b_unc},{chisq},{prob}" )

#plots the data and fit, before saving as a .PNG file
plt.figure( figsize=(8,5) )
plt.plot( x_mod1, fx_mod1, "o" )
plt.plot( x_mod1, yfit )
plt.xlabel( "x" )
plt.ylabel( "f(x)" )
plt.title( "Linear Fit of f(x) vs x for Model 1" )

plt.savefig( "practicum3_jmschroeder_problem1c_model1plot.png", dpi = 300 )
plt.show()

#docstring answering questions
''' Having an uncertainty of y = 0.5 is important because this determines the uncertainties of the fitted
    parameters a and b and the chi squared value of our uncertainty. The fit would change from 0.2 to 0.9
    by creating smaller or larger uncertainties in our analysis, but it does not change how the data is
    weighted, and thus the fits between these uncertainties are essentially identitical. The fitted 
    parameters for this model are 'a' and 'b', both with their respected values of uncertainty. From this,
    we can see that the parameters are within 3sigma of the parameters of the true line. '''


# In[33]:


print( 'Problem One-c' )

''' The probability that I would get a higher chi squared value is about 84.4% by chance, 
    assuming the data came from a fitted model with some stated random error '''


# In[45]:


print( 'Problem One-d' )
import linfit

#uncertainty given in the procedure
y_unc = 0.5

#imports the data from Model 
x_mod2, fx_mod2 = np.loadtxt( 'practicum3_1.dat', skiprows=105, max_rows=100, unpack=True)

#calls linfit and establishes its parameters
a, b, a_unc, b_unc, chisq, prob, covar, yfit = linfit.linfit( fx_mod2, x_mod2, y_unc )
print( f"{a},{a_unc},{b},{b_unc},{chisq},{prob}" )

#plots the data and fit; notice how this fit does not match
plt.figure( figsize=(8,5) )
plt.plot( x_mod2, fx_mod2, "o" )
plt.plot( x_mod1, yfit )
plt.xlabel( "x" )
plt.ylabel( "f(x)" )
plt.title( "Linear Fit of f(x) vs x for Model 2" )

plt.savefig( "practicum3_jmschroeder_problem1d_model2plot.png", dpi = 300 )
plt.show()

''' Here, having an uncertainty of y = 0.5 is important for the same reason as the previous model,
    it determines the uncertainties of the fitted parameters a and b and the chi squared value of 
    our uncertainty. The fitted values do not change much for a y_unc = 0.2 or 0.9, however their
    uncertainties do still change. The linear model does not fit the data at all. Consider first the
    probability that ther is a worse fit from this is zero; there is no fit worse than this. Secondly
    regard the absurdly large chi squared value, a value which indicates minimal correlation. From this, 
    we can determine that the parameters are not within 3sigma of uncertainty. To create a better fit, I
    should use a quadratic equation to model the data. '''


# In[ ]:




