
class Thing(object):
    def __init__(self, name, m, n, value):
        assert(type(name) == str)
        assert(type(m) == int)
        assert(type(n) == int)
        assert(type(value) == float)
        self.name = name
        self.m = m
        self.n = n
        self.value = value

    @property
    def tag(self):
        return self.name[5]
    
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
            parts = line.split()
            name = parts[0]
            if len(parts) == 3:
                nm = parts[1]
                n = nm[:3]
                m = nm[3:]
            elif len(parts) == 4:
                n = parts[1]
                m = parts[2]
            else:
                raise Exception("Incorrect parts length.")
            n = int(n)
            m = int(m)
            val, exp = parts[-1].split('D')
            value = float(val) * (10 ** int(exp)) 
            things.append(Thing(
                name=name,
                n=n,
                m=m,
                value=value,
            ))
    return things

tmp = read_file('grvfld.ggm02s')
print(find_thing('S', 160, 160, tmp).value)
