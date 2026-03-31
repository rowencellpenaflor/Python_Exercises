
"""
Write a module that defines the following functions:

Functions that convert metric and imperial units."""

def cel2fah(c):
    # Converts a temperature in Celsius to Fahrenheit.
    return 9/5 * c + 32
    
def fah2cel(f):
    # Converts a temperature in Fahrenheit to Celsius.
    return 5/9 * (f - 32)

def km2mi(km):
    # Converts a distance in kilometers to miles.
    return km / 1.60934

def mi2km(mi):
    # Converts a distance in miles to kilometers.
    return mi * 1.60934