import numpy as np
from scipy.integrate import quad
import random
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

# Example for Monte Carlo method.
point_in=0
point_out=0
for i in range(10000):
    x=random.uniform(0,1)
    y=random.uniform(0,1)
    if y<=np.sqrt(1-x**2):
        point_in=point_in+1
    else:
        point_out=point_out+1
pi=4*point_in/(point_out+point_in)
print(pi)


