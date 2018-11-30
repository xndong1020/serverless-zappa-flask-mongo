This project is created using [Zappa](https://github.com/Miserlou/Zappa), [Flask](http://flask.pocoo.org/) and [MongoDB](https://www.mongodb.com/)
Before deployment to AWS, make sure you are using virtual environment(pipenv or virtualenv, I recommend pipenv)

The root url for this API is https://hrbw32jk0d.execute-api.us-east-2.amazonaws.com/dev/
1. All requests
GET https://hrbw32jk0d.execute-api.us-east-2.amazonaws.com/dev/requests

2. Create request
POST https://hrbw32jk0d.execute-api.us-east-2.amazonaws.com/dev/requests

3. All response
GET https://hrbw32jk0d.execute-api.us-east-2.amazonaws.com/dev/reponses

4. Create response
POST https://hrbw32jk0d.execute-api.us-east-2.amazonaws.com/dev/reponses



## Step 01: Setup your aws credentials
```
npm i -g serverless

serverless config credentials --provider aws --key <your_access_key> --secret <your_access_secret> --profile <your_profile>
```

## Step 02 : Test Locally
```
pipenv install
python my_app.py
```
Then the root url will be http://localhost:5000/, and the resources will be http://localhost:5000/requests, http://localhost:5000/reponses