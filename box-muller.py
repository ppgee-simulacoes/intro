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

================================================================
= GENERATE PSEUDO-RANDOM NUMBERS FOR BOX-MULLER TRANSFORMATION =
================================================================
"""

import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import os

seed = 10 # seed
size = 1000 # number of samples
mu = 0  # mean of distribution
sigma = 1  # standard deviation of distribution
num_bins = 50 # number of bins

# function for Box-Muller Transformation
def box_muller(u1, u2):
    z1 = np.sqrt(-2*np.log(u1))*np.cos(2*np.pi*u2)
    z2 = np.sqrt(-2*np.log(u1))*np.sin(2*np.pi*u2)
    return z1,z2

np.random.seed(seed) # Define a seed

rnd = np.random.rand(2, size) # Generate a matrix with 2 rows and "size" collumns of pseudo-random numbers
u1 = rnd[0,:] # vector "row 1" with all collumns
u2 = rnd[1,:] # vector "row 2" with all collumns

z1, z2 = box_muller(u1,u2) # Result of Box-Muller Transformation

fig, ax = plt.subplots() # Create fig

# the histogram of the data
n, bins, patches = ax.hist((z1,z2), num_bins, normed='1', label=('$Z_{1}$', '$Z_{2}$'))

# add a 'best fit' line - PDF
y = mlab.normpdf(bins, mu, sigma) # PDF for Normal Distribution
ax.plot(bins, y, '--', color="black", label='PDF') # Plot y
ax.set_xlabel('Value of sample') # xlabel
ax.set_ylabel('Probability density') # ylabel
ax.set_title(r"Histogram of the samples of Box-Muller Transformation" "\n" r"$\mu=0$, $\sigma=1$, Number of samples = %d" % (size)) # Tittle
ax.legend(loc='upper right') # Show legend at upper right location

fig.tight_layout() # Tweak spacing to prevent clipping of ylabel

dir = 'box-muller_output' # directory to save graphs
if not os.path.isdir(dir): os.makedirs(dir) # if "dir" not exists, create him
filename = os.path.join(dir, "PDF_histogram.png") # Relative path
plt.savefig(filename) # Save graphic
 
plt.show() # Show graphic

plt.close(fig) # Close fig