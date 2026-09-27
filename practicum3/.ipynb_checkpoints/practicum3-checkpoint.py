#!/usr/bin/env python
# coding: utf-8

# In[48]:


#Jay Schroeder
#Sep 25th, 2025
#Practicum Three

import numpy as np
import matplotlib.pyplot as plt
import linfit


# In[47]:


print( 'Problem One-a' )

#opens file 'practicum3_1.dat" and prints its data
with open( "practicum3_1.dat", "r" ) as file:
    content = file.read()
    print(content)


# In[30]:


#data = np.genfromtxt('practicum3_1.dat')

#model_1 = data[0:len(data)//2]
#model_2 = data[len(data)//2:len(data)+1]

#this works too, this is a method a classmate used


# In[49]:


print( 'Problem One-b' )

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


# In[50]:


print( 'Problem One-c' )

''' The probability that I would get a higher chi squared value is about 84.4% by chance, 
    assuming the data came from a fitted model with some stated random error '''


# In[51]:


print( 'Problem One-d' )

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


# In[62]:


print( 'Problem Two-a' )

#N number of photons
N = 10000

#draws from a poisson distribution for N photons, and a uniform distribution between 0 and 10^6
pix_poi = np.random.poisson( N, 396 )
pix_uni = np.random.uniform( 0, 10**6, 4 )

#concatenates the two samples and perscribes then variable 'sample', before taking the mean and median
#and printing the result
sample = np.concatenate( (pix_poi, pix_uni) )
mean = np.mean(sample)
med = np.median(sample)
print( f"Mean: {mean}", f"Median: {med}" )

#Mean: 15185.417345596668 Median: 10001.0

''' Here, we can see that the median value is closer to N. '''


# In[67]:


print( 'Problem Two-b' )

#standard deviation of 'sample'
sig = np.std(sample)

#creating a mask for this data using a subsample within 5sigma called 'subsample'
subsample = sample[ np.abs(sample - med) <= 5*sig ]
print( f"Standard Deviation: {sig}" )
print( f"Sample Mean: {np.mean(subsample)}, Sample Median: {np.median(subsample)}" )
print( f"Subsample Stardard Deviation: {np.std(subsample)}" )

#Standard Deviation: 57709.69052534049
#Sample Mean: 9981.644272671938, Sample Median: 10007.0
#Subsample Stardard Deviation: 452.76402154480246

''' Here, we can see that the original standard deviation is considerable large due to there existing 
    4 pixels in the data that can have a value up to 10^6. After masking the data, the median and mean
    falls closer to 10000. '''


# In[ ]:




