import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

import warnings

warnings.filterwarnings('ignore')
st.title('INTEL Price per core')


def categorize_core_i3(core_gen):
    if '1st' in core_gen:
        return 'i3 1st gen'
    elif '2nd' in core_gen:
        return 'i3 2nd gen'
    elif '3rd' in core_gen:
        return 'i3 3rd gen'
    elif '4th' in core_gen:
        return 'i3 4th gen'
    elif '6th' in core_gen:
        return 'i3 6th gen'
    elif '7th' in core_gen:
        return 'i3 7th gen'
    elif '8th' in core_gen:
        return 'i3 8th/9th gen'
    elif '10th' in core_gen:
        return 'i3 10th gen'
    elif '12th' in core_gen:
        return 'i3 12th gen'
    elif '13th' in core_gen:
        return 'i3 13th/14th gen'

coredata = pd.read_csv('i3.csv')

st.write('The graph below shows INTEL i3, i5, i7, i9 (respectively) price per core over the generations (for desktop) .')

coredata['Gen'] = coredata['Gen'].apply(categorize_core_i3)

#Create category to sort
order = ['i3 1st gen', 'i3 2nd gen', 'i3 3rd gen', 'i3 4th gen', 
         'i3 6th gen', 'i3 7th gen', 'i3 8th/9th gen',
         'i3 10th gen','i3 12th gen','i3 13th/14th gen'] 

coredata['Gen'] = pd.Categorical(coredata['Gen'], categories=order, ordered=True)

#Sort by "Gen" column
coredata_sorted = coredata.sort_values(by='Gen', ignore_index= True)

coredata_sorted.set_index('Gen', inplace= True, drop=False)

coreI3 = coredata.pivot(index = 'Gen', columns='Type',values= 'Price/Core').fillna(0)

st.bar_chart(coreI3, use_container_width=True)

#i5 chart

def categorize_core_i5(core_gen):
    if '1st' in core_gen:
        return 'i5 1st gen'
    elif '2nd' in core_gen:
        return 'i5 2nd gen'
    elif '3rd' in core_gen:
        return 'i5 3rd gen'
    elif '4th' in core_gen:
        return 'i5 4th gen'
    elif '5th' in core_gen:
        return 'i5 5th gen'
    elif '6th' in core_gen:
        return 'i5 6th gen'
    elif '7th' in core_gen:
        return 'i5 7th gen'
    elif '8th' in core_gen:
        return 'i5 8th/9th gen'
    elif '10th' in core_gen:
        return 'i5 10th gen'
    elif '11th' in core_gen:
        return 'i5 11th gen'
    elif '12th' in core_gen:
        return 'i5 12th gen'
    elif '13th' in core_gen:
        return 'i5 13th/14th gen'
    

coredata_i5 = pd.read_csv('i5.csv')

coredata_i5['Gen'] = coredata_i5['Gen'].apply(categorize_core_i5)

order_i5 = ['i5 1st gen', 'i5 2nd gen', 'i5 3rd gen', 'i5 4th gen', 'i5 5th gen',
         'i5 6th gen', 'i5 7th gen', 'i5 8th/9th gen',
         'i5 10th gen','i5 11th gen','i5 12th gen','i5 13th/14th gen'] 

coredata_i5['Gen'] = pd.Categorical(coredata_i5['Gen'], categories=order_i5, ordered=True)

coredata_i5_sorted = coredata_i5.sort_values(by='Gen', ignore_index= True)

coredata_i5_sorted.set_index('Gen', inplace= True, drop=False)

coreI5 = coredata_i5.pivot(index = 'Gen', columns='Type',values= 'Price/Core').fillna(0)

st.bar_chart(coreI5, use_container_width=True)

#i7 charts

def categorize_core_i7(core_gen):
    if '1st' in core_gen:
        return 'i7 1st gen'
    elif '2nd' in core_gen:
        return 'i7 2nd gen'
    elif '3rd' in core_gen:
        return 'i7 3rd gen'
    elif '4th' in core_gen:
        return 'i7 4th gen'
    elif '5th' in core_gen:
        return 'i7 5th gen'
    elif '6th' in core_gen:
        return 'i7 6th gen'
    elif '7th' in core_gen:
        return 'i7 7th gen'
    elif '8th' in core_gen:
        return 'i7 8th/9th gen'
    elif '10th' in core_gen:
        return 'i7 10th gen'
    elif '11th' in core_gen:
        return 'i7 11th gen'
    elif '12th' in core_gen:
        return 'i7 12th gen'
    elif '13th' in core_gen:
        return 'i7 13th/14th gen'
    

coredata_i7 = pd.read_csv('i7.csv')

coredata_i7['Gen'] = coredata_i7['Gen'].apply(categorize_core_i7)

order_i7 = ['i7 1st gen', 'i7 2nd gen', 'i7 3rd gen', 'i7 4th gen', 'i7 5th gen',
         'i7 6th gen', 'i7 7th gen', 'i7 8th/9th gen',
         'i7 10th gen','i7 11th gen','i7 12th gen','i7 13th/14th gen'] 

coredata_i7['Gen'] = pd.Categorical(coredata_i7['Gen'], categories=order_i7, ordered=True)

coredata_i7_sorted = coredata_i7.sort_values(by='Gen', ignore_index= True)

coredata_i7_sorted.set_index('Gen', inplace= True, drop=False)

coreI7 = coredata_i7.pivot(index = 'Gen', columns='Type',values= 'Price/Core').fillna(0)

st.bar_chart(coreI7, use_container_width=True)

#i9 chart

def categorize_core_i9(core_gen):
    if '1st' in core_gen:
        return 'i9 1st gen'
    elif '2nd' in core_gen:
        return 'i9 2nd gen'
    elif '3rd' in core_gen:
        return 'i9 3rd gen'
    elif '4th' in core_gen:
        return 'i9 4th gen'
    elif '5th' in core_gen:
        return 'i9 5th gen'
    elif '6th' in core_gen:
        return 'i9 6th gen'
    elif '7th' in core_gen:
        return 'i9 7th gen'
    elif '8th' in core_gen:
        return 'i9 8th/9th gen'
    elif '9th' in core_gen:
        return 'i9 9th gen'
    elif '10th' in core_gen:
        return 'i9 10th gen'
    elif '11th' in core_gen:
        return 'i9 11th gen'
    elif '12th' in core_gen:
        return 'i9 12th gen'
    elif '13th' in core_gen:
        return 'i9 13th/14th gen'
    

coredata_i9 = pd.read_csv('i9.csv')

coredata_i9['Gen'] = coredata_i9['Gen'].apply(categorize_core_i9)

order_i9 = ['i9 1st gen', 'i9 2nd gen', 'i9 3rd gen', 'i9 4th gen', 'i9 5th gen',
         'i9 6th gen', 'i9 7th gen', 'i9 8th/9th gen', 'i9 9th gen',
         'i9 10th gen','i9 11th gen','i9 12th gen','i9 13th/14th gen'] 

coredata_i9['Gen'] = pd.Categorical(coredata_i9['Gen'], categories=order_i9, ordered=True)

coredata_i9_sorted = coredata_i9.sort_values(by='Gen', ignore_index= True)

coredata_i9_sorted.set_index('Gen', inplace= True, drop=False)

coreI9 = coredata_i9.pivot(index = 'Gen', columns='Type',values= 'Price/Core').fillna(0)

st.bar_chart(coreI9, use_container_width=True)