from things import Thing


def find_thing(tag, m, n, things):
    results = []
    for thing in things:
        if (thing.tag == tag
            and thing.m == m
            and thing.n == n):
            results.append(thing)
    if len(results) == 0:
        raise Exception("No things found.")
    elif len(results) > 1:
        raise Exception("Too many things found.")
    return results[0]

def read_file(path):
    things = []
    with open(path, 'r') as f:
        f.readline()
        f.readline()
        for line in f:
            thing = Thing(line=line)
            things.append(thing)
    return things

tmp = read_file('grvfld.ggm02s')
print(find_thing('S', 160, 160, tmp).value)
