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

        iode = parse_float(lines[1][3:22])
        crs = parse_float(lines[1][22:41])
        delta_n = parse_float(lines[1][41:60])
        m0 = parse_float(lines[1][60:79])

        cuc = parse_float(lines[2][3:22])
        e = parse_float(lines[2][22:41])
        cus = parse_float(lines[2][41:60])
        sqrt_a = parse_float(lines[2][60:79])

        ttoe = parse_float(lines[3][3:22])
        cic = parse_float(lines[3][22:41])
        big_omega = parse_float(lines[3][41:60])
        cis = parse_float(lines[3][60:79])

        i0 = parse_float(lines[4][3:22])
        crc = parse_float(lines[4][22:41])
        omega = parse_float(lines[4][41:60])
        omega_dot = parse_float(lines[4][60:79])

        idot = parse_float(lines[5][3:22])
        codes_on_l2 = parse_float(lines[5][22:41])
        gps_week = parse_float(lines[5][41:60])
        l2_p_data_flag = parse_float(lines[5][60:79])

        sv_accuracy = parse_float(lines[6][3:22])
        sv_health = parse_float(lines[6][22:41])
        tgd = parse_float(lines[6][41:60])
        iodc = parse_float(lines[6][60:79])

        ttom = parse_float(lines[7][3:22])

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
                    temp_lines.append(line)
                    if counter == 7:
                        self.process_observation_lines(temp_lines)
                        temp_lines = []
                        counter = 0
                    else:
                        counter += 1
