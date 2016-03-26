import requests
import json

# the url of the API
url = "https://api.whatismybrowser.com/api/v1/user_agent_parse"

# put your api key in this variable:
user_key = ""

# a small list of example user agents
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2357.124 Safari/537.36'

# -- prepare data for the API request
post_data = {
    'user_key': user_key,
    'user_agent': user_agent,
}

# -- make the request to the whatismybrowser server
result = requests.post(url, data=post_data)

if result.status_code != 200:
    print(result.text)

# -- try to decode the api response as json
try:
    result_json = result.json()
except Exception as e:
    print(e)

# -- check the API request was successful
if result_json.get('result') != "success":
    raise Exception("The API did not return a 'success' response. It said: result: %s, message_code: %s, message: %s" % (result_json.get('result'), result_json.get('message_code'), result_json.get('message')))

# now you have "result_json" and can store, display or process any part of the response.
# for example:
print(result_json.get('parse').get('simple_browser_string'))

# -- print the entire json dump for reference
print(json.dumps(result_json, indent=2))
