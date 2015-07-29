import math

from things import Thing
from create_stations import create_stations
from constants import GM, A, GAMMA_EQUATOR, K, SECOND_EXCENTRICITY


def find_thing(tag, things, m=None, n=None):
    results = []
    for thing in things:
        if (thing.tag == tag
            and thing.m == m
            and thing.n == n):
            results.append(thing)
    if len(results) == 0:
        raise Exception("No things found with n: {n}, m: {m}.".format(n=n, m=m))
    elif len(results) > 1:
        raise Exception("Too many things found.")
    return results[0]

def read_things_from_file(path):
    things = []
    with open(path, 'r') as f:
        f.readline()
        f.readline()
        for line in f:
            things.append(Thing(line=line))
    return things

stations = create_stations()
hermanus = stations[0]
list_of_things = read_things_from_file('grvfld.ggm02s')
#print().value)


def get_gama(phi):
    """ Phi should be in degrees.
    """
    phi = math.radians(phi)
    neumerator = 1 + K * (math.sin(phi) ** 2)
    denomenator = math.sqrt(1 - SECOND_EXCENTRICITY * (math.sin(phi)**2))
    return GAMMA_EQUATOR * (neumerator / denomenator)

def get_n(r, theta, lambda_):
    N = GM / (get_gama(theta) * r)
    for n in range(2, 100):
        N += (A / r)**n
        for m in range(0, n):
            current_c_thing = find_thing('C', list_of_things, n=n, m=m)
            current_s_thing = find_thing('S', list_of_things, n=n, m=m)

print(get_n(
        hermanus.ellipsoidal_height, 
        hermanus.geographical_coordinate.latitude, 
        hermanus.geographical_coordinate.longitude,
        )
    )