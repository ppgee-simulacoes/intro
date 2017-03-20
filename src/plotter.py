# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 09:44:21 2017

@author: Calil
"""

import numpy as np
import matplotlib.pyplot as plt

class Plotter(object):
    
    def __init__(self, num_samples):
        self.__num_samples = num_samples
        
    def get_num_samples(self):
        return self.__num_samples
    
    def plot_uniform(self):
        x = np.arange(0,1.1,0.1)
        y = 0.5*np.ones(np.size(x))
        plt.plot(x,y)
        plt.axis([0, 1, 0, 1])
        plt.savefig("../figs/uniform_pdf.png")
        
    def plot_histogram(self):
        pass
        