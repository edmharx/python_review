#ask what will be calculated
#ask the appropriate values
#print the missing value
#give option to do another computation
#while loop

def find_voltage(current, resistance):
    ans = current * resistance
    if current == 0 and resistance == 0:
        print ("The value of voltage is ", ans,". Circuit inactive")
    elif current == 0:
        print ("The value of voltage is ", ans,". Open cicuit")
    elif resistance == 0:
        print ("The value of voltage is ", ans,". Short circuit occurred")
    else:
        print("The value of voltage is ", ans)

def find_current(voltage, resistance):
    ans = voltage/resistance
    if voltage == 0 and resistance == 0:
        print ("The value of current is ", ans,". Undefined")
    elif voltage == 0:
        print ("The value of current is ", ans,". Open or inactive Circuit")
    elif resistance == 0:
        print ("The value of current is ", ans,". Short circuit occurred")
    else:
        print("The value of voltage is ", ans)

def find_resistance(current, voltage):
    ans = voltage/current
    if voltage == 0 and current == 0:
        print ("The value of current is ", ans,". Undefined")
    elif current == 0:
        print ("The value of current is ", ans,". Open Circuit")
    elif voltage == 0:
        print ("The value of current is ", ans,". Short circuit occurred")
    else:
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

else:
    print ("Type the corresponding number")


#what if a value is zero

