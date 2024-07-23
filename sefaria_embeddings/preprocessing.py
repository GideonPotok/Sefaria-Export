# /scripts/preprocessing.py
import sys

import pandas as pd
import re
import nltk
from nltk.tokenize import word_tokenize



# Function to clean and tokenize text
def preprocess_text(text):
    # Remove non-Hebrew characters
    text = re.sub(r'[^\u0590-\u05FF\s]', '', text)
    # Tokenize the text
    tokens = word_tokenize(text)
    return tokens

if __name__ == "__main__":
    args = sys.argv[1:]
    # Download the required NLTK resources
    nltk.download('punkt')

    # Load the combined texts from the CSV file
    df_texts = pd.read_csv('/Users/gideon/repos/Sefaria-Export/combined_texts.csv')
    # Apply preprocessing to the DataFrame
    df_texts['tokens'] = df_texts['verse'].apply(preprocess_text)

    # Display the first few rows of the DataFrame to verify preprocessing
    print(df_texts.head())

    # Save the preprocessed DataFrame to a CSV file for future use
    df_texts.to_csv('/Users/gideon/repos/Sefaria-Export/preprocessed_texts.csv', index=False)
