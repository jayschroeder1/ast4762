#!/usr/bin/env python
# coding: utf-8

# In[96]:


#Jay Schroeder
#Practicum 2
#Sep 21, 2026

import numpy as np
import matplotlib.pyplot as plt

print( 'Problem One' )

#assigns values for mu, sigma, and N
mu = 55 
sig = 13
N = 10

#calls numpy's random.normal() function to generate vaules from the Gaussian distribution and
#assigns it to variable 'samples'
samples = np.random.normal(mu, sig, N)
print(samples)


# In[75]:


print( 'Problem Two' )

#list of outputs
output = []

#loops 10 times to pull N=10 random, creating a new sample each time. solves for the mean and 
#standard deviation of each pull and added it to list 'output'
for i in range(10): 
    samples = ( np.random.normal(mu, sig, N), )
    mean = np.mean(np.round(samples) )
    stdv = np.std( np.round(samples) )
    output.append( [i, mean, stdv] )

#orders 'output' into an arrary before rounding it to 2 decimal places
output = np.array(output)
rounded = np.round( output, decimals=2 )

print(rounded)


# In[76]:


print( 'Problem Four' )

#writes a file and comments it appropriately
with open( "practicum2_jmschroeder_outputarray.txt", "w" ) as file:
    file.write( "#there are 10 draws in this table\n" )
    for item in rounded:
        file.write(f"{item}\n")


# In[77]:


Ns = [100, 1000, 10000, 100000, 1000000]

#loop that will be make N = 100, 1,000, 100,000, and 1,000,000 draws
for N in Ns:
    output = []

#loop that will calculate the mean and stdev of each walue N, before appending an array into the file
#"practicum2_jmschroeder_outputarray.txt"
    for i in range(10): 
        samples = ( np.random.normal(mu, sig, N), )
        mean = np.mean(np.round(samples) )
        stdv = np.std( np.round(samples) )
        output.append( [i, mean, stdv] )

    output = np.array(output)
    final = np.round( output, decimals=2 )
    print(final)


    with open( "practicum2_jmschroeder_outputarray.txt", "a" ) as file:
        file.write( f"#there {N} are draws in this table\n" )
        for item in final:
            file.write(f"{item}\n")

print( "Done" )


# In[94]:


print( 'Problem Six' )

#remakes the list of draws to include n = 10
Ns = [10, 100, 1000, 10000, 100000, 1000000]

#opens .txt file and appends with table title
with open( "practicum2_jmschroeder_outputarray.txt", "a" ) as file:
    file.write( "#Sample size   Std. dev. of mean\n" )

#pulls the second column of all arrays within the .txt and groups them into array 'groups' as lists
k = 10

mean_col = np.loadtxt( "practicum2_jmschroeder_outputarray.txt", usecols=[2], unpack=True )
groups = [mean_col[i: i + k]for i in range( 0, len(mean_col), k )]
groups = np.array(groups)

#creates new list 'means' which takes the means of 'groups' and appends them to a new array
means = []

for k in groups:
    stdv_mean = np.std(k)
    means.append(np.round(stdv_mean, decimals=2))
means = np.array(means)

print( "#Sample size   Std. dev. of mean" )
for N, item in zip(Ns, means):
        print(f"{N:<10}     {item:<20}")

#appends .txt file to include the sample size and standard deviation of the means from array 'means'
with open( "practicum2_jmschroeder_outputarray.txt", "a" ) as file:
    for N, item in zip(Ns, means):
        file.write(f"{N:<10}     {item:<20}\n")


# In[97]:


print( 'Problem Seven' )

#creates a log-log plot of std. dev of mean vs sample size, before saving it as a png
plt.loglog(Ns, means)
plt.xlabel( "Sample size (N)" )
plt.ylabel( "Std. dev of mean (sigma)" )
plt.title( "Std. Dev. of Mean vs Sample Size" )

plt.savefig( "practicum2_jmschroeder_problem7_loglogplot.png", dpi = 300 )
plt.show()


# In[ ]:




