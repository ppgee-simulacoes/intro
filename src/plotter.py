# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 09:44:21 2017

@author: Calil
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

from distribution import Distribution

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
    
    def plot_dist(self, arr,dist):
        # PLOT PDF FIRST
        fig = plt.figure(figsize=(10,10))
        ax1 = fig.add_subplot(211)
                
        #Plot histogram
        n, bins, patches = ax1.hist(arr,self.get_num_bins(), normed = 1)
        
        #Distribution specific variables
        if dist == Distribution.UNIFORM:
            y_pdf = np.ones(np.size(bins))
            
            y_cdf = bins
            
            title = "Uniform distribution with "
            file_name = self.get_dir_name() + "uniform_" 
        elif dist == Distribution.NORMAL:
            mu = 0
            sigma = 1
            y_pdf = mlab.normpdf(bins,mu,sigma)
            
            c_sum = np.cumsum(y_pdf)
            y_cdf = c_sum/np.amax(c_sum)
            
            title = "Normal distribution with "
            file_name = self.get_dir_name() + "normal_" 
        elif dist == Distribution.TRIANGLE:
            y_pdf = 0.02*bins
            
            y_cdf = 0.01*bins**2
            
            title = "Triangular distribution with "
            file_name = self.get_dir_name() + "triangular_" 
        else:
            pass
        
        # Append extra text to strings
        title = title + str(self.get_num_samples()) + " samples"
        file_name = file_name + str(self.get_num_samples()) + ".png"
        
        #Plot PDF theoretical valeue
        ax1.plot(bins,y_pdf,'r',linewidth = 0.5)
        
        #General plot configurations
        ax1.set_xlabel("Value")
        ax1.set_ylabel("Probability density")
        ax1.set_title(title)
        
        #Add CDF subplot
        ax2 = fig.add_subplot(212,sharex=ax1)
        
        #Plot cumulative histogram
        n, bins, patches = ax2.hist(arr,self.get_num_bins(), normed = 1,
                                    histtype = 'step', cumulative = True,
                                    label = 'Pseudo-random')
        
        #Plot uniform CDF theoretical valeue
        ax2.plot(bins,y_cdf,'r',linewidth = 0.5)
        
        #General plot configurations
        ax2.set_xlabel("Value")
        ax2.set_ylabel("Cumulative probability \n density")
        
        #Save and show
        plt.savefig(file_name)
        plt.show()
        