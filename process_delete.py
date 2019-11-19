#!/usr/bin/python3
print("content-type:text/html; charset=UTF-8")
print()
import cgi, os
form = cgi.FieldStorage()
pageId= form["pageId"].value

os.remove('data/'+pageId)

print("<a href=index.py>completed</a>")
print("Location: index.py")
print()
