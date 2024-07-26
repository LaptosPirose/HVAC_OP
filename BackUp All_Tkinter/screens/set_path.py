# Import libraries to manipulate PTATH
import sys
import os

"""
    Set the project absolut path
    @path: the actual sboslut project path
    @Angelo Moura
    julho 2024
"""


# Define actual project path
path = os.path.abspath(os.curdir)

# Show the path
print(f'Setting PATH {path}.')

# Include to system path
sys.path.insert(1, path)
