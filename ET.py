#how to have 2 imput windows next to each other for streamlit
import streamlit as st
import pandas as pd
import numpy as np
from pathlib import Path
import streamlit as st
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu
import pandas as pd

# 1. as sidebar menu
# with st.sidebar:
#     selected = option_menu("Product", ["BFR CORPORATE", 'BFR mikro', 'BFR Consumer', 'BRF'], 
#         icons=['play', 'play'], menu_icon="cast", default_index=1)
#     selected
#     print(selected)
# df = pd.read_excel("contoh.xlsx")
# st.dataframe(df)
# st.title('Evapotranspiration Calculator')

# Sidebar
# st.sidebar.header('User Input')
# st.sidebar.subheader('Enter the following information')
# #column 1
# st.sidebar.write('enter the daylenth for october')
# daylength = st.sidebar.number_input('Daylength', 0, 24, 12)#(label, min_value, max_value, value, step)
# # October
# # November
# December
# January
# February
# March
# April
# May
# June
# July
# August
# September
#   Warning: to view this Streamlit app on a browser, run it with the following
#   command:

#     streamlit run <path found locally> [ARGUMENTS]

#how to have a excel look to streamlit
#A: https://discuss.streamlit.io/t/how-to-display-an-excel-file-in-streamlit/1220/2


def app():
    st.title('Evapotranspiration work')
    st.write('This is the calculations for the evapotranspiration for the winter and growing season of 2023')

    df = pd.read_excel("datacopy.xlsx")
    #how to interact with a excel file
    #you can do that by using the pandas library
    # df = pd.read_excel("datacopy.xlsx")
    #interactive table

    st.dataframe(df)

    # st.table(df)

if __name__ == '__main__':
    app()
    # reference hw8

 #   streamlit run /c:/Users/green/Documents/2024Hydrologyprogramming/evapotransporation.py
    #python -m streamlit run your_script.py