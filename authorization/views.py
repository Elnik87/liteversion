from flask import Blueprint, render_template, request, flash, url_for
from flask_login import login_user, login_required, logout_user
from werkzeug.security import check_password_hash
from werkzeug.utils import redirect

from feedback.models import Feedback
from news.models import News
from liteversion import db
from .models import User

admin = Blueprint("admin", __name__, template_folder="templates")


@admin.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        login = request.form.get('login')
        password = request.form.get('password')
        if login == "Elnik" and password == "12345":
            user = User.query.filter_by(login=login).first()
            if check_password_hash(user.password, password):
                login_user(user)
                redirect("/admin")
            else:
                flash('Что-то неправильно ввел')
        else:
            flash('Что-то неправильно ввел')
            return redirect("/")
    else:
        return render_template("authorization/login.html")


@admin.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("/"))


@admin.after_request
def redirect_to_authorization(response):
    if response.status_code == 401:
        return redirect(url_for("login"))


@admin.route('/<slug>/news_update')
@login_required
def news_update(slug):
    news = News.query.filter(News.slug == slug).first()
    return render_template("authorization/news_update.html", news=news)


@admin.route('/<slug>/news_update_create')
@login_required
def news_update_create(slug):
    news = News.query.get(slug)
    if request.method == 'POST':
        news.title = request.form["title"]
        news.content = request.form["content"]
        try:
            db.session.commit()
            return redirect('')
        except:
            return "Ошибка"
    else:
        news = News.query.get(slug)
        return render_template("authorization/news_update_create.html", news=news)


@admin.route('/<slug>/news_delete')
@login_required
def news_delete(slug):
    news = News.query.get_or_404(slug)
    try:
        db.session.delete(news)
        db.session.commit()
        return redirect('/')
    except:
        return "Ошибка"


@admin.route('/create', methods=['POST', 'GET'])
@login_required
def create():
    if request.method == 'POST':
        news_simple = News(title=request.form["title"], content=request.form["content"])
        # title = request.form['title']
        # content = request.form['content']
        try:
            db.session.add(news_simple)
            db.session.commit()
            return redirect('')
        except:
            return "Ошибка"
    else:
        return render_template("authorization/create.html")


@admin.route('/')
@login_required
def admins():
    news = News.query.order_by(News.date.desc()).all()
    feedbacks = Feedback.query.order_by(Feedback.date.desc()).all()
    return render_template("authorization/admin.html", news=news, feedbacks=feedbacks)
