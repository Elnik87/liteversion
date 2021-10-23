from flask import Blueprint, render_template, request
from werkzeug.utils import redirect
from liteversion import db
from .models import News

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


@news.route('/create', methods=['POST', 'GET'])
def create():

    if request.method == 'POST':
        news_simple = News(title=request.form["title"], content=request.form["content"])
        # news_simple.title = request.form['title']
        # news_simple.content = request.form['content']
        try:
            db.session.add(news_simple)
            db.session.commit()
            return redirect('/news')
        except:
            return "Ошибка"

    return render_template("news/create.html")


@news.route('/klerjflsejtalsef;lasm;oete;rogmzxd;lfkeargj')
def admin():
    news = News.query.order_by(News.date.desc()).all()
    return render_template("/news/admin.html", news=news)


@news.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print(username, password)
        if username == "Elnik" and password == "12345":
            return redirect("klerjflsejtalsef;lasm;oete;rogmzxd;lfkeargj")
        else:
            return redirect("login")
    else:
        return render_template("news/login.html")