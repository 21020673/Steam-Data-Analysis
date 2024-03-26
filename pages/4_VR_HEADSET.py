import streamlit as st
import pandas as pd
import numpy as np
from pages.utils.utils import format_price

import warnings
warnings.filterwarnings('ignore')

st.title('VR Headset Data')


def categorize_vr_headset(vr_headset):
    if 'Windows Mixed Reality' in vr_headset:
        return 'Windows Mixed Reality'
    elif 'HTC' in vr_headset:
        return 'HTC'
    # elif 'Oculus Rift S' in vr_headset:
    #     return 'OCULUS RIFT S'
    elif 'Valve Index' in vr_headset:
        return 'Valve Index'
    elif 'Oculus' or 'Meta' in vr_headset:
        return 'Oculus/Meta'
    else:
        return 'Other'


steamdataset = pd.read_csv('shs.csv')

vr_dataset = pd.read_csv('List_of_virtual_reality_headsets_2.csv')

# Display percentage of each headset type over the years
st.write('The graph below shows the percentage of each headset manufacturer over the years.')

# Filter data for VR Headsets
vr = steamdataset.loc[(steamdataset['category'] == 'VR Headsets') & (
    steamdataset['date'] >= '2020-02-01') & (
    steamdataset['date'] != '2022-08-01')]

# List of VR Headsets and prices
vr_dataset['Price'] = vr_dataset['Price'].apply(format_price)
vr_dataset = vr_dataset.merge(vr, left_on='Name', right_on='name')
vr_dataset.drop_duplicates(subset=['Name', 'date'], inplace=True)

# Apply categorization function to 'name' column
vr['name'] = vr['name'].apply(categorize_vr_headset)

# Group by date and name, and calculate the sum of percentages for each combination
vr_grouped = vr.groupby(['date', 'name']).agg(
    {'percentage': 'sum'}).reset_index()

# Pivot the data to have 'date' as index and 'name' as columns, with 'percentage' as values
vr_pivot = vr_grouped.pivot(
    index='date', columns='name', values='percentage').fillna(0)

# Plot the data using a bar chart
st.bar_chart(vr_pivot, use_container_width=True)

st.write('The graph below shows the average price of VR headsets over the years. The price is listed in USD.')
vr_dataset['Price'] = vr_dataset['Price'].astype(float)
vr_dataset['expected_value'] = vr_dataset['percentage'] * vr_dataset['Price']
vr_dataset = vr_dataset.groupby('date').agg(
    {'expected_value': 'sum', 'percentage': 'sum'}).reset_index()
vr_dataset['average_price'] = vr_dataset['expected_value'] / vr_dataset['percentage']
st.line_chart(vr_dataset[['date', 'average_price']].set_index('date'), use_container_width=True)