import os
import ldclient
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from flask_bcrypt import Bcrypt
from ldclient import Context
from ldclient.config import Config
from weather import get_current_weather
from waitress import serve
from dotenv import load_dotenv
from threading import Lock, Event

# Set sdk_key to your LaunchDarkly SDK key.
sdk_key = os.getenv('LAUNCHDARKLY_SDK_KEY')

# Set feature_flag_key to the feature flag key you want to evaluate.
feature_flag_key = os.getenv('LAUNCHDARKLY_FLAG_KEY', 'new-banner')

# Set this environment variable to skip the loop process and evaluate the flag
# a single time.
#ci = os.getenv('CI')

app = Flask(__name__)
load_dotenv()
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'thisisasecretkey'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@app.route('/city-not-found')
def city_not_found(weather_data):
    if not weather_data['cod'] == 200:
        return render_template('city-not-found.html')

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)
    country = db.Column(db.String(20), nullable=True)
    
class RegisterForm(FlaskForm):
    username = StringField(validators=[
                            InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})
    password = PasswordField(validators=[
                            InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Password"})
    country = StringField(validators=[
                            InputRequired(), Length(min=2, max=20)], render_kw={"placeholder": "Country"})
    submit = SubmitField('Register')

    def validate_username(self, username):
        existing_user_username = User.query.filter_by(
            username=username.data).first()
        if existing_user_username:
            raise ValidationError(
                'That username already exists. Please choose a different one.')
            
class LoginForm(FlaskForm):
    username = StringField(validators=[
                            InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})
    
    password = PasswordField(validators=[
                            InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Password"})
    
    submit = SubmitField('Login')

@app.route('/')
@app.route('/index')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('get_weather'))
    else:
        return redirect(url_for('login'))
 
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    print(form.errors)

    if form.is_submitted():
        print("submitted")

    if form.validate():
        print("valid")

    print(form.errors)
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                get_weather()
                return redirect(url_for('get_weather'))
    return render_template('login.html', form=form)

@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@ app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        new_user = User(username=form.username.data, password=hashed_password, country=form.country.data)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template('register.html', form=form)

@app.route('/weather')
def get_weather():
    
    city = request.args.get('city')
    city = city if city else "Denver"
    
    # Check for empty strings or string with only spaces
    if not bool(city.strip()):
        # You could render "City Not Found" instead like we do below
        city = "Denver"
    
    # Set up the evaluation context. This context should appear on your
    # LaunchDarkly contexts dashboard soon after you run the demo.
    #context = \
    #    Context.builder('example-user-key').kind('weather-city').name(city).build()
    context = Context.builder("example-user-key").kind("user").name("Tony").build()
    
    # Evaluate the feature flag
    flag_value = ldclient.get().variation(feature_flag_key, context, False)
    show_evaluation_result(feature_flag_key, flag_value)
    
    # Add a listener to the flag
    change_listener = FlagValueChangeListener()
    listener = ldclient.get().flag_tracker \
        .add_flag_value_change_listener(feature_flag_key, context, change_listener.flag_value_change_listener)
    
        # Query all  users for debug
    users = User.query.all()

    # Print the data for debug
    for user in users:
        print(f"ID: {user.id}, Name: {user.username}, Country: {user.country}")

    app.logger.debug("current user ID is %s", current_user.id)
    username = current_user.username
    app.logger.debug("user is %s", username)
    country_code = current_user.country
    app.logger.debug("country is %s", country_code)
    weather_data = get_current_weather(city)
    app.logger.debug("weatther data: %s", weather_data)
    
    # City is not found by API
    if not weather_data['cod'] == 200:
        return render_template('city-not-found.html')
    
    if flag_value is False:
        return render_template(
            "weather.html",
            title=weather_data["name"],
            status=weather_data["weather"][0]["description"].capitalize(),
            temp=f"{weather_data['main']['temp']:.1f}"
        )
    else:
        return render_template(
            "weather-plus.html",
            title=weather_data["name"],
            status=weather_data["weather"][0]["description"].capitalize(),
            temp=f"{weather_data['main']['temp']:.1f}",
            feels_like=f"{weather_data['main']['feels_like']:.1f}"
        )

def show_evaluation_result(key: str, value: bool):
    print()
    print(f"*** The {key} feature flag evaluates to {value}")

    if value:
        print()
        #print(f"*** The {key} feature flag evaluates to {value}")
        
class FlagValueChangeListener:
    def flag_value_change_listener(self, flag_change):
        show_evaluation_result(flag_change.key, flag_change.new_value)

if __name__ == "__main__":
    # Check for the LaunchDarkly SDK key & feature flag key
    if not sdk_key:
        print("*** Please set the LAUNCHDARKLY_SDK_KEY env first")
        exit()
    if not feature_flag_key:
        print("*** Please set the LAUNCHDARKLY_FLAG_KEY env first")
        exit()

    # Initialize the LaunchDarkly SDK
    ldclient.set_config(Config(sdk_key))
    
    if not ldclient.get().is_initialized():
        print("*** SDK failed to initialize. Please check your internet connection and SDK credential for any typo.")
        exit()
    
    print("*** SDK successfully initialized")
    
    app.run(host="0.0.0.0", debug=True, port=8000)
    #use serve if you want to use waitress or publish to render.com
    #serve(app, host="0.0.0.0", port=8000)