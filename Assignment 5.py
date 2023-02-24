#list of cars avialable and their prices
cars = {"Mercedes":28000, 
        "Altima":5000,
        "Trackhawk":50000,
        "saburu":3500,
        "Yaris":2500,
        "vitz":2000,
        "Range Rover":42000,
        "Maybach":52000,
        "Infinity":15000,
        "Grand Cherokee":30000,
        "Honda Civic":18000,
        "Accord":21000,
        "Bentley":65000,
        "Corrola":12000,
        "Optima":14000,
        "Discovery":22000,
        "Cadillac":45000,
        "Porsche":105000,
        "Lamborghini":250000,
        "Ferrari":280000,
        "Peugeot":35000,
        "Prado":30000,
        "lexus":38000,
        "Crysler":35000,
        "G-Wagon":120000,
        "Brabus":135000,
        "BMW":85000,
        "Camaro":65000,
        "Dodge":140000,
        "Aston Martin":180000,
        "Tesla":45000,
        "Pontiac":15000,
        "Mclaren":250000,
        "Optima":14000,
        "Cullinan":350000}
#user input for car name
car_name = input("Please enter car_name:")

#crosscheck car name with list of cars avialable
if car_name in cars:
    print("Yes")
    #if car name is present,get its price
    car_price = cars[car_name]
    print(" {car_name} is ${carprice}." )
else:
    #if car name is not present, inform the user
    print("sorry,{car_name} is not available.")













