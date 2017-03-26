# -*- coding: utf-8 -*-
"""
Source class: crates packets and checks for bit and packet errors.

Created on Sun Mar 26 10:00:08 2017

@author: Calil
"""

import numpy as np

class Source(object):
    def __init__(self,n_bits,seed):
           
        self.__n_bits = n_bits
        self.__seed = seed
        self.__rnd_state = np.random.RandomState(seed)
        self.__last_pck = np.zeros([1,n_bits])
    
    def get_n_bits(self):
        return self.__n_bits
    
    def get_seed(self):
        return self.__seed
    
    def get_last_pck(self):
        return self.__last_pck
    
    def get_rnd_state(self):
        return self.__rnd_state
    
    def generate_packet(self):
        pck = self.get_rnd_state().randint(2,\
                                            size=self.get_n_bits())
        # Last packet is a copy of sent packet, for further comparison
        self.__last_pck = np.array(pck,copy = True)

        return pck
    
    def calculate_error(self,pck):
        n_errors = np.sum(pck != self.get_last_pck())
        pck_error = (n_errors != 0)
        
        return n_errors, pck_error