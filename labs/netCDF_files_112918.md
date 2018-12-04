# Diving into our dataset | 11-29-18

Today, we're going to use a new tool, Atom, to read, write and run our code! It's a lot like using a Jupyter notebook, but our product will be a script that we can run in Terminal or anywhere else. Atom also works with other coding languages, like R and C++, which is really neat.

1. Download [Atom here](https://atom.io/)
    - Once you have downloaded it, search for it in Finder. Drag it into your Applications folder.

2. Go to the Settings tab, then to Featured Packages, and install Hydrogen. This is an interactive code editor that allows us to run snippets of our code right in our editor. 

3. Quit Atom. Open your Terminal, and type these lines: <br/>
`conda install ipykernel` <br/>
`python -m ipykernel install --user`

4. Open up Atom again. You should be ready to rock and roll! Find the script we were working on two weeks ago, called netCDF_script_**yourinitials**.py, and drag it into Atom.

5. Let's play around with Atom! You can run individual lines by clicking on them and pressing `shift-enter`. You should see a little check mark next to the line if it has run successfully. Try writing a print statement and running that -- where does the output show up? 

6. In the .py file you have opened, there is an absolute path. Find it, and replace it with the absolute path to the "Bermuda_data_SLA.nc" file. (This is the file you downloaded on Tuesday -- you may have Slacked me the absolute path). This is our data for our project, and we'll be working with it for now on. 

If you need a quick refresher on absolute vs. relative paths: ![image](https://raw.githubusercontent.com/amnh/BridgeUP-STEM-Oceans-Six/master/photos/Screen%20Shot%202018-12-04%20at%203.46.26%20PM.png?token=AmUbDikUbpfR4wNk0exGv7aqvCHL2l-nks5cECINwA%3D%3D)

7. Time to explore our dataset! 

## Your mission: Work by yourself or with a partner to find out what the spatial coverage and resolution is for our dataset. (I.e, what is the minimum longitude? Max? Minimum latitude? Max? How many degrees between each point?). 
Once you have figured this out, try to draw it on a piece of paper!

![lat/lon](http://mrkash.com/activities/images/latitudelongitude.jpg)

**Bonus**: Figure out what the temporal coverage and resolution are (i.e. how many days does it span? What is the first and last day of measurement? How many days between each measurement?). Try to draw this as well.

Hints: 

- Use the first two lines of your code to import the dataset in Atom. Try using the `print` command on the dataset object to see what it tells you about our data. Then, explore the resources below. Try out different commands and see what your output is. 

- netCDF files contain "dimensions" and "variables." Can you find out what the difference is between the two? Which type do you want for this problem? (The answer may surprise you!)

Your resources:

- Use [this tutorial](http://snowball.millersville.edu/~adecaria/ESCI386P/esci386-lesson14-Reading-NetCDF-files.pdf) and [this tutorial](http://www.ceda.ac.uk/static/media/uploads/ncas-reading-2015/10_read_netcdf_python.pdf) to figure out what information our dataset contains. Make sure to write down any commands you use in your .py script file!

- This [cheat sheet](https://github.com/amnh/BridgeUP-STEM-Oceans-Six/blob/master/coding_cheat_sheet.md) may also be useful. You can also look at the [documentation for the netCDF4 package and the Dataset tool](http://unidata.github.io/netcdf4-python/).

- Additionally, Google is your friend! Try Googling with the key words (i.e. the coding language/coding package/output you're trying to find). 

## Reminder: Once you have finished working for the day, make sure to add and commit your changes with Git! 
