# Assignment 1
# ICS3U
# <Alex Baksh>
# March 28, 2018

###### uncomment this when you are ready to work on it
def CtoF (C):
    F=(1.8)*C+32
    return F


###### uncomment this when you are ready to work on it
def FtoC (F):
    C = (0.55556)*(F-32)
    return C
    
#temperature = int(input('Enter your temperature in Celsius: '))
#print(CtoF(temperature))

print('Enter 1 for Celsius to Fahrenheit, enter 2 for Fahrenheit to Celsius')
choice = int(input())
temperature = int(input())

if choice == 1 and temperature <-273.15:
    print('temperature must be above -273.15')
else:
    temperature = CtoF(temperature)
    print(round(temperature))


if choice == 1:
    temperature = CtoF(temperature)
    print(round(temperature))
elif choice == 2:
    temperature = FtoC(temperature)
    print(round(temperature))
else:
    print('please enter 1 or 2')
        
    
