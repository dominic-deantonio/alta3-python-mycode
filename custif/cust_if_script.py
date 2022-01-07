#!/usr/bin/env python3
"""Dominic DeAntonio
   if, elif, else - A simple program using conditionals to make a decision."""



# wrap luminosity in a float() to accept decimals as numbers
print("Let's define the spectral type of a star based on its luminosity.")
luminosity = float(input("Enter luminosity between 0.01 and 100,000 and I will tell you its spectral type.\n"))

spectral_type = 'O'

# Check the user's input value
if luminosity >= 100000:
    spectral_type = 'O'
elif luminosity >= 1000:
    spectral_type = 'B'
elif luminosity >= 20:
    spectral_type = 'A'
elif luminosity >= 4:
    spectral_type = 'F'
elif luminosity >= 1.0:
    spectral_type = 'G'
elif luminosity >= 0.2:
    spectral_type = 'K'         
else:
    spectral_type = 'M'
print(f'Stars with luminosity of {luminosity} are spectral type {spectral_type}')
