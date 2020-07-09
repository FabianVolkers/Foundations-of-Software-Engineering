#!/usr/bin/env python3
import cgi

form = cgi.FieldStorage()
entered_color = form.getvalue('color')

#path = "/Users/matthias.bothe/code/foundations/color-check/cgi-bin/colors.txt"
data = open("cgi-bin/colors.txt", "r")
content = data.read() 

successMessage = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Success!</title>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="/style.css">
  </head>  
  <body style="background-color:{};text-align:center">
    <h1>Success</h1>
    <p>The background is your color</p>
    <a href="/index.html">Try again</a>
  </body>
</html>
""".format(entered_color)

errorMessage = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Error!</title>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">    
    <link rel="stylesheet" href="/style.css">
  </head>  
  <body>
    <h1>Failed!</h1>
    <p>{} is not a valid color.</p>
    <a href="/index.html">Try again</a>
  </body>
</html>
""".format(entered_color)

if entered_color in content:
  print (successMessage)
else:
  print (errorMessage)

data.close()