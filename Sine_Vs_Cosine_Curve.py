# For this project, you will have to generate a sine vs cosine curve. 
# You will need to use the numpy library to access the sine and cosine functions. 
# You will also need to use the matplotlib library to draw the curve. 
# To make this more difficult, make the graph go from -360° to 360°, with there being a 180° 
# difference between each point on the x-axis.

# References: 1. https://pythontic.com/visualization/charts/sinewave
#             2. https://www.mathopenref.com/triggraphcosine.html
#             3. https://pythonforundergradengineers.com/plotting-sin-cos-with-matplotlib.html

import numpy as np
import matplotlib.pyplot as plot

x = np.arange(-2*np.pi, 2*np.pi, 0.1) # Start, stop, step
y = np.sin(x)
y1 = np.cos(x)

plot.plot(x,y,x,y1)

plot.title('Sine Vs Cosine Curve')

plot.xlabel('x Values from -2pi to 2pi', color = 'b')

plot.ylabel('sin(X) and cos(x)', color = 'g')

plot.legend(['sin(x)','cos(y)'])

plot.grid(True, which='both')

plot.axhline(y = 0, color = 'b')

plot.axvline(x = 0, color = 'g')

plot.show()
