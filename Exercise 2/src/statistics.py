# -*- coding: utf-8 -*-
"""
Statistics class: computes simulation statistics

Created on Tue Mar 28 10:29:08 2017

@author: Calil
"""

import numpy as np
import scipy.stats as sp

class Statistics(object):
    
    def __init__(self,n_bits,tx_rate,conf = 0.95):
        
        self.__conf = conf
        self.__n_bits = n_bits
        self.__tx_rate = tx_rate
        
        self.__n_pcks = 0
        self.__n_pck_errors = 0
        
        self.__per_array = np.array([])
        self.__thrpt_array = np.array([])
        
    def get_conf(self):
        return self.__conf
    
    def get_n_bits(self):
        return self.__n_bits
    
    def get_tx_rate(self):
        return self.__tx_rate
    
    def get_n_pcks(self):
        return self.__n_pcks
    
    def get_n_pck_errors(self):
        return self.__n_pck_errors
    
    def get_per_array(self):
        return self.__per_array
    
    def get_thrpt_array(self):
        return self.__thrpt_array
    
    def reset(self):
        self.__n_pcks = 0
        self.__n_pck_errors = 0
    
    def pck_received(self,pck_error):
        self.__n_pcks = self.__n_pcks + 1
        if pck_error:
            self.__n_pck_errors = self.__n_pck_errors + 1
            
    def calc_results(self):
        per = self.get_n_pck_errors()/self.get_n_pcks()
        
        time = self.get_n_bits()*self.get_n_pcks()/(self.get_tx_rate())
        thrpt = (self.get_n_pcks() - self.get_n_pck_errors()) * \
        self.get_n_bits()/time
                                
        np.append(self.__per_array,per)
        np.append(self.__thrpt_array,thrpt)
                                
        return per, thrpt
    
    def conf_interval(self,data):
        """
        Calculates the confidence interval of the mean of input data.
        Code adapted from: https://tinyurl.com/pn96ntp
        
        Keyword parameters:
            data -- input numpy array data
            
        Returns:
            mean_val -- mean value of data
            conf_int -- distance from mean of data's confidence interval
        """
        N_samples = len(data)
        mean_val = np.mean(data)
        se = sp.sem(data)
        conf_int = se*sp.t.ppf((1+self.get_conf())/2., N_samples-1)
        
        return mean_val, conf_int
    
    def wrap_up(self):
        per, per_conf = self.conf_interval(self.get_per_array())
        thrpt, thrpt_conf = self.conf_interval(self.get_thrpt_array())
        
        self.__per_array = np.array([])
        self.__thrpt_array = np.array([])
        
        return per, per_conf, thrpt, thrpt_conf
        
        