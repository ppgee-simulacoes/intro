# -*- coding: utf-8 -*-
"""
Theoretical results class.

Created on Sun Apr  2 11:16:43 2017

@author: Calil
"""

import numpy as np
from support.enumerations import ChannelModel
from parameters.parameters import Parameters

class Theoretical(object):
    
    def __init__(self,param):
        """
        Constructor method. Initializes atrributes:
            self.__param -- parameters object
            self.__state_ps -- state probabilities for Markov channel
        
        Keyword parameters:
            param -- parameters object
        """
        self.__param = param
        if param.chan_mod == ChannelModel.MARKOV:
            self.__state_ps = self.markov_solve()
        else:
            self.__state_ps = np.array([])
        
    def validate(self):
        """
        Calculates theoretical BER, PER and Throughput according to channel 
        model.
        
        Returns:
            ber_mean -- theoretical mean value of BER
            per_mean -- theoretical mean value of PER
            thrpt_mean -- theoretical mean value of Throughput
        """
        if self.get_param().chan_mod == ChannelModel.IDEAL:
            ber_mean, per_mean, thrpt_mean = self.validate_ideal()
        elif self.get_param().chan_mod == ChannelModel.CONSTANT:
            ber_mean, per_mean, thrpt_mean = self.validate_constant()
        elif self.get_param().chan_mod == ChannelModel.MARKOV:
            ber_mean, per_mean, thrpt_mean = self.validate_markov()
        else:
            raise NameError('Unknown channel model!')
            
        return ber_mean, per_mean, thrpt_mean
      
    def get_param(self): 
        """Getter for Parameters object."""
        return self.__param
    
    def get_state_ps(self):
        """Getter for state probabilities."""
        return self.__state_ps
    
    def validate_ideal(self):
        """
        Calculates theoretical BER, PER and Throughput for ideal channel.
        
        Returns:
            ber_mean -- theoretical mean value of BER
            per_mean -- theoretical mean value of PER
            thrpt_mean -- theoretical mean value of Throughput
        """
        ber_mean = np.zeros(np.size(self.get_param().p))
        per_mean = np.zeros(np.size(self.get_param().p))
        thrpt_mean = self.get_param().tx_rate*\
            np.ones(np.size(self.get_param().p))
        return ber_mean, per_mean, thrpt_mean
    
    def validate_constant(self):
        """
        Calculates theoretical BER, PER and Throughput for constant channel.
        
        Returns:
            ber_mean -- theoretical mean value of BER
            per_mean -- theoretical mean value of PER
            thrpt_mean -- theoretical mean value of Throughput
        """
        raise NotImplementedError
    
    def validate_markov(self):
        """
        Calculates theoretical BER, PER and Throughput for Markov channel.
        
        Returns:
            ber_mean -- theoretical mean value of BER
            per_mean -- theoretical mean value of PER
            thrpt_mean -- theoretical mean value of Throughput
        """
        raise NotImplementedError
        
        
    def markov_solve(self):
        """
        Solves the matrix equation to find Markov chain's steady state
        probabilities.
        
        Returns:
            state_probs -- numpy array of state probabilities
        """
        raise NotImplementedError