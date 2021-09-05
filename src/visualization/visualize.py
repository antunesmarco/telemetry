import streamlit as st
from steps import show_step
from altitude import show_altitude
from map import show_map
from video import show_video


st.set_page_config(layout="wide")
with st.container():
    show_step(1)

with st.container():
    show_altitude()

show_map()

show_video()






