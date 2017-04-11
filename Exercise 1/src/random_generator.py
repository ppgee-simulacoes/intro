# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 16:33:54 2017

@author: Calil
"""

import numpy as np
import math

class RandomGenerator(object):
    
    def __init__(self, seed, num_samples):
        self.__seed = seed
        self.__num_samples = num_samples
        self.__rnd_state = np.random.RandomState(seed)
        
    def get_seed(self):
        return self.__seed
    
    def get_num_samples(self):
        return self.__num_samples
    
    def get_rnd_state(self):
        return self.__rnd_state
    
    def uniform(self):
        return self.get_rnd_state().rand(self.get_num_samples(),1)
    
    def normal(self):
        """
        Uses the Box-Muller transform to generate normal distributed
        random numbers.
        
        Returns
        -------
            z1: Normal (Gausian) distributed numpy array
        """
        
        u1 = self.uniform()
        u2 = self.uniform()
        
        z1 = np.sqrt(-2*np.log(u1))*np.cos(2*math.pi*u2)
        return z1
    
    def triangle(self):
        """
        Uses the inverse CDF to generate triangular random distribution
        with PDF:
            
           f(x) = 
               0.02*x, 0 < x < 10
               0     , otherwise
        
        Returns
        -------
            t1: Triangle distributed numpy array
        """
        u1 = self.uniform()
        t1 = np.sqrt(u1/0.01)
        return t1