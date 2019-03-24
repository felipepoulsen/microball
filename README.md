# API to post results of matches and get results of matches

## Prerequisites
```
python
```
## Prerequisites for deployment with zappa
```
awscli
zappa
```
## Installation

Download the source code
```
git clone https://github.com/felipepoulsen/microball.git
cd microball
```

Install the required packages:
```
pip install -r requirements.txt
```

Create a new virtual environment:
```
virtualenv .env
source .env/bin/activate
```
## Deployment
If you have installed zappa you can deploy by running 
```
zappa init
zappa deploy dev
```

If you make changes to the app, you can redeploy using 
```
zappa update dev
```

Otherwise, you can start the webserver locally by running
```
flask run
```
## Try it out
Try out the API by entering a result for match 1:
```
curl <URL>/moneyball-api/match_id/1 -d "result=10-7" -X PUT
```
and reading the result for match 1:
```
curl <URL>/moneyball-api/match_id/1
```
The `<URL>` is the deployment URL, which is given when running:
```
zappa deploy dev
```