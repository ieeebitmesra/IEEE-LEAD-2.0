## Submitting your Projects

Before you get started, these are the steps that you need to follow only ONCE at the begining:
- [Fork this repository](https://docs.github.com/en/github/getting-started-with-github/fork-a-repo#fork-an-example-repository) so that you can make your changes without affecting the original project until you're ready to merge them.
- Go to your forked repository. Notice that the end of the URL should resemble `<your_github_username>/IEEE-LEAD-2.0`.
- Clone your forked repository: Click on the green `Code` button and copy the `HTTPS` URL of the repository.
    - Now, open `gitbash`(or `Terminal`, if you are on UNIX-system) in the folder where you want to clone the repository, and issue the following command:
    ```
    git clone <paste_your_cloned_URL_here>
    ```
    - After cloning is done, confirm that a folder named `IEEE-LEAD-2.0` is present in your current working directory.


Now, Follow the below steps for submitting each Project:
- Copy your project folder.
- Paste it in the local clone of `IEEE-LEAD-2.0`(created in the above steps), inside the respective Project folder.
- Rename your Project folder to your Full name.
- Now, Right-click and open `gitbash` in the `IEEE-LEAD-2.0` folder, and issue the following commands in order:
```
git add .

git commit -m "Your commit message"

git push -u origin master
```
- After pushing your project to github, you need to create a Pull Request to the main IEEE LEAD repository. For that, open your forked repository in browser, and you'll notice a big green button saying “Compare & pull request”. Press it!
- This will open a page in which you’ll be able to further edit the description for your proposed changes. Once, you are done with those, you can click on the "Create Pull Request button", and that's it.
 Congratulations, you just made a new Pull request!!! :fire: