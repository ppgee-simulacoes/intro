# -*- coding: utf-8 -*-
"""
Results class: saves and plots results.

Created on Thu Mar 30 16:41:59 2017

@author: Calil
"""

import numpy as np

class Results(object):
    
    def __init__(self,param):
        """
        Class constructor. Defines attributes:
            self.__param -- simulation parameters class
            self.__per_list -- list of PER mean values
            self.__per_conf_list -- list of PER confidences
            self.__thrpt_list -- list of Throughput mean values
            self.__thrpt_conf_list -- list of Throughput confidences
            
        Keyword parameters:
            param -- Parameters class
        """
        pass
    
    def get_per_list(self):
        """Getter for PER mean value list."""
        pass
    
    def get_per_conf(self):
        """Getter for PER confidence delta list."""
        pass
    
    def get_thrpt_list(self):
        """Getter for Throughput mean value list."""
        pass
    
    def get_thrpt_conf(self):
        """Getter form Throughput confidence delta list."""
        pass
    
    def store_res(self,per,thrpt):
        """
        Stores PER and Throughput for future ploting.
        
        Keyword parameters:
            per -- tuple containg PER mean value and confidence delta
            thrpt -- tuple containing Tput mean value and confidence delta
        """
        pass
    
    def plot(self):
        """
        Plots PER vs p and Throughput vs p simulation results.
        """
        pass