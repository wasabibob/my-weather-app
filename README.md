<a id="readme-top"></a>

<br />
<div align="center">
<h3 align="center">Demo Python Weather Webapp</h3>

  <p align="center">
    This is a example demo project for the purpose of showing the integration with LaunchDarkly and the Python SDK
    <br />
  </p>
</div>

---

### Sources and Inspiration
🚀 This repository includes an example demo webapp which was derrived and inspired by the resources referenced\
🔗 [Dave Gray Python Course](https://github.com/gitdagray/python-course/)\
🔗 [LaunchDarkly Python Example](https://github.com/launchdarkly/hello-python)

### 📚 Built With Reference
🔗 [Python Official Site](https://www.python.org/)\
🔗 [Visual Studio Code Official Site](https://code.visualstudio.com/)\
🔗 [Python Module Index](https://docs.python.org/3/py-modindex)\
🔗 [Python Standard Library](https://docs.python.org/3/library/ind)\
🔗 [Python Package Index (PyPI)](https://pypi.org/)\
🔗 [Flask](https://flask.palletsprojects.com/)\
🔗 [OpenWeatherMap.org API](https://openweathermap.org/)\
🔗 [LaunchDarkly Python SDK](https://docs.launchdarkly.com/sdk/server-side/python)

<!-- GETTING STARTED -->
## Getting Started

It's pretty simple... 
* Get a free account at [LaunchDarkly](https://docs.launchdarkly.com/home/getting-started) (if you don't already have one)
  * Create an LaunchDarkly SDK (API) Access Token and a Feature Flag as part of the getting started process
  * Copy and save the LaunchDarkly SDK Key for use later
* Get a free account with [OpenWeatherMap.org](https://openweathermap.org) and create an API Token
  * A usable API token should be automatically created for you upon account creation
  * It should be available inside your profile, under "My API Keys"
* clone this [repository](https://github.com/wasabibob/my-weather-app). then build, run & test

### Prerequisites

* Install Python3 [installation package](https://www.python.org/downloads/)
* Ensure you can run [pip](https://docs.docker.com/get-started/](https://packaging.python.org/en/latest/tutorials/installing-packages/#ensure-pip-setuptools-and-wheel-are-up-to-date)

## Build

1. Ensure you have registered for a [free trial account](https://docs.launchdarkly.com/home/getting-started#1-sign-up-for-a-free-trial) with LaunchDarkly
1. Create an [Personal Access Token](https://docs.launchdarkly.com/home/account/api-create/?q=create+access#create-access-tokens) for your SDK API connection giving the Role `writer` access
   **Copy and save the token value for future use** 
1. [Create a Feature Flag](https://docs.launchdarkly.com/home/getting-started#3-create-your-first-feature-flag) named `new-banner`to use for this exercise
1. Set the necessary environment variables
  * Note: `LAUNCHDARKLY_SDK_KEY` should be set to the LaunchDarkly SDK key for the environment you want to use
  * Note: `LAUNCHDARKLY_FLAG_KEY` should be set to the flag key of the flag you'll be using to toggle your new banner on and off. Unless you have a really good reason to change it, please leave this set to `new-banner`.
   ```bash
   export LAUNCHDARKLY_SDK_KEY="<Your SDK KEY>"
   export LAUNCHDARKLY_FLAG_KEY="new-banner"
   ```
   NOTE: you can optionally set the environment variable "CI" to skip evaluating the feature flag
   ```
   export CI="true"
   ``` 
1.  Clone the repo
    ```bash
    git clone git@github.com:wasabibob/my-weather-app
    ```
    
1. Install Python Virtual Environment, upgrade pip. From the top folder of the cloned repo.
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install --upgrade pip
   ```
   Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the required dependencies

   ##### Windows:
   ```zsh
   pip install -r requirements.txt 
   ```

   ##### macOS/Linux:
   ```zsh
   pip3 install -r requirements.txt
   ``` 
1. Initialize the user database
   ```
   python3
   >>> from server import db
   >>> db.create_all()
   >>> quit()
   ```
   Verify the table was create in the database
   ```
   sqlite3 database.db
   sqlite> .tables
   sqlite> .schema user
   Ctl + C
   ```
   **Note:** The above squlite3 commands should return something like this:\
   sqlite> .tables\
   user\
   sqlite> .schema user\
   CREATE TABLE user (\
        &emsp; id INTEGER NOT NULL, \
        &emsp; username VARCHAR(20) NOT NULL, \
        &emsp; password VARCHAR(80) NOT NULL, \
        &emsp; country VARCHAR(20), \
        &emsp; PRIMARY KEY (id), \
        &emsp; UNIQUE (username)\
   );

## Run Locally
   See the feature live Run the python app image in your local environment from the terminal window
   
### In a terminal window From the application source home directory (my-weather-app)
* To run in CLI mode (one-off) and validate your connection to OpenWeatherMap.org and LaunchDarkly
   ```bash
   python3 weather.py
   ```
   Enter a city on the command line prompt and it will connect to the API and return weather data
   * Note: If you receive a 401 error here, wait a few minutes and try again. It takes OpenWeather a little while to initialize a new account.

* To run the this app in the Flask webserver. Once running, you can see the app by opening a browser and browsing to **localhost:8000**
   ```bash
   python3 server.py
   ```
   NOTE: You should receive the message in the CLI "The **FLAG KEY** feature flag evaluates to **FLAG VALUE**"\
         The application will run continuously and react to the flag changes in LaunchDarkly
## Test

### From desktop browser

1. Navigate to **locahost:8000/index** and enter a city to retrieve weather information
2. Toggle the LaunchDarkly Flag to turn on or off the travel banner

<p align="right">(<a href="#readme-top">back to top</a>)</p>


