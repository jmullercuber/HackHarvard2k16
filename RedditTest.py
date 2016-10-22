import json, httplib


#Connect to reddit for json requests
conn = httplib.HTTPSConnection('www.reddit.com')

#Get the hot posts in r/worldnews
conn.request("GET", "/r/worldnews/hot/.json")
response = conn.getresponse()
sr_data = response.read()
sr_data = json.loads(sr_data) # Convert from json to dict

#Get the comments page for the top post in r/worldnews
conn.request("GET", sr_data['data']['children'][0]['data']['permalink'] + '.json')
response = conn.getresponse()
p_data = response.read()
p_data = json.loads(p_data) # Convert from json to dict
tl_posts = p_data[1]['data']['children'] # The top level posts

# Parse top level bodies
top_replies = []
for post in tl_posts:
	if 'body' in post['data']:
		top_replies.append(post['data']['body'])	
	
# Generate MS api request body for sentiment
c_body = dict()
c_body['stop_words'] = []
c_body['topicsToExclude'] = []
c_body['documents'] = []
count = 0
for reply in top_replies:
	d = dict()
	d['id'] = str(count)
	d['text'] = reply
	c_body['documents'].append(d)
	count += 1

#Headers for MS API
headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': 'b3f5d9f8d81046598dedc07a7541e2c9',
}

#Send request to MS API
conn2 = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
conn2.request("POST", "/text/analytics/v2.0/sentiment", json.dumps(c_body), headers)
response = conn2.getresponse()
data = response.read()
data = (json.loads(data))
data = data['documents']
conn2.close()	

	
conn.close()