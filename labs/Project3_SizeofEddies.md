# Project 2: Calculating the size of eddies
### Team members: Emily and Diana

### Mission: Write a script that calculates the area of our eddies (and possibly the center, too!)

You'll start with a dataframe containing closed contour paths and levels (this is the output of our eddy identification algorithm that you have already created). From this dataframe, can you use each contour path to calculate the area contained within the contour? You should return this value as a separate column within the dataframe (so each row contains the contour level/height, the contour path, and the size of the contour/eddy).

![](http://tornado.sfsu.edu/geosciences/classes/m407_707/Monteverdi/Satellite/Oceanography/eddy_files/image003.jpg)

Ultimately, you'll be combining this script with your fellow interns' work on the other projects, so make sure it can be easily adapted to others' code (i.e., you can copy the relevant sections of your script into someone else's code, and it will still work).

Resources:
- This [StackOverflow post](https://stackoverflow.com/questions/22678990/how-can-i-calculate-the-area-within-a-contour-in-python-using-the-matplotlib) might help. This equation comes from a really neat multivariable calculus theorem (you don't need to understand it to apply it, but it's cool to know!) 

- Remember that our coordinates are in degrees — how can you convert this into meters? The [Haversine formula](https://stackoverflow.com/questions/4913349/haversine-formula-in-python-bearing-and-distance-between-two-gps-points) is useful.

Additional challenge:
Can you find the center (or centroid/center of mass, since these are irregular shapes). 
Here's one [StackOverflow post](https://stackoverflow.com/questions/48168880/finding-the-center-of-a-contour) with some insight, and here is [another post](https://stackoverflow.com/questions/5271583/center-of-gravity-of-a-polygon) These tools all make use of some simple geometry! 

Good luck!


