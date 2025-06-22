from Service.Ferrari import Ferrari
from Service.KIA import KIA
from Service.Suzuki import Suzuki


class Car():

    def temp(self):
        pass

Fr=Ferrari()
Sz=Suzuki()
Ka=KIA()

for cardata in (Fr,Sz,Ka):
    cardata.Car_Name()
    cardata.fuel_type()
    cardata.max_speed()

