#!/usr/bin/python3
print("content-type:text/html; charset=UTF-8")

print()

import cgi, os
import sys # to inroll temp paht for module
import codecs #hangul procesing.

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach()) #hangul procesing2.

form = cgi.FieldStorage()
pageId= form["pageId"].value
title= form["title"].value
description= form["description"].value

opened_file =open('data/' +pageId, 'w',encoding='utf-8') #directory and file name what you want to update.
opened_file.write(description) #file contents what you want to write.
opened_file.close()
os.rename('data/'+ pageId,'data/'+ title) #directory name what you want to change. (before name, after name)

print("<a href=index.py> go to Main page </a>")
#Redirection
print("Location:index.py?id="+title)

print()

