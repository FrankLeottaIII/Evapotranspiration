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
i_January = I_value(Temp_C_January)

Temp_Febuary = input("tell me the average Temperature F for Febuary")
Temp_C_Febuary = Convert_to_Celsius(Temp_Febuary)
i_Febuary = I_value(Temp_C_Febuary)

Temp_March = input("tell me the average Temperature F for March")
Temp_C_March = Convert_to_Celsius(Temp_March)
i_March = I_value(Temp_C_March)

Temp_April = input("tell me the average Temperature F for April")
Temp_C_April = Convert_to_Celsius(Temp_April)
i_April = I_value(Temp_C_April)

Temp_May = input("tell me the average Temperature F for May")
Temp_C_May = Convert_to_Celsius(Temp_May)
i_May = I_value(Temp_C_May)

Temp_June = input("tell me the average Temperature F for June")
Temp_C_June = Convert_to_Celsius(Temp_June)
i_June = I_value(Temp_C_June)

Temp_July = input("tell me the average Temperature F for July")
Temp_C_July = Convert_to_Celsius(Temp_July)
i_July = I_value(Temp_C_July)

Temp_August = input("tell me the average Temperature F for August")
Temp_C_August = Convert_to_Celsius(Temp_August)
i_August = I_value(Temp_C_August)

Temp_September = input("tell me the average Temperature F for September")
Temp_C_September = Convert_to_Celsius(Temp_September)
i_September = I_value(Temp_C_September)

Temp_October = input("tell me the average Temperature F for October")
Temp_C_October = Convert_to_Celsius(Temp_October)
i_October = I_value(Temp_C_October)

Temp_November = input("tell me the average Temperature F for November")
Temp_C_November = Convert_to_Celsius(Temp_November)
i_November = I_value(Temp_C_November)

Temp_December = input("tell me the average Temperature F for December")
Temp_C_December = Convert_to_Celsius(Temp_December)
i_December = I_value(Temp_C_December)
#above are all i values for each month
#this is I
Average_Heat_Index = (i_January + i_Febuary + i_March + i_April + i_May + i_June + i_July + i_August + i_September + i_October + i_November + i_December)/12

chosen_month = input("tell me the month you are interested in.  choose in number format, Example: January  = 1")
if chosen_month == 1:
    i_choice = i_January
elif chosen_month == 2:
    i_choice = i_Febuary
elif chosen_month == 3:
    i_choice = i_March
elif chosen_month == 4:
    i_choice = i_April
elif chosen_month == 5:
    i_choice = i_May
elif chosen_month == 6:
    i_choice = i_June
elif chosen_month == 7:
    

a = (0.49) + (0.0179 * Average_Heat_Index ) - (0.0000771 * Average_Heat_Index) + (0.000000675 * Average_Heat_Index)
#h(i/5)^I
Part_1 = 1.6*(10*i_choice /$G$16)^($G$17)


