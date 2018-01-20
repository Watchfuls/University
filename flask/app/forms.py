from flask_wtf import Form
from wtforms import StringField,IntegerField
from wtforms.validators import DataRequired

class todoForm(Form):
    taskstring = StringField('taskstring', validators=[DataRequired()])
    completedstring = StringField('completedstring', validators=[DataRequired()])
class JobsForm(Form):
    jobs = IntegerField('jobs')
class RemoveForm(Form):
    removestring = StringField('removestring')