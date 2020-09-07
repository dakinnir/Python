'''
This is the second page that will be presented to the user once the style and size of the pizza has been chosen. 
'''


#! /usr/bin/env python3
#importing the necessary module packages
import cgi, cgitb
cgitb.enable()
print('Content-type: text/html\n')

form = cgi.FieldStorage()

#html and styling for the page
#reused the stylesheet link from dpierz
html = """
<!doctype html>
<html>
<head><meta charset="utf-8">
<link rel="stylesheet" href="https://cgi.sice.indiana.edu/~dpierz/i211.css">
<title>Ranye Pizza</title>
</head>
    <body>
    <div class="title" style="margin: auto;
            position: absolute;
            left: 36%;
            height: 70px;
            width: 400px;
            background-color: darkred;"><h1 style="color: white;
            margin: auto;
            vertical-align: middle;
            line-height: 70px;">Ranye Pizza!</h1></div>
            <br><br><br>
            <div class="topping" style="display:flex; display:inline-block;">
        <img src="mush.png" alt="logo" height="170" width="240">
        <img src="pepp.jpg" alt="logo" height="200" width="300">
        <img src="onion.png" alt="logo" height="170" width="270">
    </div>

        <p> What do you want on your {size} pizza with {crust}-style crust, {name}? Each topping costs $2 to add. </p>
        <form method="get" action="pizza2.cgi">
            <p><input type="checkbox" name="topping" value="pepperoni"> pepperoni </p>
            <p><input type="checkbox" name="topping" value="mushroom"> mushroom </p>
            <p><input type="checkbox" name="topping" value="onion"> onion </p>
            <p><input type="checkbox" name="topping" value="bell pepper"> bell pepper</p>
            <p><input type="checkbox" name="topping" value="extra cheese"> extra cheese</p>
            <input type="hidden" name="size" value='{size}' >
            <input type="hidden" name="crust" value='{crust}' >
            <p> Enter discount code here: <input type="text" name="discount"></p>
            <button type="submit"> Next </button>
        </form>
    </body>
</html>"""
#get the value from the intial html and from the radio button and dropdown menu
size = form.getfirst('size')
crust = form.getfirst('crust')
name = form.getfirst('name')
#output going into the html strinh to be printed out
print(html.format(size=str(size), crust=crust, name=str(name)))
