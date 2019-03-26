## Put your import statements here.
## What packages do you want to import?
import numpy as np
import matplotlib.pyplot as plt

## practice
lat = [32, 32.2, 32.4, 32.6, 32.8, 33., 33.2, 33.4, 33.6, 33.8, 34.]
lon = [294, 294.2, 294.4, 294.6, 294.8, 295, 295.2, 295.4, 295.6, 295.8, 296]
sla = np.random.randn(11,11)

### Challenge 1
## Given the above latitudes, longitudes and sea level anomaly
## grid (do these look familiar?), do the following:
    #A) Make a contour plot of the data, using levels evenly spaced every 0.25 meters. 
    # Make sure to save the plot as a variable.
    #B) Following the steps in Contours_with_matplotlib_part2.ipynb:
    #a) Access the set of contours associated with the fifth contour value. (i.e.,
    # all contours lines that have the same value as the fifth value in levels)
    #b) What is the contour value for these contours?
    #c) Access the first contour line in this set of contour lines and plot it. 
    # Is it closed or open? (i.e, do the ends meet?) Can you think of a Pythonic way 
    # to test if it is closed or open?
    #d) Try plotting all the contour lines with this particular contour value. 
    
#If you're confused, try working through the same lines of code used in Contours_with_matplotlib_part2.ipynb, 
## but replaced the contour set used there with this contour set of lat, lon and sla.

