# -*- coding: utf-8 -*-
"""
Unit tests for Channel class

Created on Sun Mar 26 12:12:32 2017

@author: Calil
"""

import unittest
import numpy as np

from . import Channel
from .support import ChannelModel

class ChannelTest(unittest.TestCase):
    def setUp(self):
        seed = 10
        self.n_bits = 1000
        self.channel1 = Channel(ChannelModel.IDEAL,seed)
        self.channel2 = Channel(ChannelModel.CONSTANT,seed)
        self.channel3 = Channel(ChannelModel.MARKOV,seed)
        
    def test_get_model(self):
        self.assertEqual(ChannelModel.IDEAL,\
                         self.channel1.get_model())
        self.assertEqual(ChannelModel.CONSTANT,\
                         self.channel2.get_model())
        self.assertEqual(ChannelModel.MARKOV,\
                         self.channel3.get_model())
        
    def test_get_seed(self):
        self.assertEqual(10,self.channel1.get_seed())
        
    def test_fade(self):
        """
        TODO Implement unit test for constant and Markov channels
        """
        pck_Tx = np.zeros([1,self.n_bits])
        
        # Ideal channel should cause no bit errors
        pck_Rx = self.channel1.fade(pck_Tx)
        self.assertEqual(0,np.sum(pck_Rx))        
        
if __name__ == '__main__':
    unittest.main()