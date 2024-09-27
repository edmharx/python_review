#request user to input a number
#ask the user if celsius to fahrenheit or vice versa
#verify if the input is a float or int
#convert
#print answer
#give option to do another conversion
#put in while loop

def celsius_to_fahrenheit(to_convert_ct):
    ans = to_convert_ct * (9/5) + 32
    print ("The answer is ",ans)

def fahrenheit_to_celsius(to_convert_tc):
    ans = (to_convert_tc - 32) * 5/9
    print ("The answer is ",ans)


num = float(input("Input the temperature to convert: "))
temp = int(input("Choose your conversion method: "))
print ()
print ("1. Celsius to Fahrenheit")
print ("2. Fahrenheit to Celsius")

if temp == 1 or temp == 2:
    if temp == 1:
        celsius_to_fahrenheit(num)
    elif temp == 2:
        fahrenheit_to_celsius(num)
else:
    print ("Type the corresponding conversion method")

