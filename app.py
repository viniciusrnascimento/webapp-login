from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from models import Usuario
from db import db
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

lm = LoginManager(app)
lm.login_view = 'login'

db.init_app(app)

@lm.user_loader
def user_loader(id):
    return db.session.query(Usuario).filter_by(id=id).first()


@app.route('/')
@login_required
def home():
    return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    nome = request.form['nomeForm']
    senha = request.form['senhaForm']

    user = db.session.query(Usuario).filter_by(nome=nome, senha=senha).first()

    if not user:
        return 'Nome ou senha incorretos'

    login_user(user)
    return redirect(url_for('home'))


@app.route('/registrar', methods=['GET', 'POST'])
def registrar():
    if request.method == 'GET':
        return render_template('registrar.html')

    nome = request.form['nomeForm']
    senha = request.form['senhaForm']

    novo_usuario = Usuario(nome=nome, senha=senha)
    db.session.add(novo_usuario)
    db.session.commit()

    login_user(novo_usuario)
    return redirect(url_for('home'))


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
