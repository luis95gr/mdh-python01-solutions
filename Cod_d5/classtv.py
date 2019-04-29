# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 13:45:56 2019

@author: Luis
"""

class Tv:
    
    def __init__(self, brand, on_status, current_channel, life_perc ):
        self.brand = brand
        self.on_status = on_status
        self.current_channel = current_channel
        self.life_perc = life_perc
        
    def hit_power(self):
        if self.on_status:
            self.on_status = False
            self.current_channel = 0
            self.life_perc -= 0.01
        else:
            self.on_status = True
            
    def change_channle(self, channel):
        if self.on_status:
            self.current_channel = channel
        elif self.on_status == False:
            print("The Tv in not turned on")
        
        