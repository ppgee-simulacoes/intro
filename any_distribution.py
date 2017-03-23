#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Copyright (c) <2017> <Eduardo Gonçalves Sousa>

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

======================================================================
= GENERATE PSEUDO-RANDOM NUMBERS FOR GENERAL CASE (ANY DISTRIBUTION) =
======================================================================
"""
from scipy import interpolate
import numpy as np
import matplotlib.pyplot as plt
import os

step_size = 0.05
seed = 10 # seed
size = 10000
bins = 50

# Function to remove negative elements due to the spline interpolation
def zero_negative_x(old_list):
    new_list = []
    for num in old_list:
        if num < 0:
             new_list.append(0)
        else:
            new_list.append(num)
    return new_list

# probability density function is based on this data
#probabilities = [0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0]
probabilities = [0, 1, 10, 2, 0, 0, 4, 5, 3, 1, 0]
x = np.linspace(1,len(probabilities),len(probabilities),endpoint=True)

# do spline interpolation for smoothing
xq = np.linspace(1,len(probabilities),((len(probabilities)-1)/step_size)+1,endpoint=True)
pdf = interpolate.interp1d(x, probabilities, 'cubic')

# remove negative elements due to the spline interpolation
yi=zero_negative_x(pdf(xq))

# normalize the function to have an area of 1.0 under it
pdf = yi/np.sum(yi)

# Plot PDF
fig, ax = plt.subplots() # Create fig
ax.plot(xq,pdf, label='Ideal PDF')
ax.set_xlabel('Value of sample') # xlabel
ax.set_ylabel('Probability density') # ylabel
ax.set_title(r"PDF") # Tittle
ax.legend(loc='upper right') # Show legend at upper right location

fig.tight_layout() # Tweak spacing to prevent clipping of ylabel

dir = 'any_distribution_output' # directory to save graphs
if not os.path.isdir(dir): os.makedirs(dir) # if "dir" not exists, create him
filename = os.path.join(dir, "Ideal_PDF.png") # Relative path
plt.savefig(filename) # Save graphic

plt.show() # Show graphic
plt.close(fig) # Close fig

# the integral of PDF is the cumulative distribution function
cdf = np.cumsum(pdf)

# Plot CDF
fig, ax = plt.subplots() # Create fig
ax.plot(xq,cdf, label='Ideal CDF')
ax.set_xlabel('Value of sample') # xlabel
ax.set_ylabel('Probability') # ylabel
ax.set_title(r"CDF") # Tittle
ax.legend(loc='upper right') # Show legend at upper right location

fig.tight_layout() # Tweak spacing to prevent clipping of ylabel

dir = 'any_distribution_output' # directory to save graphs
if not os.path.isdir(dir): os.makedirs(dir) # if "dir" not exists, create him
filename = os.path.join(dir, "Ideal_CDF.png") # Relative path
plt.savefig(filename) # Save graphic

plt.show() # Show graphic
plt.close(fig) # Close fig

# remove non-unique elements
cdf, mask = np.unique(cdf, return_index=True)

# create an array of "size" random numbers
np.random.seed(seed) # Define a seed
rnd = np.random.rand(size,1)

# inverse interpolation to achieve P(x) -> x projection of the random values
sub = len(xq)-len(cdf)
xq = xq[:-sub]
projection = interpolate.interp1d(cdf, xq, 'cubic')
yi=projection(rnd)

# Plot PDF histogram
fig, ax = plt.subplots() # Create fig
plt.hist(yi, bins, normed=1, label='PDF')
ax.set_xlabel('Value of sample') # xlabel
ax.set_ylabel('Probability density') # ylabel
ax.set_title(r"PDF") # Tittle
ax.legend(loc='upper right') # Show legend at upper right location

fig.tight_layout() # Tweak spacing to prevent clipping of ylabel

dir = 'any_distribution_output' # directory to save graphs
if not os.path.isdir(dir): os.makedirs(dir) # if "dir" not exists, create him
filename = os.path.join(dir, "PDF_Histogram.png") # Relative path
plt.savefig(filename) # Save graphic

plt.show() # Show graphic
plt.close(fig) # Close fig
