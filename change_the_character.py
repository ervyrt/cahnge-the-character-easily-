# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 16:32:56 2021

@author: yurtbas
"""
def change_character(txt): 
    fromm=str(input("Please write the character that you want to change:"))
    to=str(input("Please write the character that you want to change to:"))

    for i in txt:
        if i==fromm:
            txt=txt.replace(i,to)
            
    print(txt)  
change_character("Hello, I am Erva I develop python programs ")
