# -*- coding: utf-8 -*-
"""
Unit tests for statistics class.

TODO Implement test for wrap up function.

Created on Mon Mar 27 14:54:10 2017

@author: Calil
"""

import unittest
import numpy as np

from src.statistics import Statistics

class StatisticsTest(unittest.TestCase):
    
    def setUp(self):
        conf = 0.95     # Confidence
        n_bits = 1000   # Number of bits per packet
        tx_rate = 50    # Tx rate in Mbps
        
        self.stat = Statistics(conf,n_bits,tx_rate)
        
    def test_get_conf(self):
        self.assertEqual(0.95,self.stat.get_conf())
        
    def test_get_n_bits(self):
        self.assertEqual(1000,self.stat.get_n_bits())
        
    def test_get_tx_rate(self):
        self.assertEqual(50,self.stat.get_tx_rate())
        
    def test_get_n_pcks(self):
        self.assertEqual(0,self.stat.get_n_pcks())
        
    def test_get_n_pck_errors(self):
        self.assertEqual(0,self.stat.get_n_pck_errors())
        
    def test_get_per_array(self):
        self.assertEqual(0,len(self.stat.get_per_array()))
        
    def test_get_thrpt_array(self):
        self.assertEqual(0,len(self.stat.get_thrpt_array()))
        
    def test_pck_received(self):
        self.stat.pck_received(False)
        self.stat.pck_received(False)
        self.stat.pck_received(False)
        self.stat.pck_received(True)
        
        self.assertEqual(4,self.stat.get_n_pcks())
        self.assertEqual(1,self.stat.get_n_pck_errors())
        
        # Test calc_results() method
        per, thrpt = self.stat.calc_results()
        self.assertEqual(0.25,per)
        self.assertEqual(37.5,thrpt)
        self.assertEqual(np.array([0.25]),self.stat.get_per_array())
        self.assertEqual(np.array([37.5]),self.stat.get_thrpt_array())     
        
    def test_conf_interval(self):
        data = [1.0e-04, 5.0e-05, 1.0e-05, 2.0e-05]
        meanVal, interv = self.stat.conf_interval(data)
        self.assertAlmostEqual(4.5e-05,meanVal, delta = 0.05e-05)
        self.assertAlmostEqual(6.42995e-05,interv,delta=0.05e-05)
        
    def test_wrap_up(self):
        self.stat.pck_received(False)
        self.stat.pck_received(False)
        self.stat.pck_received(False)
        self.stat.pck_received(True)
        self.stat.reset()
        
        self.assertEqual(0,self.stat.get_n_pcks())
        self.assertEqual(0,self.stat.get_n_pck_errors())
        
        self.stat.pck_received(False)
        self.stat.pck_received(False)
        self.stat.pck_received(True)
        self.stat.pck_received(True)
        self.stat.reset()
        
        per, per_conf, thrpt, thrpt_conf = self.stat.wrap_up()
        
        self.assertAlmostEqual(0.375,per,delta = 0.01)
        self.assertAlmostEqual(1.1234,per_conf,delta = 0.01)
        self.assertAlmostEqual(31.25,thrpt,delta = 0.01)
        self.assertAlmostEqual(56.1708,thrpt_conf,delta = 0.01)
        
if __name__ == '__main__':
    unittest.main()
        