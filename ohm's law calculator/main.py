#ask what will be calculated
#ask the appropriate values
#print the missing value
#give option to do another computation
#while loop

def find_voltage(current, resistance):
    ans = current * resistance
    print("The value of voltage is ", ans)

def find_current(voltage, resistance):
    ans = voltage/resistance
    print("The value of voltage is ", ans)

def find_resistance(current, voltage):
    ans = voltage/current
    print("The value of voltage is ", ans)


print ("Welcome to ohm's law calculator\n\nChoose what value to find\n\n1. Voltage\n2. Current\n3. Resistance\n")
to_find = int(input("Select the corresponding number"))

if to_find == 1:
    current = float(input("Current: "))
    resistance = float(input("Resistance: "))
    find_voltage(current, resistance)

elif to_find == 2:
    voltage = float(input("Voltage: "))
    resistance = float(input("Resistance: "))
    find_current(voltage, resistance)

elif to_find == 3:
    current = float(input("Current: "))
    voltage = float(input("Voltage: "))
    find_resistance(current, voltage)



#not in the selection
#what if a value is zero

