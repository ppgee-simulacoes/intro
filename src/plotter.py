# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 09:44:21 2017

@author: Calil
"""

import numpy as np
import matplotlib.pyplot as plt

class Plotter(object):
    
    def __init__(self, num_samples,num_bins, dir_name):
        self.__num_samples = num_samples
        self.__num_bins = num_bins
        self.__dir_name = dir_name
        
    def get_num_samples(self):
        return self.__num_samples
    
    def get_num_bins(self):
        return self.__num_bins
    
    def get_dir_name(self):
        return self.__dir_name
    
    def plot_uniform(self, arr):
        # PLOT PDF FIRST
        fig = plt.figure(figsize=(10,10))
        ax1 = fig.add_subplot(211)
                
        #Plot histogram
        n, bins, patches = ax1.hist(arr,self.get_num_bins(), normed = 1)
        
        #Plot uniform PDF theoretical valeue
        x = np.arange(0,self.get_num_samples(),1)/self.get_num_samples()
        y = np.ones(np.size(x))
        ax1.plot(x,y,'r',linewidth = 0.5)
        
        #General plot configurations
        ax1.set_xlabel("Value")
        ax1.set_ylabel("Probability density")
        ax1.set_title("Uniform distribution with " + \
                      str(self.get_num_samples()) + \
                     " samples")
        
        #THEN PLOT CDF
        ax2 = fig.add_subplot(212,sharex=ax1)
        
        #Plot cumulative histogram
        n, bins, patches = ax2.hist(arr,self.get_num_bins(), normed = 1,
                                    histtype = 'step', cumulative = True,
                                    label = 'Pseudo-random')
        #Plot uniform PDF theoretical valeue
        ax2.plot(x,x,'r',linewidth = 0.5)
        
        #General plot configurations
        ax2.set_xlabel("Value")
        ax2.set_ylabel("Cumulative probability \n density")
        
        #Save and show
        file_name = self.get_dir_name() + "uniform_" \
                     + str(self.get_num_samples()) + ".png"
        plt.savefig(file_name)
        plt.show()
    
    def plot_normal(self, arr):
        pass
    
    def plot_triangle(self,arr):
        pass
        