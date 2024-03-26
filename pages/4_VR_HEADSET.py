import streamlit as st
import pandas as pd

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
    elif 'Meta Quest' in vr_headset:
        return 'Meta Quest'
    elif 'Valve Index' in vr_headset:
        return 'Valve Index'
    elif 'Oculus' in vr_headset:
        return 'Oculus'
    else:
        return 'Other'


steamdataset = pd.read_csv('shs.csv')

# Display percentage of each headset type over the years
st.write('The graph below shows the percentage of each headset type over the years.')

# Filter data for VR Headsets
vr = steamdataset.loc[(steamdataset['category'] == 'VR Headsets') & (
    steamdataset['date'] >= '2020-02-01') & (
    steamdataset['date'] != '2022-08-01')]

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

