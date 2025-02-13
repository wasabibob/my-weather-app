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
  * Create an API Key and a Feature Flag as part of the getting started process
* Get a free account with [OpenWeatherMap.org](https://openweathermap.org) and create an API key
* clone this [repository](https://github.com/wasabibob/my-weather-app). then build, run & test

### Prerequisites

* Install Python3 [installation package](https://www.python.org/downloads/)
* Install [pip](https://docs.docker.com/get-started/)
* 


## Build

1. Set the environment variable `LAUNCHDARKLY_SDK_KEY` to your LaunchDarkly SDK key. If there is an existing boolean feature flag in your LaunchDarkly project that you want to evaluate, set `LAUNCHDARKLY_FLAG_KEY` to the flag key; In this exaqmple `new-banner`.

    ```bash
    export LAUNCHDARKLY_SDK_KEY="1234567890abcdef"
    export LAUNCHDARKLY_FLAG_KEY="new-banner"
    ```
1. [Sign up](https://openweathermap.org/appid#signup) for a free account at OpenWeatherMap.org and create an API key
1. ? Ensure you have [Poetry](https://python-poetry.org/) installed.
1. ? Install the required dependencies with `poetry install`.

1.  Clone the repo
   ```bash
   git clone git@github.com:wasabibob/my-weather-app
   ```
1. ? build
   ```bash
   cd my-weather-app
   docker build .
   ```   

    
   
## Run Lcally

Run the built image in docker on in your local environment from the terminal window or from docker desktop application\
Once running, you can see the app by opening a browser and browsing to **localhost:5500**

### In a terminal

From the application source home directory (my-weather-app)
```python3 weather.py
   ```
1. On the command line, run `poetry run python main.py`
You should receive the message "The <flagKey> feature flag evaluates to <flagValue>.". The application will run continuously and react to the flag changes in LaunchDarkly.```


## Test

### From desktop browser

1. Navigate to images tab and locate your most recent build (typicaly at the bottom of the list)
2. Click on the play/run button under the Actions column
3. In the **Run a new container** diaglog box, under **Optional setting**, replace **Host port** with the value **5500**
4. Click **Run**

5. 
1. Tests are functions defined in the tests.py file
2. These will automatically run as part of the **GitHub Actions Workflow** which is found in the .github/workflows folder
3. To run the workflow, simply commit a change to your GitHub repsoitory, this will start the GitHub Actions Workflow
4. In your browser, navigate to your GitHub repository and slect the **Actions** tab
5. Click on the most recent workflow (named after your recent commit)
6. In the **docker-image.yaml** workflow select the **docker** run to see the test results as part of the workflow output


<p align="right">(<a href="#readme-top">back to top</a>)</p>


