# my-weather-app
The instructions need to explain — in detail — how the reader can run the example locally on their machine. Be sure to\
include relevant comments in the code, (e.g. where the SDK key needs to be replaced, or where afeature flag needs to be\
re-created by the user, etc.).

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
  * Create an LaunchDarkly SDK (API) Key and a Feature Flag as part of the getting started process
  * Copy and save the LaunchDarkly SDK Key for use later
* Get a free account with [OpenWeatherMap.org](https://openweathermap.org) and create an API key
* clone this [repository](https://github.com/wasabibob/my-weather-app). then build, run & test

### Prerequisites

* Install Python3 [installation package](https://www.python.org/downloads/)
* Ensure you can run [pip](https://docs.docker.com/get-started/](https://packaging.python.org/en/latest/tutorials/installing-packages/#ensure-pip-setuptools-and-wheel-are-up-to-date)

## Build

1. Set the environment variable `LAUNCHDARKLY_SDK_KEY` to your LaunchDarkly SDK key. If there is an existing boolean feature flag in your LaunchDarkly project that you want to evaluate, set `LAUNCHDARKLY_FLAG_KEY` to the flag key; In this exaqmple `new-banner`.
    ```bash
    export LAUNCHDARKLY_SDK_KEY="1234567890abcdef"
    export LAUNCHDARKLY_FLAG_KEY="new-banner"
    ```
    
1. [Sign up](https://openweathermap.org/appid#signup) for a free account at OpenWeatherMap.org and create an API key
   * Copy and save the API Key for use later

1.  Clone the repo
    ```bash
    git clone git@github.com:wasabibob/my-weather-app
    ```
    
1. Install Python Virtual Environment, waitress and the LaunchDarkly SDK
   ```bash
   cd my-weather-app
   python3 -m venv .venv
   source .venv/bin/activate
   pip install requests python-dotenv Flask
   pip install --upgrade pip
   pip install waitress
   pip install launchdarkly-server-sdk
   ```
   
1. Create .env file for environment variables, and put your OpenWeatherMap API key and the LaunchDarkly Key in this file
   ```bash
   cd my-weather-app
   touch .env
   echo "API_KEY=<put your OpenWeatherMap API key here>" >>.env
   echo "LAUNCHDARKLY_SDK_KEY=<put your LaunchDarkly SDK key here>" >>.env
   ```    
   
## Run Lcally

Run the python app image in your local environment from the terminal window\
Once running, you can see the app by opening a browser and browsing to **localhost:8000**

### In a terminal window From the application source home directory (my-weather-app)
* To run in CLI mode and validate your connection to OpenWeatherMap.org and LaunchDarkly
   ```bash
   python3 weather.py
   ```
You should receive the message "The <flagKey> feature flag evaluates to <flagValue>.". 
The application will run continuously and react to the flag changes in LaunchDarkly.```

* To run the this app in the Flask webserver and see the feature live
   ```bash
   python3 server.py
   ```

## Test

### From desktop browser

1. Navigate to images tab and locate your most recent build (typicaly at the bottom of the list)
2. 

<p align="right">(<a href="#readme-top">back to top</a>)</p>


