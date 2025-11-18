from flask import Flask, render_template, request,redirect, url_for
from flask_login import LoginManager, login_user, login_required
from models import Usuario
from db import db

app = Flask(__name__)
app.secret_key = 'Vinicius'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
lm = LoginManager(app)
db.init_app(app)

@lm.user_loader
def user_loader(id):
    usuario = db.session.query(Usuario).filter_by(id=id).first()
    return usuario

@app.route('/')

def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        nome = request.form['nomeFOrm']
        senha = request.form['senhaForm']


@app.route('/registrar', methods=['GET', 'POST'])
def registrar():
    if request.method == 'GET':
        return render_template('registrar.html')
    elif request.method == 'POST':
        nome = request.form['nomeForm']
        senha = request.form['senhaForm']

        novo_usuario = Usuario(nome=nome, senha=senha)
        db.session.add(novo_usuario)
        db.session.commit()

        login_user(novo_usuario)

        return redirect(url_for('home'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
