# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 09:44:21 2017

@author: Calil
"""

import numpy as np
import matplotlib.pyplot as plt

class Plotter(object):
    
    def __init__(self, num_samples,dir_name):
        self.__num_samples = num_samples
        self.__dir_name = dir_name
        
    def get_num_samples(self):
        return self.__num_samples
    
    def get_dir_name(self):
        return self.__dir_name
    
    def plot_uniform_pdf(self, arr):
        num_bins = 50
        fig, ax = plt.subplots()
                
        #Plot histogram
        n, bins, patches = plt.hist(arr,num_bins, normed = 1)
        
        #Plot uniform PDF mean valeue
        x = np.arange(0,self.get_num_samples(),1)/self.get_num_samples()
        y = np.ones(np.size(x))
        ax.plot(x,y,'r',linewidth = 0.5)
        
        #General plot configurations
        ax.set_xlabel("Value")
        ax.set_ylabel("Probability density")
#        plt.axis([0,1,0,1.5])
        
        file_name = (self.get_dir_name() + "uniform_pdf_" 
                     + str(self.get_num_samples()) + ".png")
        plt.savefig(file_name)
        plt.show()
        
    def plot_uniform_cdf(self, arr):
        pass
    
    def plot_normal_pdf(self, arr):
        pass
    
    def plot_normal_cdf(self,arr):
        pass
    
    def plot_triangle_pdf(self,arr):
        pass
    
    def plot_triangle_cdf(self,arr):
        pass
        