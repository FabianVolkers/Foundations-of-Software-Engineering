The Restaurants Assignment is in Google Classrooms. The explanation can be found in the [wiki](../../wiki/Restaurants-db).

The solution is rather similar to that of the previous Restaurants challenge. You'll find that we no longer need the `restaurants.txt` and are now working with `restaurants.db`
Run the solution yourself at the command line: 

```bash
python3 server.py
```

Explanation of files: 

1. `index.html`
   
    This file is generated and served by server.py. It holds all the html for our restaurants page.

2. `restaurants.db`

    This file holds all the names and neighbourhoods of the restaurants we want to display on our website. Instead of a text file, we are now using a sqlite database.

3. `server.py`

    This file holds all the logic for our website. It generates the html based on the `restaurants.txt` file and serves `index.html` to the requesting client.

4. `style.css`
   
   The CSS file is optional for the functionality we want to implement. It does make the website look a bit more pleasing to look at however.

Credits: Fabian Volkers' reference solution to this problem in Foundation 2020. 