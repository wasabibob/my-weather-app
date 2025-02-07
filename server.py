import os
import ldclient
from ldclient import Context
from ldclient.config import Config
from flask import Flask, render_template, request
from weather import get_current_weather
from waitress import serve

# Set sdk_key to your LaunchDarkly SDK key.
sdk_key = os.getenv('LAUNCHDARKLY_SDK_KEY')

# Set feature_flag_key to the feature flag key you want to evaluate.
feature_flag_key = os.getenv('LAUNCHDARKLY_FLAG_KEY', 'new-banner')

# Set this environment variable to skip the loop process and evaluate the flag
# a single time.
ci = os.getenv('CI')

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/weather')
def get_weather():
    city = request.args.get('city')

    # Check for empty strings or string with only spaces
    if not bool(city.strip()):
        # You could render "City Not Found" instead like we do below
        city = "Denver"
    
    flag_value = ldclient.get().variation(feature_flag_key, context, False)
    show_evaluation_result(feature_flag_key, flag_value)

    if ci is None:
        change_listener = FlagValueChangeListener()
        listener = ldclient.get().flag_tracker \
            .add_flag_value_change_listener(feature_flag_key, context, change_listener.flag_value_change_listener)
        
#        with Halo(text='Waiting for changes', spinner='dots'):
#            try:
#                Event().wait()
#            except KeyboardInterrupt:
#                pass
    weather_data = get_current_weather(city)
    
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
        # Set up the evaluation context. This context should appear on your
        # LaunchDarkly contexts dashboard soon after you run the demo.
        context = \
            Context.builder('example-user-key').kind('weather-city').name(city).tempature(temp).build()
        
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
    
    serve(app, host="0.0.0.0", port=8000)
#    app.run(host="0.0.0.0", port=8000)