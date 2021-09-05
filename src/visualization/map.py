import streamlit as st
import pandas as pd
import numpy as np


def show_map():
    df = pd.DataFrame(
        np.random.randn(10, 2) / [50, 50] + [-26.36, -48.84],
        columns=['lat', 'lon'])
    st.map(df, zoom=13, use_container_width=True)
    return
