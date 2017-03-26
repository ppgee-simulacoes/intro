# -*- coding: utf-8 -*-
"""
Enumerations used.

Created on Sun Mar 26 12:06:35 2017

@author: Calil
"""

from enum import Enum

class ChannelModel(Enum):
    """
    Types of channel model
    """
    IDEAL = 0
    CONSTANT = 1
    MARKOV = 2