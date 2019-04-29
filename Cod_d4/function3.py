# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 09:23:11 2019

@author: Luis
"""

def update_library(books, library):
     '''
     Input:  List - book names, Set - books already in library
     Output: List - books that weren't in the library
     '''
     nwbooks=[]
     for book in books:
         nwbooks=checkLibrary(book,library)
     print(library)    
     return nwbooks
 
def checkLibrary(book,library):
    
    new_books = []
    if book not in library:
        print('The book, {} is new!'.format(book))
        new_books.append(book)
        library.add(book)
    else:
        print("Book not new")
    return new_books
    