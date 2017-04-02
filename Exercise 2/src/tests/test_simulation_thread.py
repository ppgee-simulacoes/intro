# -*- coding: utf-8 -*-
"""
SimulationThread class unit tests.

Created on Sun Apr  2 15:21:28 2017

@author: Calil
"""

import unittest
import numpy as np
from src.simulation_thread import SimulationThread
from src.parameters.parameters import Parameters
from src.support.enumerations import ChannelModel

class SimulationThreadTest(unittest.TestCase):
    
    def setUp(self):
        par = Parameters(1)
        figs_dir = "test_figs/"
        
        # Redefine parameters for easy testing
        new_seed = np.array([0, 1])
        par.seeds = new_seed.astype(int)
        par.chan_mod = ChannelModel.IDEAL
        
        self.par = par
        self.sim = SimulationThread(par,figs_dir)
    
    def test_get_seed_count(self):
        self.assertEqual(0,self.sim.get_seed_count())
        
    def test_get_ber_count(self):
        self.assertEqual(0,self.sim.get_ber_count())
        
    def test_send_pck(self):
        n_errors, pck_error = self.sim.send_pck()
        self.assertTrue(n_errors >= 0)
        if pck_error:
            self.assertTrue(n_errors > 0)
        else:
            self.assertTrue(n_errors == 0)
            
    def test_new_seed(self):
        self.sim.new_seed()
        self.assertEqual(1,self.sim.get_seed_count())
        self.assertTrue(self.sim.station.get_seed() == self.par.seeds[1])
        self.assertTrue(self.sim.chann.get_seed() == self.par.seeds[1])
        
    def test_new_ber(self):
        self.sim.new_ber()
        self.assertEqual(1,self.sim.get_ber_count())
        self.assertTrue(self.sim.chann.get_p() == self.par.p[1])
        
    def test_simulate(self):
        self.sim.simulate()
    
if __name__ == '__main__':
    unittest.main()