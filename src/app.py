from flask import Flask, render_template, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

from api.config import Config
from api.forms import RegistrationForm, LoginForm, PokemonForm
from api.models import db, User, Pokemon


app = Flask(__name__)
app.config.from_object(Config)


db.init_app(app)


login_manager = LoginManager(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# ---- RUTAS ----


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():

        existing = User.query.filter_by(email=form.email.data).first()
        if existing:
            flash("Este email ya está registrado.", "danger")
            return redirect(url_for("register"))
        

        hashed_pw = generate_password_hash(form.password.data)
        new_user = User(
            username=form.username.data,
            email=form.email.data, 
            password=hashed_pw
            )
        db.session.add(new_user)
        db.session.commit()


        flash('Registro exitoso. Ahora puedes iniciar sesión.', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html', form=form)



@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        
        user = User.query.filter_by(email=form.email.data).first()
        
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            flash('Inicio de sesión exitoso.', 'success')
            return redirect(url_for('pokedex'))
        else:
            flash('Email o contraseña incorrectos.', 'danger')
    return render_template('login.html', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Has cerrado sesión.', 'info')
    return redirect(url_for('home'))


@app.route('/pokedex')
@login_required
def pokedex():
    pokemons = Pokemon.query.all()
    return render_template('pokedex.html', pokemons=pokemons)


@app.route('/pokemon/<int:pokemon_id>')
@login_required
def pokemon_detail(pokemon_id):
    pokemon = Pokemon.query.get_or_404(pokemon_id)
    return render_template('pokemon_detail.html', pokemon=pokemon)


@app.route('/add_pokemon', methods=['GET', 'POST'])
@login_required
def add_pokemon():
    form = PokemonForm()
    if form.validate_on_submit():
        new_pokemon = Pokemon(
            name=form.name.data,
            type=form.type.data,
            description=form.description.data,
            image_url=form.image_url.data
        )
        db.session.add(new_pokemon)
        db.session.commit()


        flash('Pokémon agregado.', 'success')
        return redirect(url_for('pokedex'))
    
    return render_template('add_pokemon.html', form=form)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
