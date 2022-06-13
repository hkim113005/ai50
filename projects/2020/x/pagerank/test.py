from pagerank import *

corpus = {"1.html": {"2.html", "3.html"}, "2.html": {"3.html"}, "3.html": {}}
page = "3.html"
damping_factor = 0.85

print(sample_pagerank(corpus, damping_factor, 100000))