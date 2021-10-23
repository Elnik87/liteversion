from flask import Blueprint, render_template, request
from werkzeug.utils import redirect
from route import db
from models import Feedback

feedback = Blueprint("feedback", __name__, template_folder="templates")

@feedback.route('/', methods = ["POST", "GET"])
def feedback_add():
    if request.method == 'POST':
        name = request.form['name']
        last_name = request.form['last_name']
        body = request.form['body']


        feedback = Feedback(name=name, last_name=last_name, body=body)
        try:
            db.session.add(feedback)
            db.session.commit()
            return redirect('/')
        except:
            return "Ошибка"
    else:
        return render_template("/")




