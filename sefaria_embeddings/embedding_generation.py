# /scripts/embedding_generation.py

import pandas as pd
from gensim.models import Word2Vec

if __name__ == "__main__":
    # Load the preprocessed texts from the CSV file
    df_texts = pd.read_csv('/Users/gideon/repos/Sefaria-Export/preprocessed_texts.csv')

    # Convert the tokens column to a list of lists
    sentences = df_texts['tokens'].apply(eval).tolist()

    # Train a Word2Vec model
    w2v_model = Word2Vec(sentences, vector_size=100, window=5, min_count=1, workers=4)

    # Save the Word2Vec model
    w2v_model.save('/Users/gideon/repos/Sefaria-Export/word2vec.model')

    # Display the vocabulary to verify
    print(w2v_model.wv.index_to_key)
