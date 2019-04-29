# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 14:55:10 2019

@author: Luis
"""

class Member():
    
    def __init__(self, name, haircolor, birthdate, coding_level="beginner",lines_of_code=0):
        self.name = name
        self.haircolor = haircolor
        self.birthdate = birthdate
        self.coding_level = coding_level
        self.lines_of_code = lines_of_code
       
        self.questions_asked = []
        
    def add_question_asked(self, question):
        self.questions_asked.append(question)
        
    def add_coded_line(self,code_line):
        
    def get_coding_level(self):
        if(coding_level)
        