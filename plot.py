import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
	
def easy_graph2(ts):
	
	# Label your graphs!
	plt.title('Topic')
	plt.xlim(-1, 1)
	plt.xlabel("Sentiment")
	plt.ylim(0,1)
	plt.ylabel("Relevance")
	
	colors = cm.rainbow(np.linspace(0, 1, len(ts)))
	
	for t, c in zip(ts, colors):
		# Extract topic string and ploints from t parameter
		topic = t.keys()[0]
		points = t[topic]
		if len(points) < 0:
			continue		
	
		# Transpose points from coordinate list
		x, y = zip(*points)
		# And translate
		x = (np.array(x) - 0.5)*2
	
		plt.scatter(x, y, color=c)
	
	# Present your graph
	plt.show()
	
	return x,y,plt

def topic_graph(t):
	# Extract topic string and ploints from t parameter
	topic = t.keys()[0]
	points = t[topic]
	
	# Transpose points from coordinate list
	x, y = zip(*points)
	# And translate
	x = (np.array(x) - 0.5)*2
	
	# Label your graphs!
	plt.title('Topic: "' + topic + '"')
	plt.xlim(-1, 1)
	plt.xlabel("Sentiment")
	plt.ylim(0,1)
	plt.ylabel("Relevance")
	plt.plot(x, y)
	
	# Present your graph
	plt.show()
	
	return x,y,plt

def bar_graph(ts):
	ts = sorted(ts, key=lambda t: np.median(extract_topic(t)[1]))[::-1]
	for t in ts:
		print(t)
	indexes = np.arange(len(ts))
	topics = [extract_topic(t)[0] for t in ts]
	sentiments = [np.median(extract_topic(t)[1]) for t in ts]
	
	plt.bar(indexes, sentiments)
	
	# Label your graphs!
	plt.title("Average Sentiment across Topics")
	plt.xlabel("Topic")
	plt.ylim(0, 1)
	plt.ylabel("Average Sentiment")
	plt.xticks(indexes, topics, rotation='vertical')
	
	# Present your graph
	plt.show()
	
	return plt, ts

def extract_topic(t):
	topic = t.keys()[0]
	x, y = zip(*(t[topic]))
	return topic, x, y