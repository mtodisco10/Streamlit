import streamlit as st
import numpy as np
import pandas as pd

# Write a title and a bit of a blurb
st.title('Distribution Tester')
st.write('Pick a distribution from the list and we shall draw the a line chart from a random sample from the distribution')
# Make some choices for a user to select
keys = ['Normal','Uniform']
dist_key = st.selectbox('Which Distribution do you want to plot?', keys)
# Logic of our program
if dist_key == 'Normal':
    nums = np.random.randn(1000)
elif dist_key == 'Uniform':
    nums = np.array([np.random.randint(100) for i in range(1000)])
# Display User
st.line_chart(nums)

x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)

add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data(10000)
# Notify the reader that the data was successfully loaded.
data_load_state.text("Done! (using st.cache)")

st.subheader('Raw data')
st.write(data)

st.subheader('Number of pickups by hour')

hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]

st.bar_chart(hist_values)