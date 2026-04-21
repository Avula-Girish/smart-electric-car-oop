'''create a Smart Electric Car system using multiple inheritance. 
One parent should handle vehicle details like brand and speed, 
another parent should handle electric features like battery level and charging. 
The child class should combine both and allow the car to start, drive (reducing battery),
and recharge. Create an object and simulate these operations.'''


class Details:
    def __init__(self,brand,speed):
        self.brand=brand
        self.speed=speed
class Features:
    def __init__(self,battery,charging=False):
        self.battery=battery
        self.charging=charging
class Car(Details,Features):
        

    def __init__(self, brand, speed, battery):
        Details.__init__(self, brand, speed)
        Features.__init__(self, battery)
    def start(self):
        print(f"{self.brand} is started 🏎️🏎️🏎️")
    def drive(self,distance):
        self.distance=distance
        if(self.battery<self.distance):#1km 1percent usage 
            print("NO battery")
        else:
            self.battery-=self.distance
            if(self.battery<=5):
                print("battery low")
    def charge(self,time):#1 min 1 percent 
        self.charging=True
        self.time=time
        self.battery+=time
        if(self.battery>=100):
            print("Unplug ur charger")
            
    def display (self):
        print("+--------------------------------------+")
        print(f"| Brand    : {self.brand:<25}|")
        print(f"| Battery  : {str(self.battery)+'%':<25}|")
        print(f"| Speed    : {str(self.speed)+' km/h':<25}|")
        print(f"| Charging : {str(self.charging):<25}|")
        print("|                                     |")
        print("|                 🚘                   |")
        print("+--------------------------------------+")


c1=Car("BMW",150,80)

c1.start()
c1.drive(20)
c1.display()
c1.charge(20)
c1.display()

        

            
            
        
    
