import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer

# Load dataset
df = pd.read_csv("/Users/usufahmed/Desktop/REDDIT_APP/reddit_data.csv")
df['text'] = df['title'].fillna('') + '. ' + df['body'].fillna('')

# Load model and encode
model = SentenceTransformer('all-MiniLM-L6-v2')
embeddings = model.encode(df['text'].tolist(), show_progress_bar=True)

# Save embeddings
np.save("/Users/usufahmed/Desktop/REDDIT_APP/embeddings/reddit_vectors.npy", embeddings)
print("Embeddings saved to embeddings/reddit_vectors.npy")
