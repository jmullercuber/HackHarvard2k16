from Scraper import Scraper
import json, httplib, string

class RedditScraper( Scraper ):
	depth = 0

	def get_documents(self, subreddit, qty):
		#Connect to reddit for json requests
		conn = httplib.HTTPSConnection('www.reddit.com')

		
		#Get the hot posts in r/worldnews
		conn.request("GET", "/r/" + subreddit + "/hot/.json")
		response = conn.getresponse()
		subreddit_data = response.read()
		subreddit_data = json.loads(subreddit_data) # Convert from json to dict
		
		documents = []
		for i in range(1, qty):
			documents.extend(self.get_comments_for_post(subreddit_data['data']['children'][i]['data']['permalink']))
		
		conn.close()
		return documents
		
		
	def get_comments_for_post(self, link):
		#Connect to reddit for json requests
		conn = httplib.HTTPSConnection('www.reddit.com')
		
		#Get the comments page for the linked posts
		conn.request("GET", link + '/.json?limit=500')
		response = conn.getresponse()
		post_data = response.read()
		post_data = json.loads(post_data) # Convert from json to dict
		tl_comments = post_data[1]['data']['children'] # The top level posts
		
		all_comments = []
		for comment in tl_comments:
			if 'body' in comment['data']:
				self.depth = 0
				all_comments.extend(self.recurse_comments(comment))	
	
		return all_comments
				
	def recurse_comments(self, comment):
		comment_bodies = []
		body = filter(lambda x : x in string.printable, comment['data']['body'])
		comment_bodies.append(body)
		if not comment['data']['replies'] == '' and self.depth < 1:
			for reply in comment['data']['replies']['data']['children']:
				if not reply['kind'] == 'more':
					self.depth += 1
					comment_bodies.extend(self.recurse_comments(reply))
		return comment_bodies