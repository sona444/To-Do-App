import os
from flask import render_template, redirect, url_for, abort, flash, request,current_app, make_response
from flask import Flask, redirect, url_for, request
from flask_migrate import Migrate, MigrateCommand
from flask_sqlalchemy import SQLAlchemy
from werkzeug.datastructures import ImmutableMultiDict
import json

 
app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://sonakshi:sonakshi@localhost/todo'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)
from models import task

@app.route('/')
def todo_app():
   return render_template("index.html") 

@app.route('/add-task', methods = ['GET', 'POST'])
def addtask():
   print(request.form)
   if request.method == "POST":
         jsonData=request.form
         jsonData.to_dict(flat=True)
         print(jsonData)
         name = jsonData['name']
         description = request.form.get('description')
         deadline = request.form.get('deadline')
         status = request.form.get('status')
         new_task = task(name=name, description=description, deadline=deadline, status=status)
         db.session.add(new_task)
         db.session.commit()
         return("updated")

if __name__ == '__main__':
   app.run()