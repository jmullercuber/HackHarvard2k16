#!/usr/bin/env python2
# Execute as ./main.py

import cognitive, json, os.path, operator
# Establish connections to internet sources
from RedditScraper import RedditScraper
from TwitterScraper import TwitterScraper


if __name__ == "__main__":
	# collect text data from them
	twitter = TwitterScraper();
	internet_documents = {'twitter': twitter.get_documents()}
	'''reddit = RedditScraper()
	internet_documents = {  'reddit-sports': reddit.get_documents("sports", 2),
							'reddit-baseball': reddit.get_documents("baseball", 2),
							'reddit-cubs': reddit.get_documents("CHICubs", 2),
							'reddit-dodgers': reddit.get_documents("dodgers", 2),
							'reddit-all': reddit.get_documents("all", 2)}'''

	# For every source analyze text data with the Microsoft Cognitive Services Text Analytics API
	sentiments = {}
	topics = {}
	
	# Load previously saved file if avaliable
	s_file_path = "./sentiments.data"
	if os.path.isfile(s_file_path):
		print("Importing sentiments...")
		s_file = open(s_file_path, 'r')
		sentiments = json.load(s_file)
		s_file.close()
	
	t_file_path = "./topics.data"
	if os.path.isfile(t_file_path):
		print("Importing topics...")
		t_file = open(t_file_path, 'r')
		topics = json.load(t_file)
		t_file.close()
	
	
	# Add any new sources in internet_documents if they have not been analyzed
	update_sentiments = update_topics = False
	for source, docs in internet_documents.items():
		
		if source not in sentiments:
			sentiments[source] = cognitive.documents_to_sentiments(docs)
			update_sentiments = True
	
		if source not in topics:
			topics[source] = cognitive.documents_to_topics(docs)
			update_topics = True
	
	if update_sentiments:
		s_file = open(s_file_path, 'w')
		s_file.write(json.dumps(sentiments))
		s_file.close()
	
	if update_topics:
		t_file = open(t_file_path, 'w')
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
			if len(topic_sents) == 0:
				# at later point, would be good to find source of these errors
				print "topic error: ", source, topic
			if len(topic_sents) > 0:
				c[source].append({t_key: topic_sents})
	
	
	# Do something to turn topics, and sentiments to desired format c
	# c = f(topics, sentiments)
	
	#### At this point we have data of the form: {'internet_source1': [{'topic1': [sentiment_array1], 'topic2': [sentiment_array2] ...}]}
	### Example: {'reddit': [{'presidential election': [(0.232, .5), (0.978, .25), (0.315, .01)], 'puppies': [(1.000, .2), (0.999, .7), (0.978, 1)] ... }]}
	
	# Data open for reduction
	
	# Visualize data

	from plot import *
	docs_per_sources_graph(c['twitter'])
	bar_graph(c['twitter'])
	#docs_per_sources_graph(c['reddit-baseball'], c['reddit-cubs'], c['reddit-sports'], c['reddit-dodgers'])
	#bar_graph(c['reddit-all'])

# Cool, we're done!
