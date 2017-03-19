# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 16:33:54 2017

@author: Calil
"""

#import numpy as np
#import math

class GenerateRandom(object):
    
    def __init__(self):
        self.__seed = 0
        self.__num_samples = 0
        
    def get_seed(self):
        return self.__seed
    
    def get_num_samples(self):
        return self.__num_samples
        