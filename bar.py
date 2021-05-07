#!/usr/bin/env python
# coding: utf-8

# In[4]:

import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import gzip
import shutil
from scipy.stats import chisquare

import pathlib
import pandas as pd
import streamlit as st


from plotly.subplots import make_subplots
import plotly.graph_objects as go
from plotly.offline import plot


#requires libraries to be locally installed, csv file and script need to be in same folder. 
st.title('KinessoX')

#import data

data = pd.read_csv('Audience_DE.csv')
data




data = data.replace({'$30,000 to $49,999':'30,000 to 49,999',
                           '$50,000 to $74,999':'50,000 to 74,999',
                           '$75,000 to $99,999':'75,000 to 99,999',
                           '$100,000 to $149,999':'100,000 to 149,999',
                           '$150,000 to $199,999':'150,000 to 199,999',
                           '$200,000 to $249,999':'200,000 to 249,999'})


#creates selectbox object for column selection
columns = tuple(data.columns)

column = st.sidebar.selectbox(
    'what column would yout like to filter by?',
    columns
)

st.write('You selected:', column)

#create selectbox object for value filtering on column chosen
values = tuple(data[column].unique())
select_2 = st.sidebar.selectbox(
    'what value-range/category would yout like to filter by?',
    values
    
)
st.write('you selected:', select_2)

#manipulate data to column and value selection
selected = data[data[column] == select_2]



def print_charts(orig, new, col_name, order):
    
    #bar chart for original dataset
    labels_orig = pd.DataFrame(orig[col_name]
                .value_counts(normalize=True)).reset_index().iloc[:, 0]
    sizes_orig = pd.DataFrame(orig[col_name]
                .value_counts(normalize=True)).reset_index().iloc[:, 1] * 100
    
    fig_orig = make_subplots(rows = 1, cols = 2, 
            subplot_titles=(col_name + ": Original", col_name + ": New"))
    fig_orig.add_trace(go.Bar(x = labels_orig, y=sizes_orig, name = 'Original'), row = 1, col = 1)
    
    #bar chart for new dataset
    
    sizes_new = []
    for i in labels_orig:
        sizes_new = np.append(sizes_new, (len(new[new[col_name] == i])/len(new[col_name]))*100)
    
    fig_orig.add_trace(go.Bar(x = labels_orig, y=sizes_new, name = "New"), row = 1, col = 2)
    
    fig_orig.update_xaxes(categoryorder = 'array', categoryarray = order)
    
    diff, pval = chisquare(sizes_orig, sizes_new)
    
    fig_orig.update_layout(height=350, width=700, 
                title_text="Change in " + col_name + 
                ". Chi squared difference: " + str(round(diff, 3)) +
                ". P_value: " + str(round(pval, 3)) )
    
    fig_orig.update_yaxes(range=[0,max(max(sizes_orig), max(sizes_new)) + 5])
    
    fig_orig.update_yaxes(tickvals = np.arange(0,101, 10))
    
    fig_orig.show()


print_charts(data, selected, "DEMO_HH_INCOME", ['Less than $30,000','30,000 to 49,999',
                                                   '50,000 to 74,999','75,000 to 99,999',
                                                   '100,000 to 149,999', '150,000 to 199,999',
                                                   '200,000 to 249,999', '$250,000 +'] )
print_charts(data, selected, "GENDER", ['F', 'M'])

print_charts(data, selected, "HOMEOWNERSHIP_STATUS", ['Homeowner', 'Renter'])

print_charts(data, selected, "EDUCATION", ['High School', 'College', 'Graduate School', 'Vocational_or_Technical', 'not_reported'])
    
print_charts(data, selected, "ETHNICITY", np.unique(data['ETHNICITY']))

print_charts(data, selected, "DMA_NAME_ACXIOM", np.unique(data["DMA_NAME_ACXIOM"]))


    





