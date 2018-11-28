## How to resolve our merge conflicts with Jupyter Notebook

To resolve our merge conflicts, we will move your edited Jupyter notebooks to a new folder, disable the repository's Git functionality, reinitialize it and redownload all the files. Whenever you make edits to a notebook, you should make sure it gets saved into this new folder!

![image](https://i.dailymail.co.uk/i/pix/2015/03/15/26AA0E7100000578-2995909-image-a-35_1426444687120.jpg)

1. It'll make it easier for you in the long run to just keep your BridgeUp STEM GitHub repository on your Desktop. Move it there if you haven't already. The folder you see should be called "BridgeUP-STEM-Oceans-Six"

2. Open up Terminal, and use `cd` to navigate to your GitHub repository.

3. Type `mv jupyter-notebooks jupyter-notebooks-completed`. 
This `mv` command actually just renames your folder!

4. Type `rm -rf .git`. 
This disables your repository's Git powers. 

5. Type `git init`

6. Type `git remote add origin https://github.com/yourusername/BridgeUP-STEM-Oceans-Six.git`. 
Make sure to replace "yourusername" with your GitHub username! If this doesn't work, change the name of the repository after the username to "BridgeUP-STEM-Abbott.git".

7. Type `git remote add upstream https://github.com/amnh/BridgeUP-STEM-Oceans-Six.git`

8. `git add .`

9. `git commit -m 'insert your message here'`

10. `git pull origin master`

11. `git push origin master -f` 
The -f flag f forces this push request even if there are minor issues.

12. `git pull upstream master --allow-unrelated-histories` 
This resolves the different histories between the files in your folder and the repository we're pulling from.

13. Follow the usual `git add`, `git commit`, `push` to `origin master` commands. These should be second nature by now! If they're not, look at our [cheat sheet](https://github.com/amnh/BridgeUP-STEM-Oceans-Six/blob/master/coding_cheat_sheet.md)
