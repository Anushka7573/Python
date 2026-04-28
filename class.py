# class creation 

class vehicle:
    color="black" # attributes # default value 
    petrolordiesel="petrol" # attributes
    mileage="10" # attributes

    def start():
        print("when you press clutch and accelerator then vehicle is start")
# object creation
car = vehicle()
car.color="pink" 
print(car.color)

bike = vehicle()
print(bike.color)

aeroplane = vehicle()
print(aeroplane.mileage)
print(aeroplane.color)

# we created one class and 3 objects of that class 