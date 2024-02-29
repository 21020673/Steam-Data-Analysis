import streamlit as st
import pandas as pd

import warnings
warnings.filterwarnings('ignore')

steamdataset = pd.read_csv('shs.csv')
url = 'https://store.steampowered.com/hwsurvey/'
st.title('Steam Hardware Survey')
st.write('This is a simple web app that displays the Steam Hardware Survey data from November 2008')
st.write('The data is from the following URL: ', url)
st.write('The data is displayed in a table below.')
st.dataframe(steamdataset, use_container_width=True)