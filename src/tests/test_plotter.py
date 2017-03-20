# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 09:49:02 2017

@author: Calil
"""

import unittest
import numpy as np

from . import Plotter

class PlotterTest(unittest.TestCase):
    
    def setUp(self):
        num_samples = 1000
        
        self.plotter = Plotter(num_samples)
        
    def test_num_samples(self):
        self.assertEqual(1000,self.plotter.get_num_samples())
        
    def test_plot_uniform(self):
        arr = np.arange(0,self.plotter.get_num_samples(),1)
        arr = arr/self.plotter.get_num_samples()
        self.plotter.plot_uniform(arr)

if __name__ == '__main__':
    unittest.main()