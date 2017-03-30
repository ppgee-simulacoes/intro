# -*- coding: utf-8 -*-
"""
Channel class, which implements three different channel models.

TODO Implement constant channel
TODO Implement Markov channel

Created on Mon Mar 27 09:16:52 2017

@author: Calil
"""

import numpy as np

from src.support.enumerations import ChannelModel

class Channel(object):
    
    def __init__(self,model,seed):
        """
        Class constructor.
        
        Keyword arguments:
            model -- channel model (IDEAL, CONSTANT or MARKOV)
            seed -- seed for random number generator
        """
        self.__model = model
        self.__seed = seed
        self.__rnd_state = np.random.RandomState(seed)
        
    def get_model(self):
        """Returns channel model."""
        return self.__model
    
    def set_seed(self,seed):
        """Set new seed."""
        self.__seed = seed
    
    def get_seed(self):
        """Returns random number generator seed."""
        return self.__seed
    
    def fade(self,pck_Tx):
        """
        Applies fade to packet according to channel model, 
        introducing bit errors.
        
        Keyword arguments:
            pck_Tx -- transmitted packet
            
        Returns:
            pck_Rx -- received packet
        """
        if self.get_model() == ChannelModel.IDEAL:
            return self.__fade_ideal(pck_Tx)
        elif self.get_model() == ChannelModel.CONSTANT:
            return self.__fade_constant(pck_Tx)
        elif self.get_model() == ChannelModel.MARKOV:
            return self.__fade_markov(pck_Tx)
        else:
            raise NameError('Unknown channel model!')
        
    def __fade_ideal(self,pck_Tx):
        """
        Ideal channel, just returns a copy of transmitted packet
        
        Keyword arguments:
            pck_Tx -- transmitted packet
            
        Returns:
            pck_Rx -- received packet, a copy of pck_Tx
        """
        pck_Rx = np.array(pck_Tx,copy = True)
        return pck_Rx
    
    def __fade_constant(self,pck_Tx):
        """
        Constant channel, with a constant BER.
        
        Keyword arguments:
            pck_Tx -- transmitted packet
            
        Returns:
            pck_Rx -- received packet
        """
        raise NotImplementedError
    
    def __fade_markov(self,pck_Tx):
        """
        Markov chain modeled channel, BER changes for each packet.
        
        Keyword arguments:
            pck_Tx -- transmitted packet
            
        Returns:
            pck_Rx -- received packet
        """
        raise NotImplementedError