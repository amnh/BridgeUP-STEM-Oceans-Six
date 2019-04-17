# Project 2: Removing "eddies inside eddies"
### Team members: Tasluba and Thais

### Mission: Write a script that removes so-called "eddies inside eddies" — an artifact of the contouring process.

You'll start with a dataframe containing contour paths and levels (this is the output of our eddy identification algorithm that you have already created). From this dataframe, can you figure out how to remove all inner contour lines (all contour lines that are contained by another contour line)?

Your output would ideally be another dataframe that **only** shows the contours that are not contained within other contours.

This is an example of your starting point:

![](https://raw.githubusercontent.com/amnh/BridgeUP-STEM-Oceans-Six/master/photos/contours_inside_contours.png?token=AJSRWDWTXQGSO3IATORV32K4YDCZM)





Resources:
- There is a function in Matplotlib called [`contains_path()`](https://github.com/matplotlib/matplotlib/blob/714d18788320325d0bff75184f62d472f67ceb91/lib/matplotlib/path.py#L515) that you will find useful. It is a dot function (so given a path object called `path1`, like the ones in our dataframe, contained inside of `path2`, we can use `path2.contains_path(path1)` and the function should return `True`). You can read more [here](https://matplotlib.org/api/path_api.html#matplotlib.path.Path.contains_path).



- [Nested for loops](https://www.poftut.com/how-to-create-nested-for-loops-in-python/) may be necessary. Here, you loop through two different lists simultaneously, with the values of one loop held constant while the other loop is run. [This post gives a good explanation](https://stackoverflow.com/questions/37135519/how-do-nested-for-loops-work).


- You might create a new column in your dataframe called "inner" or something similar that is `True` if that contour is contained within any other contours, or `False` if it is not. 

- You could also look into the [`.any()` command](http://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.any.html) in pandas. This checks if any element in the dataframe satisfies a certain condition and returns a column with True/False values.

There are a lot of different ways to tackle this project! Good luck!
