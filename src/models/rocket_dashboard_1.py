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
    return df


def streaming_data(**kwargs):
    df = get_data()
    df['timestamp'] = [pd.Timestamp.now()]
    logger.info(f'df: {df}')
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
    return


logger = logging.getLogger(__name__)
f_handler = logging.FileHandler('rm.log')
f_handler.setLevel(logging.DEBUG)
f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
f_handler.setFormatter(f_format)
logger.addHandler(f_handler)
logger.setLevel(logging.DEBUG)

# r3 = Rocket(fuel=100)
# logger.info(f'r3: {r3}')

df = PeriodicDataFrame(streaming_data, interval='1s')
logger.info(f'df: {df}')

initiate_dash()

liftoff()





