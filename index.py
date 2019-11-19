#!/usr/bin/python3
print("content-type:text/html; charset=UTF-8")
print()
import cgi, os, view_list


form = cgi.FieldStorage()
if 'id' in form :
	pageId = form["id"].value
	description= open('data/'+pageId, 'r').read()
	updateLink='<a href="update.py?id={}">Update</a>'.format(pageId)
	delete_action ='''
		<form action="process_delete.py" method="post">
			<input type="hidden" name="pageId" value="{}">
			<input type="submit" value="delete">
		</form>
	 '''.format(pageId)

else:
	delete_action=""
	updateLink=""
	pageId ='Welcome IOT Embedded'
	description='Embedded Software Engineering is the process of controlling various devices and machines that are different from traditional computers, using software engineering. Integrating software engineering with non-computer devices leads to the formation of embedded systems.'
	
 

print('''
<!DOCTYPE html>
<html>
<head>
  <title>on the JavaScript / IoT Engineering</title>
  <meta charset="utf-8">
</head>
<body>
  <h1><a href="index.py">On the JavaScript,  IoT embedded Engineering</a></h1>
  <ol>
	{listStr}
  </ol>
  <a href="create.py">Create</a> {updateLink} {delete_action}
 <h2>{title}</h2>
 <p>{desc}
 </p>
</body>
</html>'''.format(title=pageId, desc=description, listStr=view_list.getList(), updateLink=updateLink, delete_action=delete_action))
