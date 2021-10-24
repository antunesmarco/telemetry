import logging
# from rocket_dashboard_1 import initiate_dash
import pandas as pd

from rocket2 import Rocket


def calc_y_disp(self, y1, y0):
    return y1 - y0


def calc_velocity(self, y_disp, t1, t0):
    return y_disp / (t1 - t0)


def calc_accel(self, v1, v0, t1, t0):
    return (v1 - v0) / (t1 - t0)


def calc_m1(mdry, mfuel, t, txq):
    return mdry + (mfuel - (mfuel * t * txq))


def calc_v1(m1, m0, v0, f, t1, t0):
    return (f * (t1 - t0) + (m0 * v0)) / m1


def calc_y1(v, t):
    return v * t


def react(rdata, g, y0, y1, v0, t0, t1, m0):
    if rdata['fuel'] == 0:
        rdata['thrust'] = 0
        weight = rdata['dry_mass'] * g
    else:
        weight = (rdata['dry_mass'] + rdata['fuel']) * g

    net_force = weight + rdata['thrust']
    # logger.info(f'net_force: {net_force:.2f}')
    m1 = calc_m1(rdata['dry_mass'], rdata['fuel'], t1, rdata['burn_rate'])
    rdata['wet_mass'] = m1

    v1 = calc_v1(m1, m0, v0, net_force, t1, t0)
    rdata['velocity'] = v1

    y1 += calc_y1(v1, 1)
    rdata['altitude'] = y1

    if y1 <= 0:
        y1 = 0
        v1 = 0

    y0 = y1

    logger.info(f"thrust: {rdata['thrust']:.2f}N, weight: {weight:.2f}N, net_force: {net_force:,.2f}N")
    logger.info(f"m1: {m1: .2f}Kg, v1: {v1:,.2f}m/s, y1: {y1:,.2f}m")

    m0 = m1
    v0 = v1
    t1 += 1
    return rdata, y0, v0, t0


logger = logging.getLogger(__name__)
f_handler = logging.FileHandler(__name__ + '.log')
f_handler.setLevel(logging.INFO)
f_format = logging.Formatter('%(asctime)s - %(name)s - %(funcName)s - %(lineno)d - %(levelname)s - %(message)s')
f_handler.setFormatter(f_format)
logger.addHandler(f_handler)
logging.basicConfig(level=logging.INFO)


def liftoff():
    g = -9.8  # m/s2
    y0 = 0  # metros
    y1 = 0  # metros
    v0 = 0  # m/s

    t0 = 0  # segundos
    t1 = 1  # segundos
    logger.info(f't0: {t0}s')
    r1 = Rocket(dry_mass=1, fuel=1)
    rdata = r1.send_data()
    logger.info(f'stage: {rdata["stage"]}, velocity: {rdata["velocity"]}, fuel: {rdata["fuel"]}, ' \
                f'wet_mass: {rdata["wet_mass"]}, altitude: {rdata["altitude"]}')

    m0 = rdata['wet_mass']
    r1.ignite()
    rdata = r1.send_data()
    rs = pd.DataFrame()

    while t1 < 20:
        logger.info(f't1: {t1}s')
        rs.append(pd.DataFrame(rdata, index=[t1]).to_csv('rs.csv'))
        rdata, y0, v0, t0 = react(rdata, g, y0, y1, v0, t0, t1, m0)
        logger.info(f'stage: {rdata["stage"]}, velocity: {rdata["velocity"]}, fuel: {rdata["fuel"]}, ' \
                    f'wet_mass: {rdata["wet_mass"]}, altitude: {rdata["altitude"]}')

        if y0 == 0:
            break
        # refresh_dash(updated_data)
        # r1.read_sensors(updated_data)
        t1 += 1
        r1.burn_fuel()
        rdata = r1.send_data()

    print(f'FINAL: {r1}')

    return






