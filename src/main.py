# -*- coding: utf-8 -*-
"""
Main script.

Created on Sun Mar 19 14:46:39 2017

@author: Calil
"""

from random_generator import RandomGenerator
from plotter import Plotter

seed = 10
num_samples = [100, 1000, 10000]
num_bins = 50
figs_dir = "figs/"

print("\n\n\nInitializing...")
print("\nSeed = ", seed)
print(num_bins," bins")

for sd in range(0,len(num_samples)):
    print("\nNumber of samples = ", num_samples[sd])

    rnd_gen = RandomGenerator(seed,num_samples[sd])
    pltr = Plotter(num_samples[sd],num_bins,figs_dir)
    
    uni_samples = rnd_gen.uniform()
    pltr.plot_uniform(uni_samples)