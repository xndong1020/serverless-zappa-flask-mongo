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

## Step 02: Create/update deployment
```
For init deployment:
zappa deploy <target env>
Example:
zappa deploy dev

For update
zappa update <target env>
Example:
zappa update dev
```