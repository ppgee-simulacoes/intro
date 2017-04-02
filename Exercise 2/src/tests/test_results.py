# -*- coding: utf-8 -*-
"""
Results class unit tests.

Created on Sun Apr  2 08:42:53 2017

@author: Calil
"""

import unittest
import numpy as np
from src.results import Results
from src.parameters.parameters import Parameters

class ResultsTest(unittest.TestCase):
    
    def setUp(self):
        param = Parameters(1)
        self.res = Results(param)
        
    def test_get_per_list(self):
        per = self.per.get_per_list()
        self.assertEqual(0,len(per))
        
    def test_get_per_conf(self):
        per_conf = self.per.get_per_conf()
        self.assertEqual(0,len(per_conf))
    
    def test_get_thrpt_list(self):
        thrpt = self.per.get_thrpt_list()
        self.assertEqual(0,len(thrpt))
    
    def test_get_thrpt_conf(self):
        thrpt_conf = self.per.get_thrpt_conf()
        self.assertEqual(0,len(thrpt_conf))
        
    def test_store_res_plot(self):
        per_tpl = (1.0e-05, 1.0e-0.6)
        thrpt_tpl = (2.0e-05, 2.0e-0.6)
        
        # Add 100 PER and Throughput results
        for k in xrange(0,100):
            self.res.store_res(per_tpl,thrpt_tpl)
            
        # Check PER length
        per = self.per.get_per_list()
        self.assertEqual(100,len(per))
        
        # Check PER confidence length
        per_conf = self.per.get_per_conf()
        self.assertEqual(100,len(per_conf))
        
        # Check thrpt length
        thrpt = self.per.get_thrpt_list()
        self.assertEqual(100,len(thrpt))
        
        # Check thrpt_conf lenth
        thrpt_conf = self.per.get_thrpt_conf()
        self.assertEqual(100,len(thrpt_conf))
        
        # Plot
        self.res.plot()

if __name__ == '__main__':
    unittest.main()