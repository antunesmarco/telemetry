import pandas as pd
import param
import panel as pn
import hvplot.pandas
import hvplot.streamz
import holoviews as hv
from holoviews.element.tiles import EsriImagery
from streamz.dataframe import PeriodicDataFrame
from rocket2 import Rocket
import logging
from rocket_simulator_1 import liftoff


def get_data():
    df = pd.read_csv('rs.csv')
    return df.tail(1)


def streaming_data(**kwargs):
    df = get_data()
    df.loc[:, 'timestamp'] = [pd.Timestamp.now()]
    cols = ["stage", "velocity", "fuel", "wet_mass", "altitude", "thrust"]
    logger.info(f'df com timestamp: {df[cols]}')
    return df.set_index('timestamp')


def initiate_dash():
    pn_realtime = pn.Column(
        # pn.Row(dfstage.hvplot.barh('keys', 'values', title='Stage', backlog=1000)),
        pn.Row(df['altitude'].hvplot.line(title='Altitude', backlog=1000)),
        pn.Row(df['velocity'].hvplot.line(title='Velocity', backlog=1000))
    )

    pane = pn.Tabs(
        ('Real Time', pn_realtime)
    ).servable()
    pane
    logger.info(f'dash iniciado')
    return


logger = logging.getLogger(__name__)
f_handler = logging.FileHandler('rd.log', mode='w')
f_handler.setLevel(logging.DEBUG)
f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
f_handler.setFormatter(f_format)
logger.addHandler(f_handler)
logger.setLevel(logging.DEBUG)

df = PeriodicDataFrame(streaming_data, interval='1s')
logger.info(f'df: {df}')

initiate_dash()

liftoff()





