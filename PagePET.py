#This will be a webpage for my caluclate your own Evapotransparation

import streamlit as st
import pandas as pd
import numpy as np
from pathlib import Path
import streamlit as st
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu
import pandas as pd

lat = 10
#choose imput 0, 10,15,20,25,30,40
""" IGNORE
Ajustment_factor_January = 
Ajustment_factor_March = 
Ajustment_factor_April = 
Ajustment_factor_May = 
Ajustment_factor_June =  
Ajustment_factor_July = 
Ajustment_factor_August = 
Ajustment_factor_September = 
Ajustment_factor_October = 
Ajustment_factor_November = 
Ajustment_factor_December = 
"""
#what month are you interested in?
#tell me the average temperature of the month

def I_value(Temp_value)->float:
    I_value = (Temp_value/5)**1.5
    return I_value

def Convert_to_Celsius(Temp_value)->float:
    Celsius = (Temp_value-32)*5/9
    return Celsius

Temp_January = input("tell me the average Temperature F for January")
Temp_C_January = Convert_to_Celsius(Temp_January)
I_January = I_value(Temp_C_January)

Temp_Febuary = input("tell me the average Temperature F for Febuary")
Temp_C_Febuary = Convert_to_Celsius(Temp_Febuary)
I_Febuary = I_value(Temp_C_Febuary)

Temp_March = input("tell me the average Temperature F for March")
Temp_C_March = Convert_to_Celsius(Temp_March)
I_March = I_value(Temp_C_March)

Temp_April = input("tell me the average Temperature F for April")
Temp_C_April = Convert_to_Celsius(Temp_April)
I_April = I_value(Temp_C_April)

Temp_May = input("tell me the average Temperature F for May")
Temp_C_May = Convert_to_Celsius(Temp_May)
I_May = I_value(Temp_C_May)

Temp_June = input("tell me the average Temperature F for June")
Temp_C_June = Convert_to_Celsius(Temp_June)
I_June = I_value(Temp_C_June)

Temp_July = input("tell me the average Temperature F for July")
Temp_C_July = Convert_to_Celsius(Temp_July)
I_July = I_value(Temp_C_July)

Temp_August = input("tell me the average Temperature F for August")
Temp_C_August = Convert_to_Celsius(Temp_August)
I_August = I_value(Temp_C_August)

Temp_September = input("tell me the average Temperature F for September")
Temp_C_September = Convert_to_Celsius(Temp_September)
I_September = I_value(Temp_C_September)

Temp_October = input("tell me the average Temperature F for October")
Temp_C_October = Convert_to_Celsius(Temp_October)
I_October = I_value(Temp_C_October)

Temp_November = input("tell me the average Temperature F for November")
Temp_C_November = Convert_to_Celsius(Temp_November)
I_November = I_value(Temp_C_November)

Temp_December = input("tell me the average Temperature F for December")
Temp_C_December = Convert_to_Celsius(Temp_December)
I_December = I_value(Temp_C_December)






