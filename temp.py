"""
Program to Convert Celcius To Fahrenheit
"""

def celcius_to_fahrenheit(celcius):
    """ convert value given to fahrenheit """
    fah = celcius * 9/5 + 32
    return fah


celcius = 25
fah = celcius_to_fahrenheit(celcius)
print(f"{celcius} degrees is {fah} Farenheit")

