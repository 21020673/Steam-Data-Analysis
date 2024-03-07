import streamlit as st
import pandas as pd
from pages.utils.utils import extract_numerical_value

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

# Display CPU core count over the years
st.write('The graph below shows the average CPU core count over the years.')
cc = steamdataset.loc[(steamdataset['category'] == 'Physical CPUs')]
cc['value'] = cc['name'].str.extract('(\d+)').astype(float)
cc = cc.loc[cc['value'].notnull()]
# Multiply the percentage by the RAM size to get the expected value
cc['expected_value'] = cc['percentage'] * cc['value']
# Sum the expected values for each year
cc = cc.groupby('date').agg({'expected_value': 'sum'}).reset_index()
# Plot a line chart
st.line_chart(cc.set_index('date')['expected_value'], use_container_width=True)

# Display average RAM size over the years
st.write('The graph below shows the average RAM size over the years.')
ram = steamdataset.loc[(steamdataset['category'] == 'System RAM')]
ram['value'] = ram['name'].apply(extract_numerical_value)
ram = ram.loc[ram['value'].notnull()]
# Multiply the percentage by the RAM size to get the expected value
ram['expected_value'] = ram['percentage'] * ram['value']
# Sum the expected values for each year
ram = ram.groupby('date').agg({'expected_value': 'sum'}).reset_index()
# Plot a line chart
st.line_chart(ram.set_index('date')['expected_value'], use_container_width=True)