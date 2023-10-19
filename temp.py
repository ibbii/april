"""
Program to Convert Celcius To Fahrenheit
"""

def celcius_to_fahrenheit(celcius):
    """ convert value given to fahrenheit """
    fah = celcius * 9/5 + 32
    return fah

def Fahrenheit_to_celcius(fahrenheit):
    """ convert value given to celcius """
    celcius = fahrenheit - 32
    return celcius

celcius = 25
fah = celcius_to_fahrenheit(celcius)
print(f"{celcius} degrees is {fah} Farenheit")

celcius = Fahrenheit_to_celcius(fah)
print(f"{fah} degrees Fahrenheit is {fah} Celcius")

