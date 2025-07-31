import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
nltk.download('vader_lexicon')

# Load model
embed_model = SentenceTransformer('all-MiniLM-L6-v2')
sentiment_model = SentimentIntensityAnalyzer()

def load_data(path='/Users/usufahmed/Desktop/REDDIT_APP/reddit_data.csv'):
    df = pd.read_csv(path)
    df['text'] = df['title'].fillna('') + '. ' + df['body'].fillna('')
    return df

def generate_embeddings(text_list):
    return embed_model.encode(text_list, show_progress_bar=True)

def save_embeddings(embeddings, path='embeddings/reddit_vectors.npy'):
    np.save(path, embeddings)

def load_embeddings(path='embeddings/reddit_vectors.npy'):
    return np.load(path)

def analyze_sentiment(text):
    score = sentiment_model.polarity_scores(text)['compound']
    if score > 0.2:
        return "Positive"
    elif score < -0.2:
        return "Negative"
    else:
        return "Neutral"

def find_similar_stories(user_input, df, embeddings, top_n=5):
    input_vec = embed_model.encode([user_input])
    similarities = cosine_similarity(input_vec, embeddings)[0]
    top_indices = similarities.argsort()[-top_n:][::-1]
    return df.iloc[top_indices], similarities[top_indices]
