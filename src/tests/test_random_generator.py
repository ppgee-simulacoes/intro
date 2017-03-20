# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 16:37:57 2017

@author: Calil
"""

import unittest
import numpy as np

from . import RandomGenerator

class RandomGeneratorTest(unittest.TestCase):
    
    def setUp(self):
        seed = 10
        num_samples = 1000
        
        self.random_generator_1 = RandomGenerator(seed,num_samples)
        self.random_generator_2 = RandomGenerator(seed,num_samples)
    
    def test_seed(self):
        self.assertEqual(10,self.random_generator_1.get_seed())
        
    def test_num_samples(self):
        self.assertEqual(1000,self.random_generator_1.get_num_samples())
        
    def test_uniform(self):
        rnd_arr_1 = self.random_generator_1.uniform()
        
        self.assertEqual(1000,len(rnd_arr_1))
        
        self.assertTrue(np.amin(rnd_arr_1) >= 0)
        self.assertTrue(np.amax(rnd_arr_1) <= 1)
        
        #Test mean value
        epsilon = 0.05
        self.assertTrue(abs(np.mean(rnd_arr_1) - 0.5) < epsilon)
        
        #Same seed should yield same arrays
        rnd_arr_2 = self.random_generator_2.uniform()
        self.assertTrue(np.array_equal(rnd_arr_1,rnd_arr_2),
                        "Arrays created with same seed differ")
        
    def test_normal(self):
        rnd_arr_1 = self.random_generator_1.normal()
        
        self.assertEqual(1000,len(rnd_arr_1))
        
        #Test standard deviation
        epsilon = 0.05
        self.assertTrue(abs(np.std(rnd_arr_1) - 1) < epsilon)
        
        #Test mean value
        epsilon = 0.05
        self.assertTrue(abs(np.mean(rnd_arr_1) - 0) < epsilon)
        
        #Same seed should yield same arrays
        rnd_arr_2 = self.random_generator_2.normal()
        self.assertTrue(np.array_equal(rnd_arr_1,rnd_arr_2),
                        "Arrays created with same seed differ")
        
    def test_tringle(self):
        rnd_arr_1 = self.random_generator_1.triangle()
        
        self.assertEqual(1000,len(rnd_arr_1))
        
        #Test mean value
        epsilon = 0.1
        self.assertTrue(abs(np.mean(rnd_arr_1) - 6.6666666) < epsilon)
        
        #Same seed should yield same arrays
        rnd_arr_2 = self.random_generator_2.triangle()
        self.assertTrue(np.array_equal(rnd_arr_1,rnd_arr_2),
                        "Arrays created with same seed differ")
       
if __name__ == '__main__':
    unittest.main()