
"""
на вход:
1) Qнорм, Qав
2) V0 = Qнорм + Qав
3)pmin
4) подача насоса выбирается из расчета на заданное время наполнения аккумулятора
"""
class Pump:
    def __init__(self, name, va, qn):
        self.name = name
        self.va = va
        self.qn = qn


class Machine: # стр 23
    def makePumps(self):
        pumps = [
            Pump('МНУ 1', 1, 3.47),
            Pump('МНУ 1,6', 1.6, 3.47),
            Pump('МНУ 2,5', 2.5, 6.95),
            Pump('МНУ 4', 4, 6.95),
            Pump('МНУ 5,6', 5.6, 8.9),
            Pump('МНУ 8', 8, 8.9),
            Pump('МНУ 10', 10, 13.9),
            Pump('МНУ 12,5', 12.5, 13.9),
            Pump('МНУ 16', 16, 17.5),
            Pump('МНУ 20', 20, 17.5),
            Pump('МНУ 25', 25, 27.8),
            Pump('МНУ 30', 30, 27.8),
        ]
        return pumps
    
    def selectPump(self, pumps, target, filling_time):
        for pump in pumps:
            if ((pump.qn) >= (target*1000)/filling_time):
                return pump
        return Pump('МНУ 30', 30, 27.8)
    
    def __init__(self, target_volume, filling_time, pmin):
        self.emergency_volume = target_volume*1.5
        self.regular_volume = target_volume*2.5
        self.filling_time = filling_time
        self.pmin = pmin
        self.pumps = self.makePumps()

        self.selected_pump = self.selectPump(self.pumps, self.regular_volume, self.filling_time)
        self.pump_name = self.selected_pump.name

        self.relation = self.emergency_volume / self.regular_volume
        self.p_plus = self.pmin*0.92 - 0.25
        self.final_volume = self.selected_pump.va # м^3
        self.final_feed = (self.regular_volume*1000/60)/self.filling_time # л/с
    
    
        
         



        


