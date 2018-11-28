# Diving into our dataset | 11-29-18

Today, we're going to use a new tool, Atom, to read, write and run our code! It's a lot like using a Jupyter notebook, but our product will be a script that we can run in Terminal or anywhere else. Atom also works with other coding languages, like R and C++, which is really neat.

1. Download [Atom here](https://atom.io/)
    - Once you have downloaded it, search for it in Finder. Drag it into your Applications folder.

2. Go to the Settings tab, then to Featured Packages, and install Hydrogen. This is an interactive code editor that allows us to run snippets of our code right in our editor. 

3. Quit Atom. Open your Terminal, and type these lines: 
`conda install ipykernel
python -m ipykernel install`

4. Open up Atom again. You should be ready to rock and roll! Find the script we were working on two weeks ago, called netCDF_script_yourinitials.py, and drag it into Atom.

5. Let's play around with Atom! You can run individual lines by clicking on them and pressing `shift-enter`. You should see a little check mark next to the line if it doesn't have any output. Try writing a print statement and running that -- where does the output show up? 

6. Replace the absolute path in your .py file that leads to the "sea_surface_temp.nc" file with the absolute path that leads to the "Bermuda_data_SLA.nc" file. (This is the file you downloaded on Tuesday -- you may have Slacked me the absolute path). This is our data for our project, and we'll be working with it for now on. 

7. [How to get them to start exploring on their own?]

Use these [tutorial](http://snowball.millersville.edu/~adecaria/ESCI386P/esci386-lesson14-Reading-NetCDF-files.pdf) to figure out what information our dataset contains. Your mission: Figure out what the latitude and longitude range is for our file (i.e., what is its spatial coverage) and what is the resolution (how many degrees between each point? Try to draw it.

Bonus points if you can figure out what the time range is, and resolution (how many days between measurements?). Try to draw this as well.
