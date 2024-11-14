import pandas as pd
import sys
from os.path import exists
from sentence_transformers import SentenceTransformer

def getTextEmbed(text):
    embedder = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    embedding = embedder.encode(text)
    return embedding

def update_descriptions(filename, df):
    # Iterate over the DataFrame rows where 'desc' is 'Too Big, please manually describe'
    for index, row in df[df['desc'] == 'Too Big, please manually describe'].iterrows():
        # Prompt the user to enter a new description
        new_desc = input(f'Please add a description for \"{row["name"]}\": ')
        
        # Update the 'desc' column with the new description
        df.at[index, 'desc'] = new_desc
        df.at[index, 'embed'] = getTextEmbed(new_desc)
    
    # Save the updated DataFrame to a new CSV file
    df.to_csv(filename, index=False)

def main():
    if len(sys.argv) != 2:
        print(f'Please use the format "python manual_describe.py [CSV TO EDIT]" and try again.')
    if not exists(sys.argv[1]):
        print(f'Error: {sys.argv[1]} is either inaccessible or does not exist.')

    input_csv = sys.argv[1]
    df = pd.read_csv(input_csv)

    # Run the update function
    update_descriptions(input_csv, df)

    print(f'Descriptions and text embeddings added to "{input_csv}".')

if __name__ == '__main__':
    main()