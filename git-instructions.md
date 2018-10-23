**Instructions**

1. Log into GitHub on your browser, and navigate to [https://github.com/amnh/BridgeUP-STEM-Oceans-Six](https://github.com/amnh/BridgeUP-STEM-Oceans-Six). This is, of course, the repository where we will store all of our codes etc.
2. Navigate to the right side of the window and click on &quot;Fork.&quot; This will save a new copy of the repository to your own GitHub account.

![fork a repo](https://github.com/amnh/BridgeUP-STEM-Oceans-Six/blob/master/photos/fork.png)

3. Open up Terminal. Decide where you want to store your GitHub repository on your computer, and navigate to that place. For example, I made a new folder called GitHub in my documents, and I store all everything GitHub-related there.
    * Remember: to change folders, type **cd** , followed by the name of the folder you want to go to. i.e. for me, I type cd Documents/GitHub
    * Other tips:
      * **ls** shows all the files in your folder/directory.
      * **cd ..** moves you up one folder
      * **cd** (without any names after it) takes you to your home directory
      If you need more of a refresher, check out this handy [terminal cheat sheet](https://www.techrepublic.com/article/16-terminal-commands-every-user-should-know/)
4. Once you're in the right location, you&#39;ll clone your repository. This adds a local copy to your own computer, and you can make changes there! In Terminal, type **git clone \<url\>**, where **\<url\>** is the URL of your forked repository.
    * To find this URL, go to your GitHub account, open the repositories tab, find the forked repository, and click on the green button on the right side that says, \"Clone or download.\" Copy the URL it gives you.
    ![clone url](https://github.com/katyabbott/BridgeUP-STEM-Oceans-Six/blob/master/photos/clone.png)
  Make sure you're cloning your _forked_ repository, not the original! You can tell because in the top left corner, where it says the name of the repository, it will also have a description that identifies where it was forked from.
  ![forked from](https://github.com/amnh/BridgeUP-STEM-Oceans-Six/blob/master/photos/forked_from.png)


5. When you clone a repository, GitHub automatically creates a _remote_ called _origin_ that lets you interact with the online repository and make or download changes. Type **git remote -v** in Terminal to see a list of your remotes.
6. Add me as a collaborator to your repository — that way, I'll be able to see your work and integrate it into the main repository. Under settings in your repository, visit "Collaborators & teams" and add my username (katyabbott) into the "Add collaborators" box. 
![git remotes](https://github.com/amnh/BridgeUP-STEM-Oceans-Six/blob/master/photos/collaborate.png)
7. Now, we'll add a new remote that points to the original repository — the one that you forked your own repository from. This way, if any changes are made to that original repository, you will be able to download them.
    * Type **git remote add upstream** **https://github.com/amnh/BridgeUP-STEM-Oceans-Six** in Terminal.
    * Now, type **git remote -v** again. You should see two remotes: One called **origin** that points to your own repository, and one called **upstream** that points to the original.
    ![git remotes](https://github.com/amnh/BridgeUP-STEM-Oceans-Six/blob/master/photos/remotes.png)
8. Create a new **branch** in your repository. This allows you to make changes to your repository (i.e. to edit Jupyter Notebooks or write new code) without changing the main, master branch.
    * Type **git checkout -b \<branch\-name\>**. This creates a new branch _and_ switches you over to that new branch in git.
9. Practice making a change to your repository and pushing that change: In the exquisite-corpse folder, open **story1.txt** and write your name.
10. Now, add the change to your repository:
    * Type **git add story1.txt**. This lets git know you're ready to make a change
    * Type **git commit -m** \"\<Your message here\>\". Change \[Your message here\] to explain why you&#39;re making the change – i.e. &quot;Adding in my name&quot; etc.
    * Congrats! You&#39;ve just made your first commit to this repo 🎉🎉🎉
11. Next, you&#39;ll upload this change to your online repository. Type **git push origin \<branch-name\>**. This tells git to send the changes you made on your **branch** to the repository that your **origin** remote points to.
12. Lastly, let&#39;s check to see if any changes have been made to the upstream repository that you might want to **fetch** and **merge** into your master branch. This won&#39;t merge these changes into your newly created branch – you will have to do that separately.
    * Type **git fetch upstream.** This fetches the changes made so you can see what&#39;s new.
    * Type **git checkout master**. This guarantees you can make changes on the **master** branch.
    * Type **git merge upstream/master**. This tells git to merge the new changes from **upstream** into **master**.



**Cheat sheet** :

- To clone a repository: **git clone \<url\>**
- To add a new remote: **git add remote \<name\> \<url\>**
- To see your remotes: **git remote -v**
- To add a change: **git add \<file-name\>**
- To checkout (switch to) a new branch: **git checkout \<branch-name\>**
- To delete an existing branch (be careful – you may lose your changes!): **git branch -d \<branch-name\>**
- To commit that change: **git commit -m \"message\"**
- To push those changes to your remote repository: **git push origin master**
  - If you&#39;re working on a different branch or remote (not master or origin): **git push \<remote-name\> \<branch-name\>**
- To sync your forked repository with any changes made to the original:
  - **git fetch upstream**
  - **git checkout master** (replace **master **with your** \<branch-name\>** if you want to merge changes with another branch)
  - **git merge upstream/master** (replace **master **with your** \<branch-name\>** if you want to merge changes with another branch)
