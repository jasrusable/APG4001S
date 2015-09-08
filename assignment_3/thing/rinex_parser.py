from .utils import parse_float
from .satellite import Satellite
from .epoch import Epoch


class RinexParser(object):
    def __init__(self, file_path):
        self.file_path = file_path
        self.satellites = []
        self.epochs = []
        # Header is a list of lines
        self.header = []
        self.observations = []

    def get_satellite(self, prn):
        wanted_sat = None
        for sat in self.satellites:
            if sat.prn == prn:
                wanted_sat = sat
        return wanted_sat

    def get_epoch(self, year, month, day, hour, minute, second):
        wanted_ep = None
        for ep in self.epochs:
            if (ep.year == year and
                    ep.month == month and
                    ep.day == day and
                    ep.hour == hour and
                    ep.minute == minute and
                    ep.second == second):
                wanted_ep = ep
        return wanted_ep

    def process_observation_lines(self, lines):
        prn = int(lines[0][0:2])
        year = int(lines[0][3:5])
        month = int(lines[0][6:8])
        day = int(lines[0][9:11])
        hour = int(lines[0][12:14])
        minute = int(lines[0][15:17])
        second = float(lines[0][18:22])
        sv_clock_bias = parse_float(lines[0][22:41])
        sv_clock_drift = parse_float(lines[0][41:60])
        sv_clock_drift_rate = parse_float(lines[0][60:79])
        iode = parse_float(lines[1][4:22])
        crs = parse_float(lines[1][22:41])
        delta_n = parse_float(lines[1][41:60])
        m0 = parse_float(lines[1][60:79])
        print(m0)
        sat = self.get_satellite(prn)
        if not sat:
            sat = Satellite(prn)
            self.satellites.append(sat)
        ep = self.get_epoch(year, month, day, hour, minute, second)
        if not ep:
            ep = Epoch(year, month, day, hour, minute, second)
            self.epochs.append(ep)

    def parse(self):
        temp_header = []
        temp_lines = []
        counter = 0
        with open(self.file_path, 'r') as f:
            for line in f:
                if not self.header:
                    temp_header.append(line)
                    if 'END OF HEADER' in line:
                        self.header = temp_header
                else:
                    if counter < 7:
                        temp_lines.append(line)
                        counter += 1
                    else:
                        self.process_observation_lines(temp_lines)
                        temp_lines = []
                        counter = 0
