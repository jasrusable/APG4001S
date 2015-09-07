import math
import numpy as np


gamma_E = 9.78032677150
K =0.001931851353
E2= 0.00669438002290

class TrigStation(object):
    def __init__(self,Lat,Long,r,LoBand,ElliHeight,geoHeight):
        self.Lat = math.radians(Lat[0] + Lat[1]/60.0 + Lat[2]/3600.0)
        self.Long = math.radians(Long[0] + Long[1]/60.0 + Long[2]/3600.0)
        self.r = math.radians(math.sqrt(r[0]**2+r[1]**2+r[2]**2))
        self.LoBand = math.radians(LoBand)
        self.ElliHeight = ElliHeight
        self.geoHeight = geoHeight

stations ={'HNUS':TrigStation([34,25,28.6671],[19,13,23.0264],[4973168.840,1734085.512,-3585434.051],19,63.048,32.17),
                  'PRET':TrigStation([25,43,55.2935],[28,16,57.4873],[5064032.237,2724721.031,-2752950.762],29,1387.339,24.84),
                  'RBAY':TrigStation([28,47,43.9616],[32,4,42.1896],[4739765.776,2970758.460,-3054077.535],33,31.752,23.54),
                  'TDOU':TrigStation([23,4,47.6714],[30,23,2.4297],[5064840.815,2969624.535,-2485109.939],31,630.217,13.08),
                  'ULDI':TrigStation([28,17,35.2196],[31,25,15.3309],[4796680.897,2930311.589,-3005435.714],31,607.947,26.60)}

for name, data in stations.items():
    Orth = data.ElliHeight - data.geoHeight
    Gamma = gamma_E * (1+K*(math.sin(data.Lat)**2))/(math.sqrt(1-E2*(math.sin(data.Lat)**2)))
    N_Gamma = Gamma -0.1543*Orth*(10**-5)
    

    Term = Orth * ((Gamma-N_Gamma)/Gamma)
    print(name,round(Term,5))
    