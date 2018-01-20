from app import db

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    TaskName = db.Column(db.String(500))
    Completed = db.Column(db.String(10))
    
  
