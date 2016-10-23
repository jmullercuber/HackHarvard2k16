import matplotlib.pyplot as plt
import numpy as np

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
    