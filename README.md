# 1. Getting App to Run Locally (MacOS)

## Step 1: Clone Repo
```bash
git clone https://github.com/tree-in-education/roots.git roots
```

## Step 2: Install Dependencies
```bash 

# install python requirements
pip3 install -r requirements.txt

```

## Step 3: Run Flask
```bash
# from the sound_city_server directory:
export FLASK_APP=main.py
flask run
# now, navigate to http://127.0.0.1:5000/
```

In order to run the code, you have to ensure that Flask is running. After you get everything installed, you will be able to access your application in the future by just performing Step 3. 


# 2. Getting App to Run on Heroku

## Step 1: Initialization
1. Install the Heroku Command Line tools <a href="https://devcenter.heroku.com/articles/heroku-cli#download-and-install" target="_blank">Heroku CLI</a>:
    * Mac: `brew tap heroku/brew && brew install heroku`
1. Create a new app on Heroku by logging into the Heroku website and using the Web UI.
1. Using the heroku command line client:
   * Go to your command line and login:<br> `heroku login -i`
   * Connect your local git repo (assumes you have already done this) to your newly created Heroku app:<br> `heroku git:remote -a 'app-you-just-made'`
1. Push your repo to Heroku: `git push heroku master`

This will create your app and install all of the Python dependencies listed in your requirements.txt. It will also read your Procfile and see that you've created a web application (via Flask).

## Step 2: Configuration 
You will need to perform a few more steps in order to get Tesseract and OpenCV to work:

1. Go to the "settings" tab of your application and add the following buildpack:
https://github.com/heroku/heroku-buildpack-apt. This will allow you to install Ubuntu packages (OpenCV, etc.), which can be specified in the Aptfile.

2. This should be all that you need to configure Heroku, commit your changes and redeploy to Heroku by pushing an empty commit to Heroku:

```bash
git commit --allow-empty -m "empty commit"
git push heroku master
```
