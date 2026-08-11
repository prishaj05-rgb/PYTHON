#create class
class vehicle:

    #create init method
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

#modelx = Vehicle
modelx = vehicle(240, 18)

#access the variables inside init method
print("Model Max Speed: ", modelx.max_speed)
print("Model Mileage: ", modelx.mileage)