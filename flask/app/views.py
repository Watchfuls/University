from flask import render_template, flash
from app import app,db, models
from .forms import todoForm, JobsForm, RemoveForm
from .models import Task
@app.route('/todo', methods=['GET', 'POST'])
def todo():
    j = ""
    b = ""
    RForm = RemoveForm()
    form = todoForm()
    jobform = JobsForm()
    if form.validate_on_submit():
        flash('Succesfully received task: ' + str((form.taskstring.data)) + ' | Completed? : ' + str((form.completedstring.data)))
        t = models.Task(TaskName = str(form.taskstring.data), Completed = str(form.completedstring.data))
        db.session.add(t)
        db.session.commit()
        
    if jobform.validate_on_submit():
        b = ""
        if (jobform.jobs.data == 10):

            for TaskName in db.session.query(Task.TaskName).filter_by(Completed = "Yes"):
                j =  j + str(TaskName)
            j = "Completed: " + j
    if (jobform.jobs.data == 5):
        j = ""
        for TaskName in db.session.query(Task.TaskName).filter_by(Completed = "No"):
            b = b + str(TaskName)
        b = "Not completed: " +  b
    done = {'j': j}
    doing = {'b': b}
    
    x = ""
    if RForm.validate_on_submit():
        for Task.id in db.session.query(Task).filter_by(TaskName = str(RForm.removestring.data),Completed = str("No")):
            db.session.delete(Task.id)
            x = str(Task.id)
            t = models.Task(TaskName = str(RForm.removestring.data), Completed = str("Yes"))
            db.session.add(t)
        db.session.commit()
        flash('Succesfully Marked as complete task: ' + RForm.removestring.data + ' ID: ' + str(x)[27:-1])
        
            
    
    return render_template('todo.html',
                           title='To-Do List',
                           doing = doing,
                           done = done,
                           remove=RForm,
                           jobs=jobform,
                           todo=form)
    
