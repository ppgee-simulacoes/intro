# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 16:37:57 2017

@author: Calil
"""

import unittest

from . import GenerateRandom

class GenerateRandomTest(unittest.TestCase):
    
    def setUp(self):
        self.generate_random = GenerateRandom()
    
    def test_seed(self):
        self.assertEqual(1,self.generate_random.get_seed())
        
    def test_num_samples(self):
        self.assertEqual(0,self.generate_random.get_num_samples())
 
       
if __name__ == '__main__':
    unittest.main()