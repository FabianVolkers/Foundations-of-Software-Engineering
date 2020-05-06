Create a website which lists restaurants in Berlin together with the neighborhood they are in, taking that information from a text file. There should be at least 3 restaurants listed.

This exercise practices:
- setting up a repository for software development using git
- separating data (the restaurant list) from logic (the code which generates the website)
- dynamic webpage generation
- the principle of a single source of truth
- Python, HTML, CSS, and Networking
- Use of classes and designing a simple data model

We will launch these websites live on the real internet in class on Thursday, and we will continue building on this project in future weeks.

Detailed instructions:

First, create a new repository called foundations-restuarants. Make this a git repository (git init), create a repository on GitHub, push your local repository to GitHub, and submit the GitHub link here to this assignment. We will work with this more next week.

Ok, now that you have a repository, the goal is to start generating a website using Python. This is similar to what we did last week with color check. You can structure your files however you like, but the key will be to use Python to read in a text file and generate HTML with that. Here is a suggestion:

- create a file called restaurants.txt which will have your "data": the restaurant names and neigborhoods. I suggest structuring this file as comma separated value file. Each line will have a restaurant name followed by its neighborhood, with a "," in between. For instance, "Horus,Alt-Treptow".
- create a file called server.py, which reads in the contents of restaurants.txt and creates some HTM from it, which is then served. Consider the idea of a Class, which we discussed last week: you can model a restaurant has having two properties, a name and a neighborhood. You can then create a list of restaurants, and loop over this to create your HTML. One way to do this is to write a function which creates a file called index.html, and then another function which runs a Python web server to serve this. Another way to do this is to generate the HTML in-memory, never writing a file, but responding to requests with the HTML (like we did in the color-check response).
- create a css file for styling of your choice, which can be included as usual in the HTML header.

In order to check if you have created a dynamic website, do the following:
- close your webserver in the terminal
- add a new restaurant to your restaurants.txt file
- restart the webserver, and navigate to your page in the browser. Did the new restaurant appear?