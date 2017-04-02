# -*- coding: utf-8 -*-
"""
Simulation thread class.

Created on Sun Apr  2 11:04:28 2017

@author: Calil
"""

from source import Source
from channel import Channel
from statistics import Statistics
from results import Results
from parameters.parameters import Parameters

class SimulationThread(object):
    def __init__(self,param,figs_dir):
        """
        Constructor method. Receives parameters and builds the simulation 
        objects.
        
        Keyword parameters:
            param -- parameters object
        """
        self.param = param
        self.station = Source(param.n_bits,param.seeds[0])
        self.chann = Channel(param.chan_mod,param.seeds[0],param.p[0])
        self.stat = Statistics(param.n_bits,param.tx_rate,param.conf)
        self.res = Results(param,figs_dir)
        
        self.__seed_count = 0
        self.__ber_count = 0
        
    def get_seed_count(self):
        """Returns the seed count."""
        return self.__seed_count
        
    def get_ber_count(self):
        """Returns the BER count."""
        return self.__ber_count
    
    def simulate(self):
        """
        Performs simulation loop and generates results.
        """
        
        # Seed loop
        while(self.get_seed_count() < len(self.param.seeds)):
        
            # Packet loop
            for pck in range(0,self.param.n_pcks):
                # Send packet
                n_errors, pck_error = self.send_pck()
            
                # Save results only if warm-up is over
                if pck > self.param.n_warm_up_pcks:
                    self.stat.pck_received(pck_error)
                
            # After all packets have been sent, calculate iteration results
            self.stat.calc_iteration_results()
        
            # Set new seed
            self.new_seed()
            
        # Calculate mean and confidence
        per_tpl, thrpt_tpl = self.stat.wrap_up()
        return per_tpl, thrpt_tpl
            
        
    def send_pck(self):
        """
        Generates, sends and calculates error for one packet.
        
        Returns:
            n_errors -- number of bir errors in received packet
            pck_error -- boolean, True if packet has errors
        """
        pck_tx = self.station.generate_packet()
        pck_rx = self.chann.fade(pck_tx)
        n_errors, pck_error = self.station.calculate_error(pck_rx)
        
        return n_errors, pck_error
    
    def new_seed(self):
        """
        Sets the seed of all objects, incrementing the seed counter.
        """
        self.__seed_count = self.__seed_count + 1
        if self.get_seed_count() < len(self.param.seeds):
            self.station.set_seed(self.param.seeds[self.get_seed_count()])
            self.chann.set_seed(self.param.seeds[self.get_seed_count()])
        
    def reset_seed(self):
        """
        Resets the seed of all objects.
        """
        self.__seed_count = 0
        self.station.set_seed(self.param.seeds[self.get_seed_count()])
        self.chann.set_seed(self.param.seeds[self.get_seed_count()])
    
    def new_ber(self):
        """
        Resets the channel's BER.
        """
        self.__ber_count = self.__ber_count + 1
        self.chann.set_p(self.param.p[self.get_ber_count()])