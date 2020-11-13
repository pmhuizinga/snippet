# Code snippet database

Store code snippets and allow users to search on programming language, user and taga


### SETUP

- add virtual environment
- add database connection in config.py, class Config (SQLALCHEMY_DATABASE_URI)
- create models (tables) in app/models.py
- create log folder
- run create database commands:

  
    ../CRUD/flask db init
    ../CRUD/flask db migrate
    ../CRUD/flask db upgrade


- add forms data (corresponding to models.py) in case of data entry forms
- adjust views.py for handling CRUD transactions

### DATABASE CHANGES 

on initiate flask website first create the database. This is based on models.py
in terminal run:

    ../default_flask_ui/flask db init
    ../default_flask_ui/flask db migrate
    ../default_flask_ui/flask db upgrade

flask db init, this will set up a migration directory in the project and a alembic table in the database (for storing version numbers)  
flask db migrate, this will extract all the settings from models.py  
flask db upgrade, this will make the actual changes to the database  

in case of database changes run:  

    ../default_flask_ui/flask db migrate
    ../default_flask_ui/flask db upgrade
    
Migrate will extract all the settings from models.py  
Upgrade will make the actual changes to the database
