import json, httplib, urllib, string, base64, ast

key = 'kFxjNI3AlMiWGCVVIdg2mwLVf'
secret = 'VbvyqLW2B0LB3BNCVZfJaSD7djvAbYuQgBvWnoz7oycoINqKoF'
WOEID = 23424977

def getBearer(key, secret):
    # Ideally should url encode the key and secret,
    # but it will work ok without for now

    credentials = base64.b64encode(key + ':' + secret)
    headers = {'Authorization': 'Basic ' + credentials, 'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'}
    conn = httplib.HTTPSConnection('api.twitter.com')
    conn.request('POST', '/oauth2/token', 'grant_type=client_credentials', headers)
    response = conn.getresponse()
    bearer = ast.literal_eval(response.read())['access_token']
    return bearer

#Gets the most recent tweets for a hashtag
def getResults(bearer, hashtag):
    url = '/1.1/search/tweets.json?q=%23' + hashtag
    headers = {'Authorization': 'Bearer ' + bearer}
    conn = httplib.HTTPSConnection('api.twitter.com')
    conn.request('GET', url, '', headers)
    response = conn.getresponse().read()
    return response

#Returns a list of the top 10 trending topics and their tweet counts
def getTrending(bearer, woeid):
    url = '/1.1/trends/place.json?id=' + str(woeid)
    headers = {'Authorization': 'Bearer ' + bearer}
    conn = httplib.HTTPSConnection('api.twitter.com')
    conn.request('GET', url, '', headers)
    response = conn.getresponse().read()
    tweet_data = json.loads(response)
    
    trends = [
        (tag['name'], tag['tweet_volume'])
        for tag in tweet_data[0]['trends']
    ]

    return trends

if __name__ == "__main__":
    #test
    print getTrending(getBearer(key, secret), WOEID)