import streamlit as st
import plotly.graph_objects as go
import numpy as np
import time


def show_speedometer(col1):
    figspeed = go.Figure(go.Indicator(
        mode="gauge+number",
        value=300,
        # domain={'x': [0, 0], 'y': [0, 0]},
        #domain={'row': 0, 'column': 0},
        title={'text': "Speed (Km)"},
        number={'font': {'size':80}}
    ))
    # fig.show()
    col1.plotly_chart(figspeed, use_column_width=True)
    return


def show_altimeter(col2):
    figalt = go.Figure(go.Indicator(
        mode="gauge+number",
        value=1000,
        # domain={'x': [1, 1], 'y': [1, 1]},
        #domain={'row': 0, 'column': 2},
        title={'text': "Altitude (m)"}
    ))
    # fig.show()
    col2.plotly_chart(figalt, use_column_width=True)
    return


def show_altitude_graph():
    # Get some data.
    data = np.random.randn(10, 2)
    # Show the data as a chart.
    chart = st.line_chart(data)
    # Wait 1 second, so the change is clearer.
    time.sleep(1)
    # Grab some more data.
    data2 = np.random.randn(10, 2)
    # Append the new data to the existing chart.
    chart.add_rows(data2)
    return


def show_altitude():
    col1, col2, col3 = st.columns(3)
    show_speedometer(col1)
    show_altimeter(col2)
    show_altitude_graph()
    return