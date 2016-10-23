import cognitive, json, os.path
# Establish connections to internet sources
from RedditScraper import RedditScraper


if __name__ == "__main__":
	# collect text data from them
	reddit = RedditScraper()
	internet_documents = {  'reddit-politics': reddit.get_documents("politics", 3)}
			
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
	
	# Do something to turn topics, and sentiments to desired format c
	# c = f(topics, sentiments)
	
	#### At this point we have data of the form: {'internet_source1': [{'topic1': [sentiment_array1], 'topic2': [sentiment_array2] ...}]}
	### Example: {'reddit': [{'presidential election': [0.232, 0.978, 0.315], 'puppies': [1.000, 0.999, 0.978] ... }]}
	
	# Data open for reduction
	
	# Visualize data

# Cool, we're done!
