Create a website which prompts a user to input the name of color, and checks if the color exists or not. In doing this, you will practice what we did in class on Monday (getting user input, responding with dynamically generated html), and you will start adding a bit more code and logic to your python script. Please create a repository called color-check, and when you are done, push this to GitHub and submit the link to your GitHub repository here on google classrooms.

Here is the intended behavior: If the user inputs “red” they should get a response which “red is a color”. If they write “rerdo^isdhilhg” they should get a response which says “rerdoisdhilhg is not a color”. The list of colors should live in a dedicated file in the repository.


The structure will look very similar to what we did in class: an index.html file with a form, which triggers a backend script, which generates some html. This time, that script should not simply process a string, but also do a bit more: it should check if the color exists.

Bonus: if the color input by the user has a hexadecimal representation for use on the web, rendar a color swatch of that color beneath the answer. In other words: if a user writes blue, it should not only display "blue is a color", but also show a blue box below it. Feel free to play around here.

To do this, I suggest the following:
- Start a new repository. Re-create (or copy) some of the files you worked on in class, and change the filenames and texts so that they make sense for this project.
- in your backend script (previously, generate.py), think about how to check if the word which a user submitted is indeed a color. You might want to start with a very short list of colors (red, green, blue), which is hard-coded into the backend file, and write some Python code which checks if the word that the user submitted through the form is in that list.
- Then, create a new file called colors.txt, and put the colors into that file (instead of living in the python script). You are practicing separating data from logic, an important thing to write good software! You will need to read in that file to your code; there is a link below from RealPython with more information on how to do this.
- Once you have done this, you might be asking yourself: do I need to write down every color that's out there? No, of course not! Somebody else already did something like that for you. There are several machine-readable lists of colors flying around in open-source code, for instance the one linked below. You can also create your own list of colors. Either way: the colors should be listed in a separate file in your directory.
- The bonus is to actually use that color in some CSS in the website itself.