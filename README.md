# traxi

flask app tutorial:
https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world 

# create database based on the model classes
(venv) $ flask shell

from traxiapp import db

db.create_all()

# add support for database migrations
(venv) $ flask db init

To make changes to the database schema the following procedure needs to be followed:
1. make the necessary changes to the database model classes.
2. Create an automatic migration script with the 'flask db migrate' command.
3. Review the generated script and adjust it so that it accurately represents the changes that were made to the models.
4. add the migration script to the source control
5. Apply the migration to the database with the 'flask db upgrade' command


# Run application
cd into app folder
set FLASK_APP enviroment variable
(venv) $ export FLASK_APP=run.py
(venv) $ python run.py


# styling
create a responsive navbar:
https://www.youtube.com/watch?v=L0uNai3XyKQ 

# creat new branch and work locally
- create new branch on github
- greate local git repository: git init
- add remote and track newly created branch: git remote add -t <branch_name> <remote_name> <remote_url>
- pull files from remote into local folder: git pull

# rebase branch with master
https://www.youtube.com/watch?v=f1wnYdLEpgI 
