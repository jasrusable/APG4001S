import math
import sympy

from things import Thing
from create_stations import create_stations
from constants import GM, A, GAMMA_EQUATOR, K, SECOND_EXCENTRICITY
from constants import J2, J4, J6, J8


def find_thing(tag, things, m=None, n=None):
    results = []
    for thing in things:
        if (thing.tag == tag
            and thing.m == m
            and thing.n == n):
            results.append(thing)
    if len(results) == 1:
        return results[0]
    elif len(results) > 1:
        raise Exception("Too many things found.")
    return None

def read_things_from_file(path):
    things = []
    with open(path, 'r') as f:
        f.readline()
        f.readline()
        for line in f:
            things.append(Thing(line=line))
    return things

def get_gama(phi):
    """ Phi should be in radians.
    """
    neumerator = 1 + K * (math.sin(phi) ** 2)
    denomenator = math.sqrt(1 - SECOND_EXCENTRICITY * (math.sin(phi)**2))
    return GAMMA_EQUATOR * (neumerator / denomenator)

def get_p(n, m, t):
    return sympy.assoc_legendre(n, m, t)

def get_r(station):
    x_term = station.cartesian_coordinate.x ** 2
    y_term = station.cartesian_coordinate.y ** 2
    z_term = station.cartesian_coordinate.z ** 2
    return math.sqrt(x_term + y_term + z_term)

def get_n(r, theta, lambda_):
    cos = math.cos
    sin = math.sin
    theta_radians = math.radians(theta)
    lambda_radians = math.radians(lambda_)

    initial = GM / (get_gama(math.pi - theta_radians) * r)
    
    outter_loop = 0
    for n in range(2, 20):
        inner_loop = 0
        for m in range(0, n):
            current_c_thing = find_thing('C', list_of_things, n=n, m=m)
            if not current_c_thing:
                print('No current_c_thing for {n}, {m}'.format(n=n, m=m))
            current_s_thing = find_thing('S', list_of_things, n=n, m=m)
            if not current_s_thing:
                print('No current_s_thing for {n}, {m}'.format(n=n, m=m))
                s = 0
            else:
                s = current_s_thing.value

            if n == 2 and m == 0:
                c = current_c_thing.value + J2
            elif n == 4 and m == 0:
                c = current_c_thing.value + J4
            elif n == 6 and m == 0:
                c = current_c_thing.value + J6
            elif n == 8 and m == 0:
                c = current_c_thing.value + J8
            else:
                c = current_c_thing.value

            inner_loop += (c * cos(m * lambda_radians) + s * sin(m * lambda_radians)) * get_p(n, m, cos(theta_radians))
        outter_loop += ((A / r)**n) * inner_loop
    return initial * outter_loop

stations = create_stations()
hermanus = stations[0]
list_of_things = read_things_from_file('grvfld.ggm02s')

har_lat = hermanus.geographical_coordinate.latitude
har_long = hermanus.geographical_coordinate.longitude
har_r = get_r(hermanus)

print(get_n(
        har_r, 
        har_lat, 
        har_long,
    )
)
