This project is created using  [Zappa](https://github.com/Miserlou/Zappa) , [Flask](http://flask.pocoo.org/) and [MongoDB](https://www.mongodb.com/)

[![serverless](http://public.serverless.com/badges/v3.svg)](http://www.serverless.com)

Before deployment to AWS, make sure you have activated your virtual environment(pipenv or virtualenv, I recommend pipenv)

The root url for this API is https://hrbw32jk0d.execute-api.us-east-2.amazonaws.com/dev/
1. All requests
GET https://hrbw32jk0d.execute-api.us-east-2.amazonaws.com/dev/requests

2. Create request
POST https://hrbw32jk0d.execute-api.us-east-2.amazonaws.com/dev/requests

3. All response
GET https://hrbw32jk0d.execute-api.us-east-2.amazonaws.com/dev/responses

4. Create response
POST https://hrbw32jk0d.execute-api.us-east-2.amazonaws.com/dev/responses



## Step 01 : Test Locally
```
pipenv install
pipenv shell
python my_app.py
```
Then the root url will be http://localhost:5000/, and the resources will be located at http://localhost:5000/requests, http://localhost:5000/reponses

## Optional Step 02: Setup your aws credentials, you don't need to follow if you just want to test locally
```
npm i -g serverless

serverless config credentials --provider aws --key <your_access_key> --secret <your_access_secret> --profile <your_profile>
```

## Optional Step 03: Deployment, you don't need to follow if you just want to test locally
new deployment
```
zappa deploy dev 
```

or update existing deployment
```
zapp update dev
```