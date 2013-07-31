# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 15:08:37 2013

@author: laegrim
"""

import sys
from logging import getLogger
from logging.config inport fileConfig
from configobj import ConfigObj
import city

class Run(object):
    '''Execution script for pycity'''
    
    def __init__(self, log_loc, seo_loc, duration):
        self.log_loc = log_loc
        self.seo_loc = seo_loc
        self.duration = duration
        
        fileconfig(log_loc)
        self.logger = getLogger(log_loc)
        
        self.conf = ConfigObj(seo_loc)
        
if '__name__' == __main__:
    
    run_script = Run('log.conf', 'seo.conf', sys.argv[0])
    
    