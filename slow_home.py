#!/usr/local/bin/python3
print("content-type:text/html; charset=utf-8\n")

import cgi
form = cgi.FieldStorage()
if 'id' in form:
    pageId = form["id"].value
else:
    pageId = 'Slow'

print('''<!doctype html>
<html>
<head>
  <title>We Are Slow</title>
  <meta charset="utf-8">
</head>
<body>
    <h1>We Are Slow</h1>
    
</body>
</html>
''')