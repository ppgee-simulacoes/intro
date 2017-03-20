# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 16:33:54 2017

@author: Calil
"""

import numpy as np
#import math

class RandomGenerator(object):
    
    def __init__(self, seed, num_samples):
        self.__seed = seed
        self.__num_samples = num_samples
        self.__rnd_state = np.random.RandomState(seed)
        
    def get_seed(self):
        return self.__seed
    
    def get_num_samples(self):
        return self.__num_samples
    
    def uniform(self):
        return self.__rnd_state.rand(self.get_num_samples(),1)
    
    def normal(self):
        pass
    
    def triangle(self):
        pass