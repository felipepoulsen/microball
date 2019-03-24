# API to post results of matches and get results of matches

## Prerequisites

Python 3

## Prerequisites for deployment with zappa

awscli
zappa

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
