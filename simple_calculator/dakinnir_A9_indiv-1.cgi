#! /usr/bin/env python3
#immporting the necessary module packages
import cgi
#incase of internal server error
import cgitb
cgitb.enable()
print('Content-type: text/html\n')


form = cgi.FieldStorage()
#our html template
html = """
<!doctype html>
<html>
<head><meta charset="utf-8">
<title>Form in CGI</title>
<link rel="stylesheet" href="https://cgi.sice.indiana.edu/~dpierz/i211.css"></head>
    <body>
	<p>{content}</p> 
    </body>
</html>"""
try:
#check for which radio button is picked
    if 'c' in form.getfirst('vote', '0'):
        total = eval(form.getfirst('one','0')) + eval(form.getfirst('two','0'))
    elif 'd' in form.getfirst('vote', '0'):
        total = eval(form.getfirst('one','0')) * eval(form.getfirst('two','0'))
    elif 'e' in form.getfirst('vote', '0'):
        total = eval(form.getfirst('one','0')) - eval(form.getfirst('two','0'))
    elif 'f' in form.getfirst('vote', '0'):
        total = eval(form.getfirst('one','0')) / eval(form.getfirst('two','0'))
#if the user doesn't give us both numbers input
except:
	total = "Error invalid numbers"
#output
print(html.format(content = 'The result of the operation is: '+str(total)))
