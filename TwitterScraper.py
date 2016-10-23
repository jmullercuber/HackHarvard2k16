from Scraper import Scraper
from TwitterTest import *

class TwitterScraper( Scraper ):
    def get_documents(self):
        # returns ~1000 documents,
        # 100 tweets from top 10 hashtags
        
        # setup, get trending tags
        b = getBearer(key, secret)
        trends = [t for t,n in getTrending(b, WOEID)]
        results = []
        
        # Go through the trending hashtags
        for tags in trends:
            # Get 100 tweets matching
            r = getResults(b, tags)
            # If getResults didn't fail
            if len(r) > 0:
                # for every returned tweet
                for tweet in r['statuses']:
                    # Add it
                    results += [ tweet['text'] ]
                    if len(results) >= 1000:
                        return results
        
        return results

if __name__ == "__main__":
    t = TwitterScraper()
    t.get_documents()