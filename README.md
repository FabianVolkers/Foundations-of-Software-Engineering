# Foundations of Software Engineering<!-- omit in TOC -->
This is the repository for the Foundations of Software Engineering course. In here you can find reference solutions to all major challenges as well as explanations on how to solve them yourself.

## Contents<!-- omit in TOC -->
- [Overview](#overview)
  - [Challenges](#challenges)
  - [Wiki](#wiki)
- [FAQs](#faqs)
- [Working with this repository](#working-with-this-repository)
    - [Example commit workflow](#example-commit-workflow)
  - [Relative Links to the wiki](#relative-links-to-the-wiki)

## Overview
There are two core parts to this repository. The repository holds the reference solutions. This repo's wiki holds the explanations for the challenges. On top of that the wiki contains a growing number of guides and cheatsheets which hopefully help you in getting started as a Software Engineer.

### Challenges
Sample solutions for the challenges can be found [here](./challenges).

### Wiki
Have a look at the [wiki](./wiki) if you are struggling to find resources on a certain topic

## FAQs
Have a look at this repo's [issues](https://github.com/FabianVolkers/Foundations-of-Software-Engineering/issues) to find FAQs and feel free to open a new issues if you think something is missing.

## Working with this repository 

The wiki repo is a submodule to the main repository. Cloning the main repo using `git clone https://github.com/FabianVolkers/Foundations-of-Software-Engineering.git` will also clone the submodule. It can be found in the `wiki` directory. Changing into this directory will also change the git repository you are working with. To commit new changes to the wiki proceed as you usually would. The only difference is that after updating the wiki repo, you have to add and commit the wiki repo in the main repository in order to update the commit pointer. It is important to push both the submodule as well as the main repository, otherwise the commit pointer will point to a non existent commit on everyone else's machines.

#### Example commit workflow
```bash
cd wiki
git add wikipage.md
git commit -m 'update wikipage'
git push

cd ..
git status
[...]
        modified:   wiki (new commits)
[...]
git add wiki
git commit -m 'update commit pointer'
git push
```

For more information on how to use submodules check out this [link](https://brendancleary.com/2013/03/08/including-a-github-wiki-in-a-repository-as-a-submodule/)


### Relative Links to the wiki
In order to link from a README file in the main repository to the wiki using relative paths, use this structure 
`../../../../wiki/filename`
the amount of `../`'s depends on how deeply nested the current readme is. Directories in the wiki repository get ignored for some reason, adding `.md` extensions will link to the raw file on `githubusercontent`, so `/challenges/Color-Check.md` gets linked to using `../../Color-Check`