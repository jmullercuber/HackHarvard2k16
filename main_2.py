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
	
	
	
	c = {}
	
	for source in topics:
		c[source] = []
		topic_objs = topics[source]['result']['operationProcessingResult']['topics']
		topic_asgn = topics[source]['result']['operationProcessingResult']['topicAssignments']
		source_sents = sentiments[source]['result']['documents']
		for i in range(len(topic_objs)):
			topic = topic_objs[i]
			t_id = topic['id']
			t_key = topic['keyPhrase']
			topic_sents = []
			for j in range(len(topic_asgn)):
				if topic_asgn[j]['topicId'] == t_id:
					d_id = topic_asgn[j]['documentId']
					for k in range(len(source_sents)):
						if source_sents[k]['id'] == d_id:
							topic_sents.append((source_sents[k]['score'], topic_asgn[j]['distance']))
			c[source].append({t_key: topic_sents})
	
	
	# Do something to turn topics, and sentiments to desired format c
	# c = f(topics, sentiments)
	
	#### At this point we have data of the form: {'internet_source1': [{'topic1': [sentiment_array1], 'topic2': [sentiment_array2] ...}]}
	### Example: {'reddit': [{'presidential election': [(0.232, .5), (0.978, .25), (0.315, .01)], 'puppies': [(1.000, .2), (0.999, .7), (0.978, 1)] ... }]}
	from plot import easy_graph
	#tg = topic_graph(c['reddit-politics'][0])
	bg = bar_graph(c['reddit-politics'])
	
	
	# Data open for reduction
	
	# Visualize data

# Cool, we're done!
