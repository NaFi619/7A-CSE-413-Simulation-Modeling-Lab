import numpy as np
from sympy import Matrix
import matplotlib.pyplot as plt
import seaborn as sns

#Scalar & Array Operations
scalar =  3.7
arr = np.array([1.1, 2.5, -3, 4, 9,11])

# Trigonometric functions
sin_values = np.sin(arr)
cos_values = np.cos(arr)
tan_values = np.tan(arr)

# Display results
print("sin:", sin_values)
print("cos:", cos_values)
print("tan:", tan_values)