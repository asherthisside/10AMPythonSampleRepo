
# Q1. Ans:

# Website is a  collection of web pages. It is a platform where user visit through url address or routes.
# Differents b/w static and dynamic websites :
# Static website is a website where user visit through static url means its structure is fixed.like google,amazon websites.
# Dynamic website a type of website where visit through dynamic url means its structure is not fixed.a user visit with a specific id for show your output. like student management site. we visit through id.


# Q2. Ans:

# Django is  a framework for creating web application, It is based on MVT means Model view and template software pattern.

# Architecture of MVT:

# Model :
# All type of database related work happen in Models.we define classes and fields and we makemigration of classes then a file create on migration folder and migrate the data which we define in models after migrate a your table created on database.

# View:
# In the view section all business logics are defined. In the views we define functions and classes and render it to an html page. where user show in browser.
 
# Template:

# Template are based on html form where html file created. we define context in views and send to html page.

# User --> Django server--> Urls -- > views --> Models(database) -- > Templates(HTML Page) -- >


# Q3.:Ans:

#  Directory structure of django project:

# create a new folder naresh name and open folder and shift+right click mouse and open power shell and write a command djang-admin startproject new_project and enter then open your folder naresh a project create firts project contains these files and folder:

# new_project --folder or root directory and contains these files-
# __init__.py
# asgi.py
# settings.py
# urls.py 
# wsgi.py

# and also create a file views.py for define functions

# manage.py  --main file   


# Q4.Ans:

# Firstly we create a project and go to project path where manage.py exists and write command py manage.py startapp app1 and enter your app created and int the app1 folder created automatic a file models.py where all classes are define. after define wite command python manange.py makemigrations then automatic a file created on migration folder. then you write another command python manage.py migrate and enter after migrate your table will be created on database. we crete tables in databse because we want to perform crud operations  means create, read,update and delete.

# command uses in this activity:

# django-admin startproject new_project  -- for create project

# python manage.py startapp new_app  --  for create app

# python manage.py makemigrations -- for migration of classes

# python manage.py migrate    ---- for create table into database.

# Total: 32/50