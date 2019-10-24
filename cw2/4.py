def my_function(temperature, temperature_type):
    temp = 0
    # if params valid
    if temperature < -273:
        return Exception("Temperature does not exist")
    elif temperature_type not in ["kelvin", "fahrenheit", "rankine"]:
        return Exception("You need to choose one of (kelvin, fahrenheit, rankine)")
    # calc
    if temperature_type.lower() == "fahrenheit":
        temp = (temperature * 1.8) + 32
    elif temperature_type.lower() == "kelvin":
        temp = temperature + 273.15
    elif temperature_type.lower() == "rankine":
        temp = (temperature + 273.15) * 1.8
    return temp


print(my_function(15, "fahrenheit"))
print(my_function(15, "kelvin"))
print(my_function(15, "rankine"))
print(my_function(15, "oooo"))
print(my_function(-500, "kelvin"))
