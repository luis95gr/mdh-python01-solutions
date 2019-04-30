# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 17:33:25 2019

@author: Luis
"""


class TipOutTracker:
    
    def __init__(self, tip=0.18):
        self.tip = tip
        self.tipsList = []
        
    def add_bill(self, bill, tip=0.18):
        self.tipsList.append(bill*tip)
        
    def __str__(self):
        return sum(self.tipsList)
    
    def __len__(self):
        return len(self.tipsList)
            