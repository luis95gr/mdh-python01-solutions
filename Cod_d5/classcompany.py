# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 12:53:45 2019

@author: Luis
"""

class Company:
    
    def __init__(self, name, industry_type, num_employees, total_revenue):
        self.name = name
        self.industry_type = industry_type
        self.num_employees = num_employees
        self.total_revenue = total_revenue
        
        self.employeesL = []
        
    def serve_customer(self, cost):
        self.total_revenue += cost
        
    def gain_employees(self, emplpoyees):
        self.num_employees += len(emplpoyees)
        
        
    