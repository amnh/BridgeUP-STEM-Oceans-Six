## Put your import statements here.
## What packages do you want to import?
import numpy as np

## practice
lat = [32, 32.2, 32.4, 32.6, 32.8, 33., 33.2, 33.4, 33.6, 33.8, 34.]
lon = [294, 294.2, 294.4, 294.6, 294.8, 295, 295.2, 295.4, 295.6, 295.8, 296]
sla = np.random.randn(11,11)

### Challenge 1
## Given the above latitudes, longitudes and sea level anomaly
## grid, do the following:
    #A) Make a contour plot of the sla dataset
    #B) Make a filled in contour plot, and add a colorbar
    #C) Create custom levels for the contour plot that are
    # evenly spaced at 0.25 meters apart and cover the entire range of sla
    # (i.e.) there are contour lines even at the max/min heights
    #hint: np.arange may help with this: https://www.sharpsightlabs.com/blog/numpy-arange/
    #D) save your plots to your repository
    #E) How many "eddies" do you see?
    
### Challenge 2
## Load in our dataset of SLA in Bermuda, and repeat
## exercises A-E for the entire dataset region. Pick a single day
## of SLA. 

## Bonus points if you make the day index a variable (like
## our plotting function) so you can easily change it to see different
## contour maps for different days

