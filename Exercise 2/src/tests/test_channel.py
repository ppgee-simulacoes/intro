# -*- coding: utf-8 -*-
"""
Unit tests for Channel class

Created on Sun Mar 26 12:12:32 2017

@author: Calil
"""

import unittest
import numpy as np

from src.channel import Channel
from src.support.enumerations import ChannelModel

class ChannelTest(unittest.TestCase):
    def setUp(self):
        seed = 10
        self.n_bits = 1000
        p = 1e-5
        self.channel1 = Channel(ChannelModel.IDEAL,seed,p)
        self.channel2 = Channel(ChannelModel.CONSTANT,seed,p)
        self.channel3 = Channel(ChannelModel.MARKOV,seed,p)
        self.channel4 = Channel(3,seed,p)
        
    def test_get_model(self):
        self.assertEqual(ChannelModel.IDEAL,\
                         self.channel1.get_model())
        self.assertEqual(ChannelModel.CONSTANT,\
                         self.channel2.get_model())
        self.assertEqual(ChannelModel.MARKOV,\
                         self.channel3.get_model())
        
    def test_get_seed(self):
        self.assertEqual(10,self.channel1.get_seed())
        
    def test_get_p(self):
        self.assertEqual(1e-5,self.channel1.get_p())
        
    def test_set_p(self):
        self.channel1.set_p(2e-5)
        self.assertEqual(2e-5,self.channel1.get_p())
        
    def test_fade(self):
        """
        TODO Implement unit test for constant channel
        TODO Implement unit test for Markov channel
        """
        pck_Tx = np.zeros([1,self.n_bits])
        
        # Ideal channel should cause no bit errors
        pck_Rx = self.channel1.fade(pck_Tx)
        self.assertEqual(0,np.sum(pck_Rx))
        
        # For now, constant channel sould return exception
        with self.assertRaises(NotImplementedError):
            pck_Rx = self.channel2.fade(pck_Tx)
            
        # For now, Markov channel sould return exception
        with self.assertRaises(NotImplementedError):
            pck_Rx = self.channel3.fade(pck_Tx)
        
        # Invalid Channel Model should raise exception
        with self.assertRaises(NameError):
            pck_Rx = self.channel4.fade(pck_Tx)
        
if __name__ == '__main__':
    unittest.main()