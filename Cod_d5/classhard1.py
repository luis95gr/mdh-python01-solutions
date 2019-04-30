# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 14:13:44 2019

@author: Luis
"""

class OurClass():
    
    def __init__(self, name, location, size=0,members=None):
        self.name = name
        self.location = location
        self.size = size
        self.members = members
        self.questions

        
        self.check_if_at_capacity()
        
        if self.members is None:
            self.members=[]
        else:
            self.members = members


    def add_class_members(self, member):
        
        self.members.append(member)
        
        self.size += 1

        if self.check_if_at_capacity() is False:
            print('Capacity Reached!!')
            
    def check_if_at_capacity(self):
        if self.size >= 31:
            self.at_capacity = True
            return False
        else:
            self.at_capacity = False
            return True
        
    def get_questions(self):
        return len(self.questions_asked)
    
    def get_num_questions_asked(self):
        for member in self.members:
            self.questions += member.get_questions()
        return self.questions
        
        

        
        
        
        