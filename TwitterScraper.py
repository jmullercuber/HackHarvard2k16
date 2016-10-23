from Scraper import Scraper
from TwitterTest import *

class TwitterScraper( Scraper ):
    def __init__(self, v=False):
        self.verbose = v
    
    def get_documents(self):
        if self.verbose:
            print "starting TwitterScraper"
        # returns ~1000 documents,
        # 100 tweets from top 10 hashtags
        
        # setup, get trending tags
        b = getBearer(key, secret)
        trends = getTrending(b, WOEID)
        results = []
        
        # Go through the trending hashtags
        for tag, query, n in trends:
            if self.verbose:
                print "....collecting tweets for trend:", tag
            # Get 100 tweets matching
            r = getResults(b, query)
            # If getResults didn't fail
            if len(r) > 0:
                # for every returned tweet
                for tweet in r['statuses']:
                    # Add it
                    results += [ tweet['text'] ]
                    if len(results) >= 1000:
                        return results
        
        if self.verbose:
            print "finished TwitterScraper"
        return results

if __name__ == "__main__":
    t = TwitterScraper()
    t.get_documents()