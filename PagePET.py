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

Temp_January = input("tell me the average Temperature F for January")

I_January = I_value(Temp_January)

Temp_Febuary = input("tell me the average Temperature F for Febuary")

I_Febuary = I_value(Temp_Febuary)

Temp_March = input("tell me the average Temperature F for March")

I_March = I_value(Temp_March)

Temp_April = input("tell me the average Temperature F for April")

I_April = I_value(Temp_April)

Temp_May = input("tell me the average Temperature F for May")

I_May = I_value(Temp_May)

Temp_June = input("tell me the average Temperature F for June")

I_June = I_value(Temp_June)

Temp_July = input("tell me the average Temperature F for July")

I_July = I_value(Temp_July)

Temp_August = input("tell me the average Temperature F for August")

I_August = I_value(Temp_August)

Temp_September = input("tell me the average Temperature F for September")

I_September = I_value(Temp_September)

Temp_October = input("tell me the average Temperature F for October")

I_October = I_value(Temp_October)

Temp_November = input("tell me the average Temperature F for November")

I_November = I_value(Temp_November)

Temp_December = input("tell me the average Temperature F for December")

I_December = I_value(Temp_December)






