# Foundations of Software Engineering<!-- omit in TOC -->
This is the repository for the Foundations of Software Engineering course. In here you can find reference solutions to all major challenges as well as explanations on how to solve them yourself.

## Contents<!-- omit in TOC -->
- [Overview](#overview)
  - [Challenges](#challenges)
  - [Wiki](#wiki)
- [FAQs](#faqs)
- [Working with this repository](#working-with-this-repository)
  - [Branches](#branches)
  - [Wiki submodule](#wiki-submodule)
    - [Example commit workflow](#example-commit-workflow)
  - [Relative Links to the wiki](#relative-links-to-the-wiki)
  - [Links to Google Classrooms](#links-to-google-classrooms)
  - [Fabi's wildest dreams](#fabis-wildest-dreams)

## Overview
There are two core parts to this repository. The repository holds the reference solutions. This repo's wiki holds the explanations for the challenges. On top of that the wiki contains a growing number of guides and cheatsheets which hopefully help you in getting started as a Software Engineer.

### Challenges
Sample solutions for the challenges can be found [here](./challenges).

### Wiki
Have a look at the [wiki](./wiki) if you are struggling to find resources on a certain topic

## FAQs
Have a look at this repo's [issues](https://github.com/FabianVolkers/Foundations-of-Software-Engineering/issues) to find FAQs and feel free to open a new issues if you think something is missing.

## Working with this repository 

### Branches
The main branch of this repo is latest. Github only supports using the master branch for the wiki pages, therefore the wiki's repository's only branch is master.

### Wiki submodule
The wiki repo is a submodule to the main repository. Cloning the main repo using `git clone --recurse-submodules https://github.com/FabianVolkers/Foundations-of-Software-Engineering.git` will also clone the submodule. It can be found in the `wiki` directory. Changing into this directory will also change the git repository you are working with. To commit new changes to the wiki proceed as you usually would. The only difference is that after updating the wiki repo, you have to add and commit the wiki repo in the main repository in order to update the commit pointer. It is important to push both the submodule as well as the main repository, otherwise the commit pointer will point to a non existent commit on everyone else's machines.

#### Example commit workflow
```bash
$ cd wiki
$ git add wikipage.md
$ git commit -m 'update wikipage'
$ git push

$ cd ..
$ git status

On branch latest
Your branch is up to date with 'origin/latest'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   wiki (new commits)

no changes added to commit (use "git add" and/or "git commit -a")

$ git add wiki
$ git commit -m 'update commit pointer'
$ git push
```

For more information on how to use submodules check out this [link](https://brendancleary.com/2013/03/08/including-a-github-wiki-in-a-repository-as-a-submodule/)


### Relative Links to the wiki
In order to link from a README file in the main repository to the wiki using relative paths, use this structure 
`../../../../wiki/filename`
the amount of `../`'s depends on how deeply nested the current readme is. Directories in the wiki repository get ignored for some reason, adding `.md` extensions will link to the raw file on `githubusercontent`, so `/challenges/Color-Check.md` gets linked to using `../../Color-Check`

### Links to Google Classrooms
Because assignments in Google Classrooms can only be linked to directly once they have been published, we use Firebase Dynamic Links in this [Firebase Project](https://console.firebase.google.com/u/0/project/code-se-foundations/durablelinks/links/https:~2F~2Ffoundations.page.link). All we have to do every year is change the redirect url in the Firebase Console to point to the newly published assignments. There is also an API for both Google Classrooms and the Dynamic Links, maybe we can automate this step.

### Fabi's wildest dreams
- Automatically update Firebase Dynamic Links when new assignments get posted
  - Combine [Classroom API](https://developers.google.com/classroom/reference/rest/v1/courses.courseWork/list?apix_params=%7B%22courseId%22%3A%22121369170019%22%2C%22courseWorkStates%22%3A%5B%22DRAFT%22%5D%7D) with [Firebase API](https://firebase.google.com/docs/dynamic-links/create-links?authuser=0#manually_constructing_a_url)
- Automated testing for challenges using firebase 
- 