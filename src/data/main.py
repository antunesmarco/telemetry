import pandas as pd
import param
import panel as pn
import hvplot.pandas
import hvplot.streamz
import holoviews as hv
from holoviews.element.tiles import EsriImagery
from streamz.dataframe import PeriodicDataFrame
from rocket import Rocket
import logging


def get_data():
    data = r3.send_data()
    logger.info(f'data: {data}')

    df = pd.DataFrame({
        'altitude': data['altitude'],
        'speed': data['speed'],
        'stage': data['stage']
    }, index=['medida'])

    r3.burn_fuel()
    return df


def streaming_data(**kwargs):
    df = get_data()
    df['timestamp'] = [pd.Timestamp.now()]
    logger.info(f'df: {df}')
    return df.set_index('timestamp')


logger = logging.getLogger(__name__)
f_handler = logging.FileHandler('main.log')
f_handler.setLevel(logging.DEBUG)
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
f_handler.setFormatter(f_format)
logger.addHandler(f_handler)


r3 = Rocket(100)

df = PeriodicDataFrame(streaming_data, interval='1s')
logger.info(f'df: {df}')

pn_realtime = pn.Column(
    # pn.Row(dfstage.hvplot.barh('keys', 'values', title='Stage', backlog=1000)),
    pn.Row(df['altitude'].hvplot.line(title='Altitude', backlog=1000)),
    pn.Row(df['speed'].hvplot.line(title='Speed', backlog=1000))
)

def data_plot(col):
    df = get_data()
    df['x'], df['y'] = -48.8455600, -26.3044400
    table = hv.Table(df['altitude']).opts(width=800)
    points = df.hvplot.scatter('x', 'y', c=col, cmap='bkr', hover_cols=['name'])
    map_tiles = EsriImagery().opts(alpha=0.5, width=900, height=480, bgcolor='white')
    return pn.Column(points * map_tiles, table)


# REFRESH
class refresh_rocket_dashboard(param.Parameterized):
    action = param.Action(lambda x: x.param.trigger('action'), label='Refresh')
    select_column = param.ObjectSelector(default='altitude', objects=['altitude'])

    @param.depends('action', 'select_column')
    def get_plot(self):
        return data_plot(self.select_column)


rocket_dashboard = refresh_rocket_dashboard()

pn_rocket = pn.Column(
    pn.panel(rocket_dashboard.param, show_labels=True, show_name=False, margin=0),
    rocket_dashboard.get_plot, width=400
)

# COMBINE TWO DASHBOARDS
pane = pn.Tabs(
    ('Real Time', pn_realtime),
    ('Refresh Rocket Dashboard', pn_rocket)
).servable()

r3.ignite()

pane
