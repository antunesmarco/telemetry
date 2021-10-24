import streamlit as st
from steps import show_step
from altitude import show_altitude
from map import show_map
from video import show_video
from stage import show_stage

st.set_page_config(
    page_title="Kosmos Telemetry",
    page_icon="🧊",
    layout="wide"
)

col1, col2, col3 = st.columns(3)
col1.image('../../reports/figures/logo_kosmos.jpg', width=100)
col2.title("Kosmos Telemetry")

show_stage()

with st.container():
    show_altitude()

col1, col2, col3 = st.columns(3)
show_map(col1)

show_video(col2)



