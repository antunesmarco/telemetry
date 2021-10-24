import streamlit as st
import plotly.graph_objects as go
from PIL import Image


def get_stage():
    stage = 'parachute'
    return stage


def show_cgi(stage, col):
    stage_image = {
        'liftoff': '../../data/raw/liftoff.png',
        'meco': '../../data/raw/meco.png',
        'apogee': '../../data/raw/apogee.png',
        'parachute': '../../data/raw/parachute.png',
        'landing': '../../data/raw/landing.png'
    }
    image = Image.open(stage_image[stage])
    col.image(image, use_column_width='auto')
    # streamlit.image(image, caption=None, width=None, use_column_width=None, clamp=False, channels='RGB', output_format='auto')
    return


def show_stagemeter(stage, col):
    stage_id = {
        'liftoff': 1,
        'meco': 2,
        'apogee': 3,
        'parachute': 5,
        'landing': 6
    }
    figsteps = go.Figure(go.Indicator(
        mode="gauge",
        value=stage_id[stage],
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': "Stage", 'font': {'size': 24}},
        gauge={
            'axis': {
                'range': [None, 6], 'tickwidth': 1, 'tickcolor': "darkblue",
                'ticktext': ['Liftoff', 'MECO', 'Apogee', 'Fairing', 'Parachute', 'Landing'],
                'tickvals': [1, 2, 3, 4, 5, 6]
            },
            'bar': {'color': "cyan"},
            'bgcolor': "white",
            'borderwidth': 2,
            'bordercolor': "gray",
            'steps': [
                {'range': [0, 1], 'color': 'darkblue'},
                {'range': [1, 2], 'color': 'darkblue'},
                {'range': [2, 3], 'color': 'darkblue'},
                {'range': [3, 4], 'color': 'darkblue'},
                {'range': [4, 5], 'color': 'darkblue'},
                {'range': [5, 6], 'color': 'darkblue'}
            ],
            'threshold': {
                'line': {'color': "red", 'width': 5},
                'thickness': 1,
                'value': 3},
        }
    ))

    figsteps.update_layout(font={'color': "cyan", 'family': "Arial"})
    figsteps.update_traces(name="Liftoff", selector=dict(type='indicator'))
    col.plotly_chart(figsteps)
    return


def show_stage():
    col1, col2, col3 = st.columns(3)
    stage = get_stage()
    show_stagemeter(stage, col1)
    show_cgi(stage, col3)

    return
