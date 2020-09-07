'''

This is the third page that is shown to the users once their order information have been entered.

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
            line-height: 70px;">Thank you!</h1></div>
            <br><br><br>

        <p> Your order: A {size} {crust} pizza, with {topping}. </p>
        <p> Total Cost: ${totalcost}
    </body>
</html>"""
#get the value from the intial html and from the radio button and dropdown menu
size = form.getfirst('size')
crust = form.getfirst('crust')
#get the toppings picked from the checkboxes
toppingList = form.getlist('topping')

#if the user select more than two topping
if len(toppingList) > 2:
    topping = ", ".join(toppingList[:-1]) + ", and " + toppingList[-1]
elif len(toppingList) == 2:
    topping = " and ".join(toppingList)
elif len(toppingList) == 1:
    topping = toppingList[0]
else:
    topping = "Nothing selected"

discount_code = 'PYTHON'

discount = form.getfirst('discount')

pizzaCost = {'small': 8.50, 'medium': 10.50, 'large': 12.50}
toppingCost = len(toppingList) * 2
totalcost = pizzaCost.get(size, 0) + toppingCost

if str(discount) == discount_code:
    totalcost = totalcost - (totalcost * .10)


print(html.format(size=str(size), crust=crust, topping=topping, totalcost=str(totalcost)))
