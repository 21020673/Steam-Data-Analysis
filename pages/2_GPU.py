import streamlit as st
import pandas as pd

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