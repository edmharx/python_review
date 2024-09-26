#request user to input a number
#ask the user if celsius to fahrenheit or vice versa
#verify if the input is a float or int
#convert
#print answer
#give option to do another conversion
#put in while loop


num = float(input("Input the temperature to convert: "))
temp = input("Choose your conversion method: ")
choices = ["celsius to fahrenheit", "fahrenheit to celsius"]

def celsius_to_fahrenheit(to_convert_ct):
    ans = to_convert_ct * (9/5) + 32
    print ("The answer is ",ans)

def fahrenheit_to_celsius(to_convert_tc):
    ans = (to_convert_tc - 32) * 5/9
    print ("The answer is ",ans)

while True:
    if temp.lower in choices and temp == 1 or 2:
        break
    else:
        print ("Type the conversion method or simply type the number: ")

if temp == 1 or temp == choices[0]:
    celsius_to_fahrenheit(num)
elif temp == 2 or temp == choices[1]:
    fahrenheit_to_celsius(num)

