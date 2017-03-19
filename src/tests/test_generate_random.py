# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 16:37:57 2017

@author: Calil
"""

import unittest
import numpy as np

from . import GenerateRandom

class GenerateRandomTest(unittest.TestCase):
    
    def setUp(self):
        seed = 10
        num_samples = 1000
        self.generate_random = GenerateRandom(seed,num_samples)
    
    def test_seed(self):
        self.assertEqual(10,self.generate_random.get_seed())
        
    def test_num_samples(self):
        self.assertEqual(1000,self.generate_random.get_num_samples())
        
    def test_uniform(self):
        rnd_arr = self.generate_random.uniform()
        self.assertEqual(1000,np.size(rnd_arr,1))
       
if __name__ == '__main__':
    unittest.main()