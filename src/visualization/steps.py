import streamlit as st
import plotly.graph_objects as go


def get_step(step):
    step = 0 if step == None else 1
    return step


def load_step_image(step):
    step = get_step(step)
    if step == 0:
        st.image('../../reports/figures/steps0.png')
    elif step == 1:
        st.image('../../reports/figures/steps1-Liftoff.png')
    elif step == 2:
        st.image('../../reports/figures/steps2-MECO.png')
    elif step == 3:
        st.image('../../reports/figures/steps3-Fairing.png')
    elif step == 4:
        st.image('../../reports/figures/steps4-Landing.png')
    return


def show_step(step):
    figsteps = go.Figure(go.Indicator(
        mode="gauge",
        value=4,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': "Steps", 'font': {'size': 24}},
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
    st.plotly_chart(figsteps)
    return
