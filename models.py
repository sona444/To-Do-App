from app import db
 
class task(db.Model):
    __tablename__="task"
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String)
    description=db.Column(db.Text)
    deadline=db.Column(db.Date)
    status=db.Column(db.Text)

def __init__(self, name, description, deadline, status):
        self.name = name
        self.description = description
        self.deadline = deadline
        self.status = status