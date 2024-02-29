import streamlit as st
import pandas as pd

import warnings
warnings.filterwarnings('ignore')

st.title('CPU and RAM Data')

steamdataset = pd.read_csv('shs.csv')

# Display percentage of each CPU manufacturer over the years
st.write('The graph below shows the percentage of each CPU manufacturer over the years.')
cpu = steamdataset.loc[(steamdataset['category'] == 'Intel CPU Speeds') | (steamdataset['category'] == 'AMD CPU Speeds')]
cpu = cpu.groupby(['date', 'category']).agg({'percentage': 'sum'}).reset_index()
cpu = cpu.pivot(index='date', columns='category', values='percentage')
cpu['Intel CPU'] = cpu['Intel CPU Speeds']
cpu.drop(columns=['Intel CPU Speeds'], inplace=True)
cpu['AMD CPU'] = 1 - cpu['Intel CPU']
cpu.drop(columns=['AMD CPU Speeds'], inplace=True)
cpu = cpu[cpu['AMD CPU'] < 0.9]
# Plot a stacked bar chart
st.bar_chart(cpu, use_container_width=True)

# Display average RAM size over the years
st.write('The graph below shows the percentage of RAM size over the years.')
ram = steamdataset.loc[(steamdataset['category'] == 'System RAM')]
ram = ram.groupby(['date', 'name']).agg({'percentage': 'sum'}).reset_index()
ram = ram.pivot(index='date', columns='name', values='percentage')
st.line_chart(ram, use_container_width=True)