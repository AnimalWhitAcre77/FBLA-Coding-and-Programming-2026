#this is a file with functions that don't have to be in Small Business Finder.py
import os
from pathlib import Path
import tkinter as tk

#validation functions ----

#Checks the input to be a float between 0.0 and 5.0 with at most 1 decimal
def is_rating(value):
    if value == "" or value in ["0.", "1.", "2.", "3.", "4.", "5."]:
        return True
    
    try:
        numValue = float(value)
    except:
        return False
    
    if numValue < 0 or numValue > 5:
        return False
    
    if value != f"{numValue:.1f}" and value != f"{numValue:.0f}":
        return False
    
    return True