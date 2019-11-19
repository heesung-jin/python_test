#!/usr/bin/python3
print("content-type:text/html; charset=UTF-8")
print()
import cgi
form = cgi.FieldStorage()
title= form["title"].value
description= form["description"].value

opened_file =open('data/' +title, 'w')
opened_file.write(description)

print("<a href=index.py>completed</a>")
print("Location: index.py?id="+title)
print()
