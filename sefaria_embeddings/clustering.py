# /scripts/clustering.py
import json
import sys

import json
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
import pandas as pd
from gensim.models import Word2Vec
from sklearn.cluster import KMeans
import numpy as np

if __name__ == "__main__":
    args = sys.argv[1:]
    # Load the Word2Vec model
    w2v_model = Word2Vec.load('/Users/gideon/repos/Sefaria-Export/word2vec.model')

    # Get the word vectors
    word_vectors = w2v_model.wv.vectors

    # Apply K-means clustering
    num_clusters = 10  # You can adjust the number of clusters
    kmeans = KMeans(n_clusters=num_clusters, random_state=42)
    kmeans.fit(word_vectors)

    # Assign clusters to words
    words = w2v_model.wv.index_to_key
    word_clusters = {word: cluster for word, cluster in zip(words, kmeans.labels_)}
    print(word_clusters)
    # Save the clustering results
    # with open('/Users/gideon/repos/Sefaria-Export/word_clusters.json', 'w', encoding='utf-8') as f:
    #     json.dump(word_clusters, f, ensure_ascii=False, indent=4)
    # Get the word vectors and corresponding clusters
    words = list(word_clusters.keys())
    vectors = np.array([w2v_model.wv[word] for word in words])
    clusters = [word_clusters[word] for word in words]

    # Reduce dimensions using PCA for visualization
    pca = PCA(n_components=2)
    reduced_vectors = pca.fit_transform(vectors)

    # Create a DataFrame for visualization
    df = pd.DataFrame({
        'word': words,
        'x': reduced_vectors[:, 0],
        'y': reduced_vectors[:, 1],
        'cluster': clusters
    })

    # Plot the clusters
    plt.figure(figsize=(12, 8))
    sns.scatterplot(x='x', y='y', hue='cluster', data=df, palette='tab10')
    for i, word in enumerate(df['word']):
        plt.text(df.iloc[i]['x'] + 0.02, df.iloc[i]['y'], word, fontsize=9)
    plt.title('Word Clusters Visualization')
    plt.xlabel('PCA Component 1')
    plt.ylabel('PCA Component 2')
    plt.legend(title='Cluster')
    plt.show()

    # Interpretation:
    # After visualizing the clusters, you can interpret the clusters by looking at the words in each cluster and understanding the contextual similarities captured by the embeddings.
    # You can also further analyze specific clusters to see if they align with expected groupings based on the documentary hypothesis or other criteria.

    # Display the cluster assignments to verify

