import json, httplib, time

# Headers for MS API
headers = {
	# Request headers
	'Content-Type': 'application/json',
	'Ocp-Apim-Subscription-Key': 'b3f5d9f8d81046598dedc07a7541e2c9',
}

def documents_to_sentiments(docs):
    # Generate MS api request body for sentiment
	c_body = { 'documents': [
		{
			'id': str(i),
			'text': docs[i],
		}
		for i in range(len(docs))
		if docs[i] != ""
	]}
	
	global headers
		
	# Send request to MS API
	conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
	conn.request("POST", "/text/analytics/v2.0/sentiment", json.dumps(c_body), headers)
	response = conn.getresponse()
	data = response.read()
	conn.close()
	
	res = {'body': c_body, 'result': json.loads(data)}
	
	return res

def documents_to_topics(docs):
    # Generate MS api request body for sentiment
	c_body = {
		'stop_words': [],
		'topicsToExclude': [],
		'documents': [
			{
				'id': str(i),
				'text': docs[i],
			}
			for i in range(len(docs))
		],
	}

	# Send request to MS API
	conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
	conn.request("POST", "/text/analytics/v2.0/topics", json.dumps(c_body), headers)
	response = conn.getresponse()
	
	op_loc = response.getheader('operation-location')
	print(response.getheaders())
	print(op_loc)
	op_loc = op_loc[op_loc.index('.com') + 4 :]
	
	print(op_loc)
	
	res = {'body': c_body}
	
	while True:
		time.sleep(5)
		conn2 = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
		conn2.request("GET", op_loc, '', headers)
		response = conn2.getresponse()
		data = response.read()
		data = json.loads(data)
		if 'status' in data:
			print(data['status'])
			if data['status'] == 'Succeeded':
				res['result'] = data
				break
		conn2.close()
			
	conn.close()
	return res