import streamlit as st
import pandas as pd
from pages.utils.utils import extract_numerical_value

import warnings
warnings.filterwarnings('ignore')

st.title('GPU Data')

steamdataset = pd.read_csv('shs.csv')

# Display percentage of each video card manufacturer over the years
st.write('The graph below shows the percentage of each video card manufacturer over the years.')
video_card = steamdataset.loc[(steamdataset['category'] == 'Video Card Description')]
video_card['Manufacturer'] = video_card['name'].str.split(' ').str[0]
# Sum of the percentage of each manufacturer
video_card = video_card.groupby(['date', 'Manufacturer']).agg({'percentage': 'sum'}).reset_index()
video_card = video_card.pivot(index='date', columns='Manufacturer', values='percentage')
video_card = video_card.fillna(0)
video_card['AMD'] = video_card['ATI'] + video_card['AMD'] + video_card['Radeon']
video_card['Intel'] = video_card['Intel'] + video_card['Intel(R)'] + video_card['Mobile'] + video_card['Desktop']
video_card = video_card.drop(columns=['Intel(R)', 'Mobile', 'Desktop', 'ATI', 'Radeon', 'Other', 'Apple', 'RDPDD'])
# Add 'Other' column
video_card['Other'] = 1 - video_card.sum(axis=1)
video_card = video_card[video_card['Other'] < 0.5]
# Plot a stacked bar chart
st.bar_chart(video_card, use_container_width=True)

# Display the average video card memory size over the years
st.write('The graph below shows the average VRAM size over the years. The VRAM size is listed in GB.')
video_card = steamdataset.loc[(steamdataset['category'] == 'VRAM')]
video_card['value'] = video_card['name'].apply(extract_numerical_value)
video_card = video_card.loc[video_card['value'].notnull()]
# Multiply the percentage by the video card memory size to get the expected value
video_card['expected_value'] = video_card['percentage'] * video_card['value']
# Sum the expected values for each year
video_card = video_card.groupby('date').agg({'expected_value': 'sum'}).reset_index()
# Plot a line chart
st.line_chart(video_card.set_index('date')['expected_value'], use_container_width=True)