#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 11:03:15 2020

@author: viktorstenby
"""

def bakebread():
    import time
    steps = ['Take a bowl', \
             'Add water', \
             'Add yeast', \
             'Add flour',  \
             'Form bread', \
             'Leave the bread to rise for 30 minutes', \
             'Bake the bread', \
             'Enjoy!']
        
    for step in steps:
        print(step)
        time.sleep(2)
        
    
bakebread()