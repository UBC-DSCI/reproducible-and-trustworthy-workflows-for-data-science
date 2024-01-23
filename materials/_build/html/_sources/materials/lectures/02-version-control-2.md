# Version control (for transparency and collaboration) II

## Topic learning objectives

By the end of this topic, students should be able to:

1. Use Git and GitHub to successfully collaborate with others (e.g., handle merge conflicts, use a fork-pull-request and branch-pull-request workflow to contribute to a project, organize tasks through issue milestones and project boards)

## Git Branches

Branches allow you to have a playground 
for developing and testing new additions to your code,
as well as fixes.
This playground lets your explore, experiment and test 
in a safe place - away from others that might be using 
or depending on the current version of your code.
This is perhaps more obviously useful if your project
is deployed and has users (e.g., a data visualization dashboard, 
an R or Python package, a phone app, etc),
but this can also be useful for code that make up a data analyses.
As, in addition to the reasons stated above for branching,
branching also lets you organize units of work into smaller, 
more manageable chunks that are easier for collaborators to check over and review.

Once the new code additions or fixes have been 
finalized in their branch playground,
they can be merged back to the main code-base.
Several branch playgrounds can co-exist, 
one for each new code addition or fix being worked on.
This allows for parallelization of work!

We can use a construction of a house
as a metaphor for this kind of development.
First,
you need to build the foundation.
Since everything depends on the foundation being built,
this would be developed on the main branch.
When the foundation is finished,
the construction of other parts of the house that don't depend on each other
could take place in parallel,
e.g. some contributors might start working on the walls and others on the floor.
When either of these features is finished, 
it can be added back to the house
(merged into main).
When depicted graphically,
this process would look something like this
(each dot is a commit).

<img src="img/branches-house-analogy.png" width=400>

A more realistic Git branching example for a data analysis project might look something like this:

<img src="img/git-branch-diagrams.png" width=400>

### Creating a branch using the command line

In the terminal, and in the working directory of the project in which you wish to create a branch,
use `git switch` with the `-c` flag and specify the branch name. 
This create a new branch and immediately switch to it.
For example, to create a branch named `patch-docs` 
(a good branch name if we were planning on working on a fix
in the project's documentation),
we would type:

```
git switch -c patch-docs
```

To ask Git what branches now exist and to see where we are,
we can use the `branch` command with the `-v` flag 
(for "verbose", meaning tell us everything!):

```
git branch -v
```

And we should see something like the output shown below,
which lists the branch names in the first column,
the SHA of the last commit on each branch in the second column,
and the commit message associated with the last commit in the third column:

```
  main       f756bbb initial
* patch-docs f756bbb initial
```

As you work here on this new branch, 
you can commit your changes to version control locally, 
and even push your changes to the remote repository. 
All the changes however will live only on that branch 
until you do something to move them to another branch. 
When you want to start discussing your changes with your collaborators 
to start the process of bringing these changes into the main branch (main code-base) 
you typically create what is called a pull request. 
A pull request is a like an asking your collaborators "is it OK to merge my code?" 
Usually there will be some discussion and a few more revisions to the code, 
but eventually they will give you the thumbs up when everything looks good 
and the code can then be merged. We will discuss this more next.

#### Switching to branches that already exist

After you have been working on your new brain for some time,
you will eventually want to get back to the project's default branch, 
or some other branch.
To do this, we use `git switch <branch_name>`. 
Note that we do not use the `-c` flag this time, as we are not creating a new branch.

#### Getting remote branches you did not create locally

If your collaborator creates a branch that you want to 
run or test locally, but it only exists on the remote repository
you have to tell Git to fetch (go get it) for you first, 
before you can switch to it. 
You can specify which branch you specifically want to grab,
but for simplicity it is often easy to ask Git 
to fetch all of them for you, using the `fetch` command
with the `--all` flag:

```
git fetch --all
```

#### Useful command line Git branching commands

Below is a table of the most commonly used 
Git commands for branching. 
This table includes the commands we presented above
as well as the a few other useful ones.

| Description | Command |
|---------|-------------|
| list all local branches | `git branch -v` |
| create a new branch & immediately switch to it | `git switch -c <branch_name>` or `git checkout -b <branch_name>` |
| switch to a branch | `git switch <branch_name>` or `git checkout  <branch_name>` |
| fetches all changes to all branches | `git fetch --all` |
| retrieve a branch you don't have locally on your laptop from GitHub| `git checkout --track origin/<branch_name` |
| merge changes from another branch | `git merge <branch_name>` |
| delete a local branch | `git branch -d <branch_name>` |
| push changes to a remote branch | `git push origin <branch_name>` |

#### Exercise

1. Make your own copy of [this GitHub repository](https://github.com/ttimbers/sqrt) by clicking the green "Use this template" button. And then clone your copy of the repository to your computer.

2. Create a new branch named `better_error_msg` in the local repository using Git.

3. On that branch, fix the `sqrt.py` so that if you run this script with a negative number as an argument you do not get an difficult to understand error, but instead throw a helpful exception informing the user that the number should be positive. Fix to add to `sqrt.py`:
  
```
if number < 0:
  raise Exception("n should not a positive number")
```

4. Add and commit those changes.

5. Switch back to the `main` branch and look at the `sqrt.py` file - do you see the change there?

6. Switch back to the `better_error_msg` branch - do you see the change there?

7. Push your change to the remote GitHub repository, and see where you can find it there!

> Note: if you use the Git command line tool and get an error message like the one shown below,
> this is because you did not state the remote (usually it is `origin`).
> Try pushing again using `git push origin <branch_name>`
>
> ```
> fatal: The current branch better_error_msg has no upstream branch.
> To push the current branch and set the remote as upstream, use
> 
>     git push --set-upstream origin better_error_msg
> 
> To have this happen automatically for branches without a tracking
> upstream, see 'push.autoSetupRemote' in 'git help config'.
> ```

## Creating a pull request

To create a pull request,
you first need to ensure all the local changes you made on the new branch 
are also available on the remote repository
(i.e., you need to push them).
Once that has happened you need to
go to the remote GitHub repository,
as pull requests are created from there.

GitHub often tries to be helpful when a change 
is pushed to a new branch that doesn't yet exist
on the default branch by showing you a yellow banner 
listing any recently pushed branches.

<img src="img/create-pr.png" width=700>

To create a pull request,
you click the green button "Compare & pull request".
In the new page,
add a message to describe the changes you have made,
scroll down to review the changed files,
and the click the green button that reads "Create pull request".
If you are working together in a team,
you could also designate certain team members to review your work
and assign relevant labels,
via the right hand side panel.

The next step is for a collaborator to review your work
and merge it in if they approve it.

#### Exercise

1. Use the green "Compare & pull request" button on the yellow banner to open a pull request.

2. Go to the "Pull requests" tab on the remote GitHub repository and explore the "Conversation" and "Files changed" sub-tabs there.

## Code reviews using in-line comments and suggested code fixes

- In the project, you are expected to read and review eachother's code BEFORE accepting a pull request. 

- Do not expect all (or even most) pull requests to be perfect in their first submission. 

- We very often need to have a conversation to get pull requests into good shape before merging into master, and GitHub has a very nice tool we can utilize to do this: **GitHub code reviews**

<img src ="img/code-review-suggest-change.png" width=600>

### Demo: do a code review:

I am going to demo a code review of a pull request. I have set-up a template GitHub repository for you so that you can easily generate a pull request for you to review if you want to try this later.

#### Steps:

1. Click the green "Use this template" button in [this repository](https://github.com/ttimbers/review-my-pull-request) to obtain a copy of it for yourself (do not fork it).

2. Create a remote branch named `pr` (this will use GitHub Actions to create a pull request for you to review in this repository).

3. Click on the Pull Requests tab of your copy of the repository, click on the pull request titled "Report most accomplished pilots", and then click on "Files Changed". Next click on the `star-wars.Rmd` file. Review the file and observe the following problems with the R Markdown report that was submitted via the pull request:
  - Reasoning of the sentence on line 15
  - Incompatibility with the sentence on line 15 with the code in the code chunk named `table-of-most-accomplished-pilots`
  - Incorrect code in code chunk named `table-of-most-accomplished-pilots` (unested `film` instead of `starships`) leads to naming the wrong pilot as the most accomplished pilot on line 19
  - Incorrect code in code chunk named `table-of-most-accomplished-pilots` (unested `film` instead of `starships`) leads to the use of the wrong character's picture in the image that is sourced in the code chunk named `top-pilot` (it should be a picture of Obi-Wan Kenobi, you could use this URL for example: <https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/ewan-mcgregor-obi-wan-1570898048.jpg>).

4. Add comments and suggested changes using the `+` sign beside the line numbers (the first time you do this will trigger the start of your code review. Need help? See [GitHub's how to on reviewing proposed changes in a pull request](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/reviewing-proposed-changes-in-a-pull-request).

5. After you have made all the comments and suggested changes, then add a general comment for the code review, select "Request Changes" and submit your code review.


### Demo: Accept suggested changes from a code review:

#### Steps:

1. To accept the code changes that you provided as suggestions, revisit the Pull Requests tab of your copy of the repository and clicking on the pull request titled "Report most accomplished pilots". Scroll through the pull request comments and find the code suggestions. Then click on the "Commit suggestion button" for each suggestion. 

2. Click on the "Show all reviewers" link beside the red "Changes requested"" text. Then click on the `...` beside the reviewer and click "Approve changes".

3. Finally click on the green buttons ("Merge Pull Request" & "Confirm merge") to merge the pull request.

### Discussion: 

Could I have done the entire code review well by just reviewing it on GitHub?

*Hint: if I didn't tell you that the top pilot was Obi-Wan Kenobi, how would you have known that?*

### Useful things you can do with branches on GitHub

Create a new branch:

<img src="img/create_branch.png" width=600>

Source: <https://github.com/UBC-DSCI/introduction-to-datascience>

View all branches and their status:

<img src="img/view_branches.png" width=600>

Source: <https://github.com/UBC-DSCI/introduction-to-datascience>

And delete remote branches:

<img src="img/delete_branches.png" width=600>

Source: <https://github.com/UBC-DSCI/introduction-to-datascience/branches>

### How do you not accept a pull request?

In some cases, it might not make sense to merge a pull request. To close a pull request that should not be merged, scroll to the bottom of the pull request page, and look for a gray "Closes pull request" button. This will end move the pull request to the closed pull requests section (similar to closed issues) and does not merge the changes. 

<img src="img/close-pr.png" width=500>

## Git and GitHub flow

Branching generally works well if a team agrees to and follows a consistent workflow. The two leading workflows used in industry are Git flow and GitHub flow. We will describe and discuss both here so you are aware of both, and we will employ GitHub flow in our projects for this course. 

### GitHub Flow

Key features:
- **A single** "main" branch that also serves as the deployment branch, we call this main.
- Every new contribution is done on a new branch (with a meaningful name) created from main.
- Contributions from that new branch are sent back to main by means of a pull request, which ideally is reviewd & tested before merging.

(note: at the time this figure was made, the default branch on GitHub as still called the master branch)

<img src="https://files.programster.org/tutorials/git/flows/github-flow.png" width=600>

Source: https://blog.programster.org/git-workflows

### Git Flow

Key features:
- **Two** "main" branches that last forever, main for deployment and develop where things are tested before they are released to main.
- Three supporting branches: feature, release & hotfix. Both feature & release branches are created from develop. feature branches should be merged into develop before they are incorporated into a release. release branches eventually get merged into main after adequate review and testing.

(note: at the time this figure was made, the default branch on GitHub as still called the master branch)

<img src="https://files.programster.org/tutorials/git/flows/git-flow.png" width=600>

Source: https://blog.programster.org/git-workflows

### Discuss:

What do you think are pros & cons of each of these branching workflows?

### Relevance to course project:

- You will be expected to work using the GitHub flow workflow for your projects in this course. 

### What happens when my feature branch falls behind main?

> How to catch up a branch that has fallen behind the `main` branch using the command line:
> 
> - run `git pull origin main` to pull any changes from the remote version of main that we might not have
> - run `git switch <branch>` to make sure we are on the branch we want to catch up
> - run `git merge main` to merge the changes
> - run `git push origin <branch>` to push our updated branch to the remote

## Project boards

Example of a physical [Kanban board](https://en.wikipedia.org/wiki/Kanban_board):

<img src="https://miro.medium.com/max/1300/1*9xfpL1ercY-JA7BzEiLpjA.jpeg" width=500>

Source: <https://medium.com/@mli/lets-get-physical-task-boards-f9d08383e667>

Example of a digital project board from GitHub:

Reading: [About project boards - GitHub Help](https://help.github.com/en/github/managing-your-work-on-github/about-project-boards)

<img src="img/github_kanban.png" width=800>

Source: <https://github.com/CodeDoesGood/org-website/projects/1>


### Why use project boards for collaborative software projects?

- **Transparency:** everyone knows what everyone is doing

- **Motivation:** emphasis on task completion

- **Flexibility:** board columns and tasks are customized to each project

### Exercise: Getting to know GitHub project boards

We are going to each create our own project board for our MDS homework. I have set-up a template GitHub repository for you so that you can easily populate it with relevant issues for your homework this block. You will use these issues to create your MDS homework project board.

#### Steps:

1. Click the green "**Use this template**" button from [this GitHub repository](https://github.com/UBC-DSCI/dsci-310-homework) to obtain a copy of it for yourself (do not fork it).

2. Click on the Actions tab, and then click on the workflow `.github/workflows/create_issues.yml`. You then should see a **“Run workflow”** button with a drop down menu, from that menu select **“Run workflow”**.

3. Wait patiently while GitHub Actions to create 24 issues for you in your copy of this repository.

4. Click on the Projects tab, and then click **“Link a project”** and then select **“Create a new Project”**. Select **“Board”** as the template option and give the project a a name.

5. Use the issues in the repo to set-up a project board for the next two weeks (or more) of your DSCI 310 homework. For each issue you add to the project, assign it to yourself and add a label of "group-work" or "individual-work".

Additional Resources:
- [Assigning issues and pull requests to other GitHub users](https://help.github.com/en/github/managing-your-work-on-github/assigning-issues-and-pull-requests-to-other-github-users)
- [Applying labels to issues and pull requests](https://help.github.com/en/github/managing-your-work-on-github/applying-labels-to-issues-and-pull-requests)

### Relevance to course project:

- You will be expected to create a project board for each of your groups projects and update it each milestone (at a minimum)

- We expect that each issue should have at least one person assigned to it

## Milestones

- Group related issues together that are needed to hit a given target (e.g., new release version of a software package)

- Can assign a due date to a milestone

- From the milestone page you can see list of statistics that are relevant to each milestone set in that repository

Reading: [About milestones - GitHub Help](https://help.github.com/en/github/managing-your-work-on-github/about-milestones) 

Example of the `readr` package milestones:

<img src="img/readr-milestones.png" width=600>

Source: https://github.com/tidyverse/readr/milestones

### Exercise: Getting to know GitHub milestones

We are going to practice creating milestones and associating issues with them. To do this we will continue working with the same repository that you just created a project board for.

#### Steps:

1. Click on the Issues tab, and then click on "Milestones". 

2. Click "New milestone" and name it "month 1" and set the due date to be the end of January. Click "Create milestone".

3. Go to the Issues tab, and for each issue that should be associated with the month 1 milestone (i.e., things due before the end of January), click on their checkbox. Then click "Milestone" and select "month 1"

4. Once you are done, go back to the Milestones page to view what the month 1 milestone looks like.

5. If you finish early, do this for  month 2.

### Relevance to course project:

- You will be expected to create a milestone on each of your project repositories for each course assigned milestone. You must link the relevant issues needed to complete that milestone to it on GitHub.

## SSH for authentication

So far you have likely been using a personal access token to authenticate to GitHub. 
This works, however there is another very secure and more convenient method of authentication
that is widely used: secure shell protocol (SSH).
SSH can be use for other forms of authentication as well (beyond GitHub), 
including logging into remote machines in the cloud. 
So for many these reasons it is worthwhile learning. 
Thus, we will spend some time explaining it here, 
and setup our computers to use this for authenticating with GitHub going forward.

### Remotely accessing another computer using SSH 

Let's start with some definitions:

#### Definitions

**Secure SHell (SSH)** - a common method for remote login to another computer which is secure.

**server** - a machine you are SSHing into. The server sits and waits to be contacted.
 
**client** - usually your machine. The client initiates contact with the server.

#### SSH key-based authentication

Two components: 

1. public key
2. private key

These files have an asymmetrical relationship:

- the public key CANNOT decrypt messages generated by the private key
- the private key CAN decrypt messages generated by the public key

#### Understanding public key private key concepts

- Think of a public key, not as a key, but as a padlock that you can make copies of and put anywhere you want.
- To put your ‘padlock’ on an another machine, you would copy it to `authorized_keys` in the `~/.ssh` folder.
- Think of a private key as an actual key, it can open the padlock that is stored on the other machine.

<img src="img/keys_1.png" width=600>

*source: http://blakesmith.me/2010/02/08/understanding-public-key-private-key-concepts.html*

#### How the lock works

- Keys are generated using `ssh-keygen`, to make private key (usually called `id_ed25519`) and a public key (usually called `id_ed25519.pub`) 
- You can make copies of `id_ed25519.pub` (public key/padlock) and distribute them to other machines
- The other machine uses the public key to encrypt a challenge message to you
- You need to show that you can decrypt the message to demonstrate that you are in possesion of the associated private key

_Note: GitHub has changed recently the SSH key generation instructions to use [Ed25519 algoritm](https://github.com/github/docs/issues/876). 

#### You can put your lock at many places

As long as you are using the same lock (public key),
you will be able to open it with the same private key.

<img src="img/keys_2.png" width=600>

*source: http://blakesmith.me/2010/02/08/understanding-public-key-private-key-concepts.html*

#### Keeping your private key safe

- `ssh-keygen` allows you to put a password or passphrase on the private key
- this should be shared with NO ONE!
- if your private key does fall into the wrong hands, the person must still know the password or passphrase to use the private key 

<img src="img/password_strength.png" width=600>

*source - https://xkcd.com/936/*

#### Exercise

Setting up SSH for authentication on GitHub! Follow the docs linked below here to accomplish each step to set this up.
At the top of each of the documentation sections, be sure to select the tab for your operating system.

1. [Checking for existing SSH keys on your computer](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/checking-for-existing-ssh-keys)

2. [Generating a new SSH key](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent#generating-a-new-ssh-key)

3. [Adding your SSH key to the ssh-agent](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent#adding-your-ssh-key-to-the-ssh-agent)

4. [Adding a new SSH key to your GitHub account](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account)

5. Test it out! Create a private GitHub.com repository and try to clone it using the SSH code URL (instead of the HTTPS one), it should look something like this: `git@github.com:username/repo-name.git` 

*(whereas HTTPS code URLs look like: `https://github.com/username/repo-name.git`)*

## Next: 

- file and directory structure for data analysis projects
- integrated development environments for data science