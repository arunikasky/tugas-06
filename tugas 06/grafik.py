import numpy as np
from scipy import integrate
import matplotlib.pyplot as plotlib

#define parameter
x_start = 0                 #interval awal
x_stop = 3.14                  #interval akhir
x_steps_interval = 0.01     #besar step

#define an array of data points
x_values = np.arange (x_start, x_stop, x_steps_interval)
y_values = (x_values**2*np.cos(x_values)) + (3*np.sin(2*x_values))

#plotlib
plotlib.plot(x_values, y_values)

#define a lambda function for integration
integration_function = lambda x:(x**2*np.cos(x)) + (3*np.sin(2*x))

#integral ignoring error 
integral, _= integrate.quad(integration_function, x_start, x_stop)

#output
print("Integral Value", integral)

#plot
plotlib.xlabel('x')
plotlib.ylabel('f(x)')
plotlib.title('Plot of f(x) = x**2*np.cos(x) + 3*np.sin(2*x)')
plotlib.show()
