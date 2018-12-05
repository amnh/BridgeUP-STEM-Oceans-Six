# Ocean's Six Coding Cheat Sheet

## Tips
- Brackets (<>) indicate that you should replace the brackets and words inside with your own input
- Spaces are very important in coding! 
  - Terminal/bash scripts use a lot of spacing between commands. i.e. `git pull upstream master`
  - In Python, there are very few spaces needed. i.e. `np.array([[1,2,3], [2,3,4]])`
- Frequently, my own coding errors come from adding a space when there shouldn't be one (or vice versa) or mispelling something.
  
## Numpy Arrays
- Remember, all arrays begin at the 0 index! So `a[0]` picks the first element, `a[1]` picks the second, and so on
- In these tips, `a`, `b` and `c` refer to different numpy arrays.
### 1D arrays
- This command selects everything: `a[:]`
- This command selects the 0th, 1st and 2nd rows (does not select the 3rd row): `a[0:3]`
  - The numbers inside the brackets can be changed to select whatever values you want.
### 2D arrays
- This command selects all rows and all columns: `b[:,:]`
- This command selects all rows, and the zeroth column: `b[:,0]`
- This command selects the zeroth row, and all columns in that row: `b[0,:]`
- This column selects the zeroth and first row, but NOT the second. It includes all the columns in that row: `b[0:2,:]` 
### 3D arrays
Technically, the first dimension is known as the row, the second as column and the third as depth, but I find that confusing. We'll call the first dimension the "group," the second "row," and third, "column" (as usual).
- This command selects everything. `c[:,:,:]` #This command selects everything.
- This command selects the 0th group, and all rows/columns in that group: `c[0,:,:]`
- This command selects the 0th row from every group: `c[:,0,:]`
- This command selects the 0th row from every group: `c[:,:,0]`
- This command tells you the shape of your array: `c.shape`
  - The first value is the size of the first dimension, and so on

## NetCDF files
[This tutorial](http://www.ceda.ac.uk/static/media/uploads/ncas-reading-2015/10_read_netcdf_python.pdf) was written in Python 2.7, so the print command is slightly different, but it's a helpful read to understand how these files work.

Follow these first steps in order:
1. Import the tools to open a dataset: `from netCDF4 import Dataset`
2. Open a dataset: `dataset = Dataset('path/to/filename.nc')`

Use these tools in any order: 
- View the dataset's attributes: `dataset.ncattrs()`
- Access a specific attribute: `dataset.attribute_name`
- View the dataset's dimensions: `dataset.dimensions`
- View a specific dimension: `dataset.dimensions['name of dimension']`
- View the dataset's variables: `dataset.variables`
- View a specific variable: `dataset.variables['name of variable']`
- See a variable's values: `dataset.variables['name of variable'][ : ]`


## Terminal
- To show all the files in the folder you're in: `ls`
- To navigate to a new folder: `cd <path name>` (enter the name of the folder or [path to the folder](http://www.mactips.info/2011/11/how-to-read-and-write-a-filepath))
- To navigate to the home director: `cd `
- To navigate to the previous folder: *cd ..*
- To open a file: open <file name>
- To find the path of a file: Find the file in Finder, then drag it into the Terminal window. The path will automatically appear!


## Git
- To clone a repository: `git clone <url>`
  (i.e., copy all files from an online repository to a folder on your computer)
- To add a new remote: `git add remote <name> <url>`
    (i.e., connecting your local repository (on your computer) to a remote repository (online)
- To see your remotes: `git remote -v`
- To add a change: `git add <file-name>`
    (i.e., you've edited a file and want to make Git aware of those changes)
- To commit that change: `git commit -m "message"`
    (this makes your changes official. It's basically like "saving" your work to Git.)
- To push those changes to your remote repository: `git push origin master`
     (i.e., sending any updated files to your online repository)
- To sync your forked repository with any changes made to the original: `git pull upstream master`
      (i.e., you're adding any new files from the main online repository to your computer)
