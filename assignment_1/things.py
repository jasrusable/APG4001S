class Thing(object):
    def __init__(self, name=None, m=None, n=None, value=None, line=None):
        if line:
            #print("Creating Thing from line. Ignoring other args.")
            self.create_from_line(line)
        else:
            #print("Creating Thing from args.")
            self.name = name
            self.m = m
            self.n = n
            self.value = value

    @property
    def tag(self):
        return self.name[5]

    def create_from_line(self, line):
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
        self.name = name
        self.m = m
        self.n = n
        self.value = value
