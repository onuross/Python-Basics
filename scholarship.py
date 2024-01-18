#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 13:43:00 2022

@author: onursemitosun
"""

NAME_SURNAME= input("Name Surname:")
GENDER= input("Gender (m/f):")
GPA= float(input("GPA:"))
if GENDER== 'f' :
    WAGE=float(input("Monthly Family Income:"))
BASE_SCHOLARSHIP= 250
MIN_GPA=2
GPA_FACTOR=35
MIN_WAGE=2400
FEMALE_ADDITION=150
GPA_ADDITION=GPA*GPA_FACTOR
scholarship= BASE_SCHOLARSHIP

if GPA>=MIN_GPA :
    scholarship = scholarship + GPA_ADDITION

    
if GENDER=='f' and WAGE <= MIN_WAGE:
    scholarship = scholarship + FEMALE_ADDITION

print(f"Student: {NAME_SURNAME} \nScholarship: {scholarship}")
    

