# -*- coding: utf-8 -*-
"""
Theoretical class unit tests.

Created on Sun Apr  2 11:58:11 2017

@author: Calil
"""

import unittest
import numpy as np
from src.parameters.parameters import Parameters
from src.theoretical import Theoretical

class TheoreticalTest(unittest.TestCase):
    
    def setUp(self):
        param = Parameters(1)
        self.theo = Theoretical(param)
        
    def test_get_param(self):
        par = self.theo.get_param()
        self.assertEqual(20,len(par.p))
        
    def test_get_state_ps(self):
        ps = self.theo.get_state_ps()
        self.assertEqual(0,len(ps))
        
    def test_validate(self):
        # Ideal channel should have 0 BER and PER and Tput = tx_rate
        ber, per, thrpt = self.theo.validate_ideal()
        
        # Assert values
        self.assertFalse(np.any(ber != 0))
        self.assertFalse(np.any(per != 0))
        self.assertFalse(np.any(thrpt != 50))
        
        # For now, constant channel sould return exception
        with self.assertRaises(NotImplementedError):
            ber, per, thrpt = self.theo.validate_constant()
            
        # For now, Markov channel sould return exception
        with self.assertRaises(NotImplementedError):
            ber, per, thrpt = self.theo.validate_markov()
    
if __name__ == '__main__':
    unittest.main()