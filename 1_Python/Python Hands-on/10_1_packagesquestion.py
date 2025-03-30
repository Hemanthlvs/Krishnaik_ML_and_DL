''' Assignment 7: Working with the `sys` Module

Use the `sys` module to print the Python version currently in use 
and the command-line arguments passed to the script.'''

import sys

print(sys.version)

print(f"these are the arguments that are passed: {sys.argv}")

for i, arg in enumerate(sys.argv): 
    print(f"Argument {i}: {arg}")
