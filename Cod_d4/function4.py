# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 09:53:52 2019

@author: Luis
"""

def repeat_list_of_file_line(file_name, line_num, num_copies):
     '''
     Input:  Str - path to file,
             Int - number of line to copy from file,
             Int - number of times to copy line into list
     Output: List - filled with num_copies of line_num in file_name
     '''
     line = None
     with open(file_name) as f:
         for i, file_line in enumerate(f, 1):
             if i == line_num:
                 line = file_line.strip()
     if not line:
         copies_of_line = 'There were not {} lines in the document'.format(line_num)
     else:
         copies_of_line = [line for _ in range(num_copies)]
     return copies_of_line