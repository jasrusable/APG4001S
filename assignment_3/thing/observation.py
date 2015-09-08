

class Observation(object):
    def __init__(self,
                epoch,
                satellite,
                sv_clock_bias,
                sv_clock_drift,
                sv_clock_drift_rate,

                iode,
                crs,
                delta_n,
                m0,

                cuc,
                e,
                cus,
                sqrt_a,

                ttoe,
                cic,
                big_omega,
                cis,

                i0,
                crc,
                omega,
                omega_dot,

                idot,
                codes_on_l2,
                gps_week,
                l2_p_data_flag,

                sv_accuracy,
                sv_health,
                tgd,
                iodc,

                ttom,
                ):
        self.epoch = epoch
        self.satellite = satellite
        self.sv_clock_bias = sv_clock_bias
        self.iode = iode
        self.crs = crs
        self.delta_n = delta_n
        self.m0 = m0
        self.cuc = cuc
        self.e = e
        self.cus = cus
        self.sqrt_a = sqrt_a
        self.ttoe = ttoe
        self.cic = cic
        self.big_omega = big_omega
        self.cis = cis
        self.i0 = i0
        self.crc = crc
        self.omega = omega
        self.omega_dot = omega_dot
        self.idot = idot
        self.codes_on_l2 = codes_on_l2
        self.gps_week = gps_week
        self.l2_p_data_flag = l2_p_data_flag
        self.sv_accuracy = sv_accuracy
        self.sv_health = sv_health
        self.tgd = tgd
        self.iodc = iodc
        self.ttom = ttom
