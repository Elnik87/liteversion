from flask import Blueprint, render_template, request, flash, url_for
from werkzeug.utils import redirect
from liteversion import db
from .models import Feedback

feedback = Blueprint("feedback", __name__, template_folder="templates")

@feedback.route('/', methods = ["POST", "GET"])
def feedback_add():
    if request.method == 'POST':
        name = request.form['name']
        last_name = request.form['last_name']
        body = request.form['body']
        feedback = Feedback(name=name, last_name=last_name, body=body)
        flash("Сообщение успешно отправлено")
        try:
            db.session.add(feedback)
            db.session.commit()
            return redirect(url_for("feedback.feedback_add"))
        except:
            return flash("Сообщение успешно неотправлено")

    return render_template("feedback/feedback.html")




