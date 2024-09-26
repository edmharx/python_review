#request user to input a number
#ask the user if celsius to fahrenheit or vice versa
#verify if the input is a float or int
#convert
#print answer
#give option to do another conversion
#put in while loop


num = float(input("Input the temperature to convert"))
temp = input("Choose your conversion method")

def celsius_to_fahrenheit(to_convert_ct):
    ans = to_convert_ct * (9/5) + 32
    print (ans)

def fahrenheit_to_celsius(to_convert_tc):
    ans = (to_convert_tc - 32) * 5/9
    print (ans)

while True:
    if temp == 1 or 2