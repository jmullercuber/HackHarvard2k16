import cognitive, json
# Establish connections to internet sources
from RedditScraper import RedditScraper


if __name__ == "__main__":
    # collect text data from them
    reddit = RedditScraper()
    internet_documents = {  'reddit-politics': reddit.get_documents("politics", 1)  }
    	
    print(len(internet_documents['reddit-politics']))
    
    # For every source analyze text data with the Microsoft Cognitive Services Text Analytics API
    
    sentiments = {
        source: cognitive.documents_to_sentiments(docs)
        for source, docs in internet_documents.items()
    }
    
    s_file = open('sentiments.data', 'w')
    s_file.write(json.dumps(sentiments))
    
    topics = {
        source: cognitive.documents_to_topics(docs)
        for source, docs in internet_documents.items()
    }
    
    
    t_file = open('topics.data', 'w')
    t_file.write(json.dumps(topics))
    
    # Do something to turn topics, and sentiments to desired format c
    # c = f(topics, sentiments)
    
    #### At this point we have data of the form: {'internet_source1': [{'topic1': [sentiment_array1], 'topic2': [sentiment_array2] ...}]}
    ### Example: {'reddit': [{'presidential election': [0.232, 0.978, 0.315], 'puppies': [1.000, 0.999, 0.978] ... }]}
    
    # Data open for reduction
    
    # Visualize data

# Cool, we're done!
