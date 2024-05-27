from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from machine import Machine

"""
на вход:
1) Qнорм, Qав
2) V0 = Qнорм + Qав
3)pmin
4) подача насоса выбирается из расчета на заданное время наполнения аккумулятора
"""
class EntryData(BaseModel):
    emergency_volume: int
    regular_volume: int
    filling_time: int

app = FastAPI()

@app.get("/") # view 
async def makeCalculation(target_volume: float, filling_time: float, pmin: float):
    machine = Machine(target_volume, filling_time, pmin)
    return {
        "Типоразмер": f"{machine.pump_name}",
        #"Нормальный расход":f"{machine.regular_volume}",
        #"Аварийный расход":f"{machine.emergency_volume}",
        "Уставка реле давления":f"{machine.p_plus}",
        "Объем котла": f"{machine.final_volume}",
        "Подача насоса": f"{machine.final_feed}"
    }

if __name__ == "__main__": 
    uvicorn.run("main:app", reload=True)
