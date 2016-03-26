# api-sample-python-3
API Sample Code - Python 3.x

This is a small repository containing sample code for the WhatIsMyBrowser.com API. The code here is written for Python 3.x

Accessing the API is very straightforward and requires no "official" libraries - all you need to do is send a POST request to:

    https://api.whatismybrowser.com/api/v1/user_agent_parse

containing two parameters:

    user_key
    user_agent

The ```user_key``` parameter is your API key/token which you obtain by logging in to https://developers.whatismybrowser.com

The ```user_agent``` parameter is the particular User Agent you want the API to parse.

The API will return a response in JSON containing everything we are able to tell you based on that user agent.

## Sample code
To make it easy and neat to send HTTP requests in python, we recommend using the excellent ```requests``` python module. This is what is used in the sample code here.

## Using the sample code

We recommend using ```virtualenv``` to create a stand-alone python environment and then using ```pip``` to install ```requirements.txt``` into the virtualenv.

The only external requirement is the ```requests``` python library.
