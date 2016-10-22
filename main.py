import cognitive
# Establish connections to internet sources
from RedditScraper import RedditScraper

# collect text data from them
reddit = RedditScraper()
internet_documents = {  'reddit': reddit.get_documents()  }

# For every source Analyze text data with the Microsoft Cognitive Services Text Analytics API
# a = cognitive.documents_to_topics(stuff)
# b = cognitive.documents_to_sentiments(same stuff)

# Do something to turn a, and b to desired format c
# c = f(a, b)

#### At this point we have data of the form: {'internet_source1': [{'topic1': [sentiment_array1], 'topic2': [sentiment_array2] ...}]}
### Example: {'reddit': [{'presidential election': [0.232, 0.978, 0.315], 'puppies': [1.000, 0.999, 0.978] ... }]}

# Data open for reduction

# Visualize data

# Cool, we're done!