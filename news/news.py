from flask import Blueprint, render_template, request
from werkzeug.utils import redirect
from route import db
from models import News

news = Blueprint("news", __name__, template_folder="templates")

@news.route("/")
def newses():
    news = News.query.all()
    return render_template("news/news.html", news=news)

@news.route("/<slug>")
def news_detail(slug):
    news_detail = News.query.filter(News.slug==slug).first()
    return render_template("news_detail/detail.html", news_detail=news_detail)

@news.route('/<slug>/delete')
def delete(id):
    news = News.query.get_or_404(id)
    try:
        db.session.delete(news)
        db.session.commit()
        return redirect('/')
    except:
        return "Ошибка"


@news.route('/<slug>/create', methods=['POST', 'GET'])
def create(id):
    news = News.query.get(id)

    if request.method == 'POST':
        news.title = request.form['title']
        news.content = request.form['content']
        try:
            db.session.commit()
            return redirect('/')
        except:
            return "Ошибка"

    return render_template("news/news.html", news=news)


@news.route('/klerjflsejtalsef;lasm;oete;rogmzxd;lfkeargj')
def admin():
    news = News.query.order_by(News.date.desc()).all()
    return render_template("/news/admin.html", news=news)


@news.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == "Elnik" and password == "12345":
            return redirect("/klerjflsejtalsef;lasm;oete;rogmzxd;lfkeargj")
        else:
            return redirect("/")
    else:
        return render_template("news/login.html")