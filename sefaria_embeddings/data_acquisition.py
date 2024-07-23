# /scripts/data_acquisition.py

import os
import json
import sys

import pandas

# Define the paths to the JSON files
json_files = [
    '/Users/gideon/repos/Sefaria-Export/json/Tanakh/Torah/Numbers/Hebrew/Tanach with Nikkud.json',
    '/Users/gideon/repos/Sefaria-Export/json/Tanakh/Torah/Leviticus/Hebrew/Tanach with Nikkud.json',
    '/Users/gideon/repos/Sefaria-Export/json/Tanakh/Torah/Deuteronomy/Hebrew/Tanach with Nikkud.json',
    '/Users/gideon/repos/Sefaria-Export/json/Tanakh/Torah/Genesis/Hebrew/Tanach with Nikkud.json',
    '/Users/gideon/repos/Sefaria-Export/json/Tanakh/Torah/Exodus/Hebrew/Tanach with Nikkud.json'
]

# Function to load JSON files
def load_json_files(file_paths):
    data = []
    for file_path in file_paths:
        with open(file_path, 'r', encoding='utf-8') as file:
            json_data = json.load(file)
            data.append(json_data)
    return data

# Load the data

# Combine all texts into a single DataFrame for easier processing
def combine_texts(texts):
    combined_data = []
    for text in texts:
        for chapter in text['text']:
            for verse in chapter:
                combined_data.append(verse)
    return pandas.DataFrame(combined_data, columns=['verse'])

# Combine the texts into a DataFrame

# Display the first few rows of the combined DataFrame

# Save the combined DataFrame to a CSV file for future use
if __name__ == "__main__":
    args = sys.argv[1:]
    texts = load_json_files(json_files)
    df_texts = combine_texts(texts)
    print(df_texts.head())
    df_texts.to_csv('/Users/gideon/repos/Sefaria-Export/combined_texts.csv', index=False)

