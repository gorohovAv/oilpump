
"""
на вход:
1) Qнорм, Qав
2) V0 = Qнорм + Qав
3)pmin
4) подача насоса выбирается из расчета на заданное время наполнения аккумулятора
"""
class Machine: # стр 23
    table = { # стр 20
        'p20': {}, 
        'p25': {},
        'p40': {},

    }
    def __init__(self, emergency_volume, regular_volume, filling_time, pmin):
        self.emergency_volume = emergency_volume
        self.regular_volume = regular_volume
        self.filling_time = filling_time
        self.pmin = pmin

        self.relation = self.emergency_volume / self.regular_volume
        self.p_plus = self.pmin*0.92 - 0.25
        #self.air_volume =
         



        


