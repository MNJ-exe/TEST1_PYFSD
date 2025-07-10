from abc import ABC,abstractmethod
class Vehicles(ABC):
    @abstractmethod
    def set_vname(self,name):
        pass
class FleetVehicles(Vehicles):
    def set_vname(self,vname):
        self.__vname = vname
        return self.__vname
    # def b_name(self,bname):
    #     self.__bname = bname
    #     return self.__bname
    # def kmrun(self,kms):
    #     self.__kms = kms
    #     return self.__kms
class Car(Vehicles):
    def __init__(self,bname,kmrun,fuel):
        self.bname = bname
        self.kmrun = kmrun
        self.__fuel = 30
    def bname(self,name):
        self.bname = name
        print(f"Car Brand is : {self.bname}")
    def kmrun(self,kms):
        self.kmrun=kms
        print(f"Car KM run is : {self.kmrun}")
        if self.kmrun>5000:
            print("Needs Service.")
        else:
            print("Doesnot needs Service.")
            return self.kmrun
    def fuel(self,fuel):
        self.__fuel =fuel-(self.kmrun*0.05)
        print(f"Car Fuel  remaining : {self.__fuel}")
class Truck(Vehicles):
    def __init__(self,bname,kmrun,fuel):
        self.bname = bname
        self.kmrun = kmrun
        self.__fuel = fuel
    def bname(self,name):
        self.bname = name
        print(f"Truck Brand is : {self.bname}")
    def kmrun(self,kms):
        self.kmrun = kms
        print(f"Truck KM run is : {self.kmrun}")
        if self.kmrun>5000:
            print("Needs Service.")
        else:
            print("Doesnot needs Service.")
    def fuel(self,fuel):
        self.__fuel = fuel-(self.kmrun*0.05)
        print(f"Truck Fuel  remaining : {self.__fuel}")
class Bike(Vehicles):
    def __init__(self,bname,kmrun,fuel):
        self.bname = bname
        self.kmrun = kmrun
        self.fuel = fuel
    def bname(self,name):
        self.bname = name
        print(f"Bike Brand is : {self.bname}")
    def kmrun(self,kms):
        self.kmrun = kms
        print(f"Bike KM run is : {self.kmrun}")
    def fuel(self,fuel):
        self.fuel = fuel-(self.kmrun * 0.05)
        print(f"Bike Fuel  remaining : {self.fuel}")
class Cprint:
    # def __init__(self,bname,kmrun,fuel):
    #     self.bname = bname
    #     self.kmrun = kmrun
    #     self.fuel = fuel
    def bname(self,name):
        self.bname = name
        return self.bname
    def kmrun(self,kms):
        self.kmrun = kms
        return self.kmrun
    def fuel(self,fuel):
        self.fuel = fuel-(self.kmrun * 0.05)
        return self.fuel


        # c.bname=input("Enter the Brand of the car : ")
        # c.kmrun=int(input("Enter the KM run of the car : "))
        # c.fuel=int(input("Enter the Fuel of the car : "))
class Tprint:
    # def __init__(self,bname,kmrun,fuel):
    #     self.bname = bname
    #     self.kmrun = kmrun
    #     self.fuel = fuel
    def bname(self,name):
        self.name = name
        return self.name
    def kmrun(self,kms):
        self.kmrun = kms
        return self.kmrun
    def fuel(self,fuel):
        self.fuel = fuel-(self.kmrun * 0.05)
        return self.fuel

class Bprint:
    # def __init__(self,bname,kmrun,fuel):
    #     self.bname = bname
    #     self.kmrun = kmrun
    #     self.fuel = fuel
    def bname(self,name):
        self.bname = name
        return self.bname
    def kmrun(self,kms):
        self.kmrun = kms
        return self.kmrun
    def fuel(self,fuel):
        self.fuel = fuel-(self.kmrun * 0.05)
        return self.fuel

f=FleetVehicles()
vt=f.set_vname(input("Enter the type of the Vehicle : "))
if vt.lower() == "car":
    cp=Cprint()
    cname=cp.bname(input("Enter the Brand of the car : "))
    ck=cp.kmrun(int(input("Enter the KM run of the car : ")))
    cf=cp.fuel(int(input("Enter the Fuel of the car : ")))
    print("Car Brand is :",cname)
    print("Car Fuel is :",cf)
    print("KM run is :",ck)
    print(f"{cname} is a car.")
    if ck>5000:
        print("Needs Service.")
    else:
        print("Doesnot needs Service.")
elif vt.lower() == "truck":
    tp=Tprint()
    tname=tp.bname(input("Enter the Brand of the truck : "))
    tk=tp.kmrun(int(input("Enter the KM run of the truck : ")))
    tf=tp.fuel(int(input("Enter the Fuel of the truck : ")))
    print("Truck Brand is :",tname)
    print("Truck Fuel is :",tf)
    print("KM run is :",tk)
    print(f"{tname} is a truck.")
    if tk>5000:
        print("Needs Service.")
    else:
        print("Doesnot needs Service.")

else:
    bp=Bprint()
    bname=bp.bname(input("Enter the Brand of the bike : "))
    bk=bp.kmrun(int(input("Enter the KM run of the bike : ")))
    bf=bp.fuel(int(input("Enter the Fuel of the bike : ")))
    print("Bike Brand is :",bname)
    print("Bike Fuel is :",bf)
    print("KM run is :",bk)
    print(f"{bname} is a bike.")
    if bk>5000:
        print("Needs Service.")
    else:
        print("Doesnot needs Service.")

    # print(f"Car brand : {bname}")
    # if(kmrun>5000):
    #     print("Needs Service.")
    # else:
    #     print("Doesnot needs Service.")
    #