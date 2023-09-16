import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image

st.set_page_config(page_title='Car Insurance company - Customer info',
                    page_icon=":car:",
                      layout="centered",
                        initial_sidebar_state="auto",
                          menu_items=None)
st.title('Car Insurance company - Customer info')

@st.cache_data
def load_data():
    data = pd.read_csv("data/data.csv")
    return data

data_load_state = st.text('Loading data...')
data = load_data()
data_load_state.text("Import done! (using st.cache_data)")


image = Image.open('data/car_image.jpg')
st.image(image, caption='This is a nice car')

st.subheader('Who are the clients?')

tab1, tab2, tab3 = st.tabs(["Gender distribution", "Age distribution", "Vehicle Age distribution"])
with tab1:
    fig = px.histogram(data, x="Gender", category_orders=dict(day=["Male", "Female"]))
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)

with tab2:
    fig = px.histogram(data, x="Age")
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)

with tab3:
    fig = px.histogram(data, x="Vehicle_Age")
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)

st.subheader('Explore the dataset!')

# Check dataset if needed
if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

# Create a radio button for gender selection
selected_gender = st.radio('Select Gender',
                            ['Male', 'Female', 'Both'],
                              horizontal=True)

# Define a function to filter data based on the selected radio button
def filter_data(selected_gender):
    if selected_gender == 'Both':
        return data
    elif selected_gender == 'Male':
        return data[data['Gender'] == 'Male']
    elif selected_gender == 'Female':
        return data[data['Gender'] == 'Female']
    else:
        return None

# Filter data based on the selected radio button
filtered_data = filter_data(selected_gender)

# Display the proportion of vehicle damage for the selected gender(s)
if filtered_data is not None:
    vehicle_damage_proportion = filtered_data['Vehicle_Damage'].value_counts(normalize=True)

    if 'No' in vehicle_damage_proportion:
        no_damage_percentage = vehicle_damage_proportion['No'] * 100
        st.write(f"Never had damage: <font size='+3'><font color='green'>**{no_damage_percentage:.1f}%**</font></font>", unsafe_allow_html=True)

    if 'Yes' in vehicle_damage_proportion:
        yes_damage_percentage = vehicle_damage_proportion['Yes'] * 100
        st.write(f"Already had damage: <font size='+3'><font color='red'>**{yes_damage_percentage:.1f}%**</font></font>", unsafe_allow_html=True)
else:
    st.write("Please select a gender option.")


with st.expander("See explanation"):
    st.write(
        "No, you're not dreaming. Women have proportionately fewer car accidents than men."
    )



