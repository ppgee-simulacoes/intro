# -*- coding: utf-8 -*-
"""
Channel class, which implements three different channel models.

TODO Implement constant channel
TODO Implement Markov channel

Created on Mon Mar 27 09:16:52 2017

@author: Calil
"""

import numpy as np

from support import ChannelModel

class Channel(object):
    def __init__(self,model,seed):
        self.__model = model
        self.__seed = seed
        self.__rnd_state = np.random.RandomState(seed)
        
    def get_model(self):
        return self.__model
    
    def get_seed(self):
        return self.__seed
    
    def fade(self,pck):
        if self.get_model() == ChannelModel.IDEAL:
            return self.fade_ideal(pck)
        elif self.get_model() == ChannelModel.CONSTANT:
            return self.fade_constant(pck)
        elif self.get_model() == ChannelModel.MARKOV:
            return self.fade_markov(pck)
        else:
            return NotImplementedError
        
    def fade_ideal(self,pck_Tx):
        pck_Rx = np.array(pck_Tx,copy = True)
        return pck_Rx
    
    def fade_constant(self,pck_Tx):
        return NotImplementedError
    
    def fade_markov(self,pck_Tx):
        return NotImplementedError