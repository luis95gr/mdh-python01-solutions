# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 14:55:10 2019

@author: Luis
"""

class Member():
    
    def __init__(self, name, haircolor, birthdate, coding_level="beginner", lines_of_code=None, num_lines_coded=0):
        self.name = name
        self.haircolor = haircolor
        self.birthdate = birthdate
        self.coding_level = coding_level
        self.num_lines_coded = num_lines_coded
       
        self.questions_asked = []
        if lines_of_code is None:
            self.lines_of_code =[]
        else: 
            self.lines_of_code = lines_of_code
            
    def add_question_asked(self, question):
        self.questions_asked.append(question)
        
    def add_coded_line(self,code_line):
        self.lines_of_code.append(code_line)
        self.num_lines_coded += 1
        self.get_coding_level()
        
    def get_coding_level(self):
        if self.num_lines_coded <= 100:
            self.coding_level = "beginner"
        elif self.num_lines_coded <= 1000:
            self.coding_level = "novice"
        elif self.num_lines_coded <= 10000:
            self.coding_level = "intermediate"
        elif self.num_lines_coded > 10000:
            self.coding_level = "master"
            
    def get_questions(self):
        return len(self.questions_asked)
            
    
            
        