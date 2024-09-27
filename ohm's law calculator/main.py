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