import streamlit as st
import pandas as pd

import warnings
warnings.filterwarnings('ignore')

st.title('Operating System Data')

def categorize_windows_version(os_name):
    if 'Windows 11' in os_name:
        return 'Windows 11'
    if 'Windows 10' in os_name:
        return 'Windows 10'
    elif 'Windows 7' in os_name:
        return 'Windows 7'
    elif 'Windows Vista' in os_name:
        return 'Windows Vista'
    elif 'Windows XP' in os_name:
        return 'Windows XP'
    elif 'Windows 8' in os_name:
        return 'Windows 8/8.1'
    else:
        return 'Other'

steamdataset = pd.read_csv('shs.csv')

# Display percentage of each operating system over the years
st.write('The graph below shows the percentage of OS versions over the years.')
os = steamdataset.loc[(steamdataset['category'] == 'OS Version')]
os['os_category'] = os['name'].apply(categorize_windows_version)
os.loc[os['name'].str.contains('MacOS'), 'os_category'] = 'MacOS'
os = os.groupby(['date', 'os_category']).agg({'percentage': 'sum'}).reset_index()
os = os.pivot(index='date', columns='os_category', values='percentage')
# Plot a stacked bar chart
st.bar_chart(os, use_container_width=True)
