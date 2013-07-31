# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 13:01:59 2013

@author: laegrim
"""
from numpy.random import randint
from math import floor
from players import Prince, Great, Large, Norm, Small, Tiny
import logging
from logging.config inport fileConfig

class City(object):
    '''Meant to provide a model for the important attributes of a city in 
    this simulation:
    -num_players represents the number of merchants or owners in the city,
    -percentages represent how many of those players fit into each wealth
    catagory.  These should total to 1.
    -ranges represent the range of wealth that defines each catagory.  The 
    caps of these measures should total no more than the city's gold cap.
    -gold_cap represents roughly the total ammount worth of gold held in cash,
    property, and resources by all people in the city.  As time progresses, 
    this may grow less accurate, but gold_cap will provide a useful rough
    measure of the wealth of a city.
    -int_rage represents the annual interest rate earned on cash reserves.  
    Changes based on volatility.
    -volatility is an important percent measure used to calculate many things, 
    often reperesenting how often and to what degree measures change.  This 
    number will greatly, and it may be a good idea to keep this low (.5 - 5%)
    -health represents the overall health of the economy, and can indicate 
    depressions or good markets.  Used in calculating many measures, and 
    changes based on volatility.'''

    def __init__(self, num_players, perc_prince, perc_great, perc_large,
                 perc_norm, perc_small, perc_tiny, range_prince, range_great,
                 range_large, range_norm, range_small, range_tiny, range_lower,
                 gold_cap, int_rate, volatility, health):
        self.num_players = num_players
        self.perc_prince = perc_prince
        self.perc_great = perc_great
        self.perc_large = perc_large
        self.perc_norm = perc_norm
        self.perc_small = perc_small
        self.perc_tiny = perc_tiny
        self.range_prince = range_prince
        self.range_great = range_great
        self.range_large = range_large
        self.range_norm = range_norm
        self.range_small = range_small
        self.range_tiny = range_tiny
        self.range_lower = range_lower
        self.gold_cap = gold_cap
        self.int_rate = int_rate
        self.volatility = volatility
        self.health = health
        
        self.num_prince = floor(self.num_players * self.perc_prince)
        self.num_great = floor(self.num_players * self.perc_great)
        self.num_large = floor(self.num_players * self.perc_large)
        self.num_norm = floor(self.num_players * self.perc_norm)
        self.num_small = floor(self.num_players * self.perc_small)
        self.num_tiny = floor(self.num_players * self.perc_tiny)
        
        self.players = []

        
    def update_city(self):
        '''update city's vital statistics: gold_cap, int_rate, volatility,
        health'''
        
        if randint(1, 101) > 100 - int(self.volatility * 100):
            self.health = self.health + randint(-1, 2) * self.volatility
            self.int_rate = self.int_rate + self.health * self.int_rate
            if self.int_rate < 0:
                self.int_rate = 0
            self.gold_cap = self.gold_cap + self.gold_cap * self.health
            
    def update_players(self):
        '''update players vital statistics'''
        
        for player in self.players:
            player.update()
            
    def create_players(self):
        '''create a list of players (NPCs with stakes in the city)'''
        
        for prince in range(self.num_prince):
            self.players.append(Prince(randint(self.range_great,
                                                       self.range_prince)
                                                       randint(1, 6)))
        for great in range(self.num_great):
            self.players.append(Great(randint(self.range_larege,
                                                      self.range_prince)
                                                      randint(1,6)))
        for large in range(self.num_large):
            self.players.append(Large(randint(self.range_norm,
                                                      self.range_prince)
                                                      randint(1,6)))
        for norm in range(self.num_norm):
            self.players.append(Norm(randint(self.range_small,
                                                     self.range_norm)
                                                     randint(1,6)))
        for small in range(self.num_small):
            self.players.append(Small(randint(self.range_tiny,
                                                      self.range_small)
                                                      randint(1,6)))
        for tiny in range(self.num_tiny):
            self.players.append(Tiny(randint(self.range_lower,
                                                     self.range_tiny),
                                                     randint(1,6)))
        
    def __repr__(self):
        return '''
        self.num_players = %s
        self.perc_prince = %s
        self.perc_great = %s
        self.perc_large = %s
        self.perc_norm = %s
        self.perc_small = %s
        self.perc_tiny = %s
        self.num_prince = %s
        self.num_great = %s
        self.num_large = %s
        self.num_norm = %s
        self.num_small = %s
        self.num_tiny = %s
        self.range_prince = %s
        self.range_great = %s
        self.range_large = %s
        self.range_norm = %s
        self.range_small = %s
        self.range_tiny = %s
        self.gold_cap = %s
        self.int_rate = %s
        self.volatility = %s
        self.health = %s
        ''' % (self.num_players,
        self.perc_prince,
        self.perc_great,
        self.perc_large,
        self.perc_norm,
        self.perc_small,
        self.perc_tiny,
        self.num_prince,
        self.num_great,
        self.num_large,
        self.num_norm,
        self.num_small,
        self.num_tiny, 
        self.range_prince,
        self.range_great,
        self.range_large,
        self.range_norm,
        self.range_small,
        self.range_tiny,
        self.gold_cap,
        self.int_rate,
        self.volatility,
        self.health)
        

    
            
                 
    