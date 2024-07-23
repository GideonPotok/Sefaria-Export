# /scripts/analysis_visualization.py

import pandas as pd
import json
from gensim.models import Word2Vec
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA

# Load the Word2Vec model and cluster assignments
w2v_model = Word2Vec.load('/Users/gideon/repos/Sefaria-Export/word2vec.model')

with open('/Users/gideon/repos/Sefaria-Export/word_clusters.json', 'r', encoding='utf-8') as f:
    word_clusters = json.load(f)
