import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

sat_num = '22'

with open("data/igs18540.sp3", 'r') as f:
    Lr1 = []
    for line in f:
        if line[2:4] == sat_num:
            x = float(line[6:18])
            y = float(line[18:32])
            z = float(line[32:46])
            rad1 = np.array([x, y, z])
            rad1_sq = np.sqrt((rad1**2).sum())
            Lr1 += [rad1_sq]
            precise = np.array(Lr1) * 1000

with open("data/brdc2000.15n", 'r') as f:
    lr2 = []
    count = []
    numline = f.readlines()
    for i in range(len(numline)):
        if numline[i][0:2] == sat_num:
            if numline[i][12:14] == '18':
                hours = float(numline[i][12:14])
                minutes = float(numline[i][15:17])
                seconds = float(numline[i][19:22])
                Total_sec = float(hours*3600 + minutes*60 + seconds)
                SV_clock_bias = float(numline[i][22:41].replace('D', 'e'))
                SV_clock_drift = float(numline[i][41:60].replace('D', 'e'))
                SV_clock_drift_rate = float(numline[i][60:79].replace('D', 'e'))

                iode = float(numline[i+1][3:22].replace('D', 'e'))
                crs = float(numline[i+1][22:41].replace('D', 'e'))
                deltaN = float(numline[i+1][41:60].replace('D', 'e'))
                mo = float(numline[i+1][60:79].replace('D', 'e'))

                cuc = float(numline[i+2][3:22].replace('D', 'e'))
                ecc = float(numline[i+2][22:41].replace('D', 'e'))
                cus = float(numline[i+2][41:60].replace('D', 'e'))
                sqa = float(numline[i+2][60:79].replace('D', 'e'))

                ttoe = float(numline[i+3][3:22].replace('D', 'e'))
                cic = float(numline[i+3][22:41].replace('D', 'e'))
                omega = float(numline[i+3][41:60].replace('D', 'e'))
                cis = float(numline[i+3][60:79].replace('D', 'e'))

                io = float(numline[i+4][3:22].replace('D', 'e'))
                crc = float(numline[i+4][22:41].replace('D', 'e'))
                omega = float(numline[i+4][41:60].replace('D', 'e'))
                omega_dot = float(numline[i+4][60:79].replace('D', 'e'))

                IDOT = float(numline[i+5][3:21].replace('D', 'e'))
                L2 = float(numline[i+5][22:41].replace('D', 'e'))
                GPS_W = float(numline[i+5][41:60].replace('D', 'e'))
                L2_P = float(numline[i+5][60:79].replace('D', 'e'))

                SV_Acc = float(numline[i+6][3:22].replace('D', 'e'))
                SV_Health = float(numline[i+6][22:41].replace('D', 'e'))
                TGD = float(numline[i+6][41:60].replace('D', 'e'))
                IODC = float(numline[i+6][60:79].replace('D', 'e'))

                TTOM = float(numline[i+7][4:22].replace('D', 'e'))
                FI = float(numline[i+7][4:22].replace('D', 'e'))

                m = 3.986008*10**14
                omega_dote = 7.292115167*10**-5
                a = (sqa)**2
                n0 = np.sqrt(m / (a**3))
                n = n0 + deltaN
                Mk1 = mo - n * ttoe
                time = 0
                for j in range(0, 96):
                    time = j * 900
                    tk = time - ttoe
                    mk = mo + n * tk
                    k = 0
                    while k < 5:
                        if k == 0:
                            ek = mk + ecc*np.sin(mk)
                        else:
                            ek = mk + ecc*np.sin(ek)
                        k += 1

                    v_k = np.arctan(
                        ((np.sqrt(1 - ecc**2)*np.sin(ek))/(1 - ecc*np.cos(ek)))
                        / ((np.cos(ek)-ecc)/(1 - ecc*np.cos(ek)))
                    )

                    phi_k = v_k + omega
                    di_uk = cus*np.sin(2*phi_k) + cuc*np.cos(2*phi_k)
                    di_rk = crc*np.cos(2*phi_k) + crs*np.sin(2*phi_k)
                    di_ik = cic*np.cos(2*phi_k) + cis*np.sin(2*phi_k)

                    uk = phi_k + di_uk
                    rk = a * (1 - ecc * np.cos(ek)) + di_rk
                    ik = io + di_ik + (IDOT)*tk

                    x_k = rk * np.cos(uk)
                    y_k = rk * np.sin(uk)

                    omega_k = omega + (omega_dot - omega_dote) * tk - omega_dote * ttoe

                    XK = x_k * np.cos(omega_k) - y_k * np.cos(ik)*np.sin(omega_k)
                    YK = x_k * np.sin(omega_k) + y_k * np.cos(ik)*np.cos(omega_k)
                    ZK = y_k * np.sin(ik)

                    rad2 = np.array([XK, YK, ZK])
                    rad2_sq = np.sqrt((rad2**2).sum())
                    lr2 += [rad2_sq]
                    broadcast = np.array(lr2)

                count += [hours]
                length = len(count)
                llr1 = length * Lr1
                vllr1 = np.array(lr2)
                r = precise - broadcast

                counter = []
                for c in range(1, 97):
                    counter += [c]
                t = r[:96]
                fig, ax = plt.subplots()
                plt.plot(counter, t, '-', color='black')
                plt.ylim([-100, 100])
                plt.title("Radial Difference")
                plt.plot()
                plt.show()
