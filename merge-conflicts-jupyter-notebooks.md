## How to resolve our merge conflicts with Jupyter Notebook

![image](https://i.dailymail.co.uk/i/pix/2015/03/15/26AA0E7100000578-2995909-image-a-35_1426444687120.jpg)

1. It'll make it easier for you in the long run to just keep your BridgeUp STEM GitHub repository on your Desktop. Move it there if you haven't already. The folder you see should be called "BridgeUP-STEM-Oceans-Six"

2. Go ahead and open any Jupyter Notebook file in your jupyter-notebooks folder, using Sublime. (You may have to right-click). Notice that it doesn't look exactly like it does it your browser. This makes it difficult to find differences between two files that could be causing Git to report a merge issue. In addition, every time you run a Jupyter Notebook, it's modified slightly, and Git also can't handle that easily.

3. Open your terminal. Type `conda install nbdime`. This is a tool, like Git, that you can use to resolve merge conflicts easily.

4. Delete your branch. They aren't necessary for the work that we're doing and adding an additional layer of conflict. Remove the brackets (<, >) when you put in your branch name.
    - `git checkout master`

    - `git merge <put in name of branch>`
    
    If you can't remember the name of your branch (happens to the best of us!), type `git branch`. This will tell you the name of your active branches.

    - `git commit -m "Merging branches"`

    - `git branch -d <name of branch>`

5. `git status`. Do you have any files that need to be added?

    - `git add .`

    - `git commit -m "Message"`

    - `git push origin master`

6. `git pull upstream master`

    - (It will probably say Automatic Merge failed)

7. Type `nbdime mergetool`. This will open a new window with your jupyter notebook file that shows the difference.
![image](https://nbdime.readthedocs.io/en/stable/_images/nbdiff-web.png)

8. Decide how you want to resolve these conflicts. What are the differences between the files? Look for a little red triangular hazard sign. It's up to you to decide how to do this, but I usually try to include any lines that are different in both versions, to avoid future issues. 
Come talk to me if you're confused about how to resolve the two. Otherwise, you can just save and close.

9. Now, you should be all set!
