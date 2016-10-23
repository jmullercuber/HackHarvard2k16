import matplotlib.pyplot as plt
import numpy as np

def easy_graph(t):
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
	
def easy_graph2(ts):
	
	# Label your graphs!
	plt.title('Topic"')
	plt.xlim(-1, 1)
	plt.xlabel("Sentiment")
	plt.ylim(0,1)
	plt.ylabel("Relevance")
	
	for i in range(len(ts)):
		# Extract topic string and ploints from t parameter
		t = ts[i]
		topic = t.keys()[0]
		points = t[topic]
		if len(points) < 0:
			continue		
	
		# Transpose points from coordinate list
		x, y = zip(*points)
		# And translate
		x = (np.array(x) - 0.5)*2
	
		plt.plot(x, y)
	
	# Present your graph
	plt.show()
	
	return x,y,plt