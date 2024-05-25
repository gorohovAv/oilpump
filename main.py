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
async def makeCalculation(emergency_volume: float, regular_volume: float, filling_time: float):
    machine = Machine(emergency_volume, regular_volume, filling_time)
    return {
        "gfbdfbdfbdfbdf": f"gs{name}"
    }

if __name__ == "__main__": 
    uvicorn.run("main:app", reload=True)
