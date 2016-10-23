import cognitive, json, os.path, operator
# Establish connections to internet sources
from RedditScraper import RedditScraper


if __name__ == "__main__":
	# collect text data from them
	reddit = RedditScraper()
	internet_documents = {  'reddit-sports': reddit.get_documents("sports", 2),
							'reddit-baseball': reddit.get_documents("baseball", 2),
							'reddit-cubs': reddit.get_documents("CHICubs", 2),
							'reddit-dodgers': reddit.get_documents("dodgers", 2),
							'reddit-all': reddit.get_documents("all", 2)}

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
		t_file = open('topics.data', 'w')
		t_file.write(json.dumps(topics))
		t_file.close()
	
	
	
	c = {}
	
	for source in topics:
		c[source] = []
		topic_objs = topics[source]['result']['operationProcessingResult']['topics']
		topic_asgn = topics[source]['result']['operationProcessingResult']['topicAssignments']
		if "dodgers" in source:
			print("\n"*10)
			print(source)
			print(sentiments[source])
		source_sents = sentiments[source]['result']['documents']
		for topic in topic_objs:
			t_id = topic['id']
			t_key = topic['keyPhrase']
			topic_sents = []
			for j in topic_asgn:
				if j['topicId'] == t_id:
					for k in source_sents:
						if k['id'] == j['documentId']:
							topic_sents.append((k['score'], j['distance']))
			if len(topic_sents) >= 0:
				c[source].append({t_key: topic_sents})
	
	
	# Do something to turn topics, and sentiments to desired format c
	# c = f(topics, sentiments)
	
	#### At this point we have data of the form: {'internet_source1': [{'topic1': [sentiment_array1], 'topic2': [sentiment_array2] ...}]}
	### Example: {'reddit': [{'presidential election': [(0.232, .5), (0.978, .25), (0.315, .01)], 'puppies': [(1.000, .2), (0.999, .7), (0.978, 1)] ... }]}
	
	# Data open for reduction
	
	# Visualize data

	from plot import *
	bg = easy_graph2(c['reddit-sports'])
	g = easy_graph2(c['reddit-baseball'])
	bg = easy_graph2(c['reddit-cubs'])
	g = easy_graph2(c['reddit-dodgers'])
	bg = easy_graph2(c['reddit-all'])

# Cool, we're done!
