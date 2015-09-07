def parse_float(value):
    try:
        base, exp = value.split('D')
    except ValueError:
        print('No D')
    try:
        base, exp = value.split('E')
    except:
        pass
    return float(base) * (10 ** int(exp))
