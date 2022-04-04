
# Welcome to the WayBackStack! #

This project will deploy an AWS Cloudformation stack that consists of two primary assets (Lambda Function and an Eventbridge rule to trigger said function) as well as associated assets such as roles/policies/etc. 

## Purpose ##

The purpose of this project is to automate archival of web pages to the internet archive at [web.archive.org](). In summary, an time based event will trigger a serverless function which will iterate over a list of urls, requesting each url be archived, waiting an amount of time, then requesting the next url on the list. 

## Getting Started ##

### Requirements ###
- AWS CDK `v2.19` (maybe older)
- Docker
- Python3
- pip3
- AWS Account and credentials 
    - stored in `.aws/credentials`
    - or some other manner of authenticating

### Create Virtual Environment ###

__MacOS and Linux:__

- Create and activate Virtual Environment:

```
python3 -m venv .venv
$ source .venv/bin/activate
```

__Windows__

- Create and activate Virtual Environment:

```
python3 -m venv .venv
.venv\Scripts\activate.bat
```

__Install the required dependencies__

```
$ pip install -r requirements.txt
```

### Build and Deploying ###

- Build (make sure docker is running)

```sh
cdk synth --no-staging
```

- Deploy (make sure you are sending to the correct account)

```sh
cdk deploy
```



## Modifying the Stack ##

### Modifying URLs ###
If you want to modify the list of urls, you can just do that and rebuild and deploy the stack (see above).  The list is managed in `/wayback_app/app.py` and can be expanded to close to 60 items before the timeout will need to be extended (see below). 

```python
 9  url_list = [
10      "https://api.cps.edu/health/help",
...
27  ]
```


It can be extended to near 180 accounting for the 15 minute Lambda execution time limit and the 5 second wait time in-between requests. This URL limit could potentially be increased to near 900 with the Lambda limit increased to max 0f 900 seconds and the wait time between wayback API requests reduced to 1 second.

### Extend Lambda Timeout ###
The Lambda is set to timeout after 300 seconds and the pause time in between requests is 5 seconds. This means if the list of URLs gets near 60, the timeout will need to be extended.  It is managed in `/wayback/wayback_stack.py`:

```python
25          timeout=Duration.seconds(300),
```

### Modify Wait In Between Requests ###

The time that the function waits in between requests is managed in `/wayback_app/app.py` and can be modified.

```python
36        signal.alarm(5) # resets alarm
```

### Modify Invocation Time ###

The Eventbridge Cron Job is manages in `wayback/wayback_stack.py` and follows standard crontab conventions and are set for the UTC timezone. Undeclared parameters (ie `day`, `month`, `week_day`, `year`) are set to `*` (eg. every `day` of the month). 

```python 
30            schedule=event.Schedule.cron(
31                minute="0", 
32                hour="9",
33                ),
```

## More Stuff ##

Explore and build more using the AWS CDK and python. Its fun. 
