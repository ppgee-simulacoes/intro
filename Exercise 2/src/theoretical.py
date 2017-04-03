# -*- coding: utf-8 -*-
"""
Theoretical results class.

Created on Sun Apr  2 11:16:43 2017

@author: Calil
"""

import numpy as np
from src.support.enumerations import ChannelModel

class Theoretical(object):
    
    def __init__(self,model,tx_rate,p):
        """
        Constructor method. Initializes atrributes:
            self.__model -- parameters object
            self.__p -- PER numpy array
            self.__state_ps -- state probabilities for Markov channel
        
        Keyword parameters:
           model -- channel model
           p -- PER numpy array
        """
        self.__p = p
        self.__tx_rate = tx_rate
        self.__model = model
        if model == ChannelModel.MARKOV:
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
        if self.__model is ChannelModel.IDEAL:
            return self.validate_ideal()
        elif self.__model is ChannelModel.CONSTANT:
            return self.validate_constant()
        elif self.__model is ChannelModel.MARKOV:
            return self.validate_markov()
        else:
            raise NameError('Unknown channel model!')
      
    def get_model(self): 
        """Getter for Parameters object."""
        return self.__model
    
    def get_p(self):
        """Getter for PER numpy array."""
        return self.__p
    
    def get_tx_rate(self):
        """Getter for tx_rate."""
        return self.__tx_rate
    
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
        ber_mean = np.zeros(np.size(self.get_p()))
        per_mean = np.zeros(np.size(self.get_p()))
        thrpt_mean = self.get_tx_rate() * np.ones(np.size(self.get_p()))
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