import cognitive, json, os.path, operator
# Establish connections to internet sources
from RedditScraper import RedditScraper


if __name__ == "__main__":
	# collect text data from them

	# For every source analyze text data with the Microsoft Cognitive Services Text Analytics API
	s_file_path = "./sentiments.data"
	if os.path.isfile(s_file_path):
		print("Importing sentiments...")
		s_file = open(s_file_path, 'r')
		sentiments = json.loads(s_file.read())
	else:
		sentiments = {
			source: cognitive.documents_to_sentiments(docs)
			for source, docs in internet_documents.items()
		}
		s_file = open('sentiments.data', 'w')
		s_file.write(json.dumps(sentiments))
		s_file.close()
	
	t_file_path = "./topics.data"
	if os.path.isfile(t_file_path):
		print("Importing topics...")
		t_file = open(t_file_path, 'r')
		topics = json.loads(t_file.read())
	else:
		topics = {
			source: cognitive.documents_to_topics(docs)
			for source, docs in internet_documents.items()
		}
		t_file = open('sentiments.data', 'w')
		t_file.write(json.dumps(topics))
		t_file.close()
	
	topics_by_score = {}
	documents_by_id = {}
	sentiments_by_doc_id = {}
	
	for i in range(len(topics['reddit-politics']['result']['operationProcessingResult']['topics'])):
		topics_by_score[topics['reddit-politics']['result']['operationProcessingResult']['topics'][i]['keyPhrase']] = topics['reddit-politics']['result']['operationProcessingResult']['topics'][i]['score']
		
	for i in range(len(topics['reddit-politics']['body']['documents'])):
		documents_by_id[topics['reddit-politics']['body']['documents'][i]['id']] = topics['reddit-politics']['body']['documents'][i]['text']
		
	for i in range(len(sentiments['reddit-politics']['result']['documents'])):
		sentiments_by_doc_id[sentiments['reddit-politics']['result']['documents'][i]['id']] = sentiments['reddit-politics']['result']['documents'][i]['score']
		
	sorted = sorted(topics_by_score.items(), key=operator.itemgetter(1))
	
	for item in sorted:
		print(item[1]),
		print(":\t"),
		print(item[0])
		
	
	# Do something to turn topics, and sentiments to desired format c
	# c = f(topics, sentiments)
	
	#### At this point we have data of the form: {'internet_source1': [{'topic1': [sentiment_array1], 'topic2': [sentiment_array2] ...}]}
	### Example: {'reddit': [{'presidential election': [0.232, 0.978, 0.315], 'puppies': [1.000, 0.999, 0.978] ... }]}
	
	# Data open for reduction
	
	# Visualize data

# Cool, we're done!
