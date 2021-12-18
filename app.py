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
   tasks=task.query.all()
   return render_template("index.html", task=tasks) 

@app.route('/task-form')
def newtask():
   return render_template("task-form.html")

@app.route('/task-form/<task_id>')
def edittask(task_id):
   if task_id != None:
      tasks = task.query.filter_by(id=task_id).first()
      return render_template("task-form.html", task=tasks)

@app.route('/add-task', methods = ['GET', 'POST'])
def addtask():
   if request.method == "POST":

         taskid = request.form.get('id')
         name = request.form.get('name')
         description = request.form.get('description')
         deadline = request.form.get('deadline')
         status = request.form.get('status')
         if taskid!=None and taskid>0:
            taskk = task.query.filter_by(id=taskid).first()
            taskk.name=name
            taskk.description=description
            taskk.deadline=deadline
            taskk.status=status
            db.session.commit()
            return todo_app()
         new_task = task(name=name, description=description, deadline=deadline, status=status)
         db.session.add(new_task)
         db.session.commit()
         return todo_app()

@app.route('/delete/task/<task_id>')
def deletetask(task_id):
   print(task_id)
   task_id = task.query.filter_by(id=task_id).first()
   if task_id != None:
      task_id = task.query.filter_by(id=task_id.id).delete()
      db.session.commit()
      return todo_app()
   return json.dumps(dict(status=501,message="Task do not exist"))


if __name__ == '__main__':
   app.run()