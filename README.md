
### 💔 Breakup Story Analyzer

A sentiment-aware NLP-powered app that helps users process their breakup experiences by analyzing emotional tone, finding similar Reddit stories, and surfacing the most relevant advice from real people.

Built with `Streamlit`, `SentenceTransformers`, and a dataset from Reddit’s r/BreakUps subreddit.

---

## 🚀 Features

- ✍️ **User Input**: Share a breakup story through the web interface
- 🧠 **Sentiment Analysis**: Understand the emotional tone (Positive, Neutral, Negative)
- 🔍 **Story Matching**: Find similar breakup posts from real Reddit users
- 💬 **Advice Generator**: Get distilled advice from top comments of similar posts

---

## 📂 Project Structure

```

breakup-story-analyzer/
├── app.py                   # Main Streamlit app
├── model\_utils.py           # Core logic: embedding, sentiment, similarity
├── generate\_embeddings.py   # One-time embedding generator
├── data/
│   └── reddit\_data.csv      # Cleaned Reddit dataset
├── embeddings/
│   └── reddit\_vectors.npy   # Precomputed sentence embeddings
├── requirements.txt         # Project dependencies

```

---

## 🧠 How It Works

1. **Text Embedding**: Stories are converted into vector form using `all-MiniLM-L6-v2`
2. **Sentiment Scoring**: VADER determines story emotion
3. **Similarity Matching**: Cosine similarity finds top 5 most similar stories
4. **Advice Extraction**: `top_comments` from matching posts are shown

---

## 🖥️ Running the App

### 🔧 Installation
```bash
git clone https://github.com/yourusername/breakup-story-analyzer.git
cd breakup-story-analyzer
pip install -r requirements.txt
````

### ⚙️ Generate Embeddings (Run Once)

```bash
python generate_embeddings.py
```

### ▶️ Launch the App

```bash
streamlit run app.py
```

---

## 🧪 Example Input

> "We were together for three years. Things slowly fell apart as we stopped communicating. Last week, she said she needed space and left. I feel empty and confused."

**Predicted Sentiment**: Negative
**Top Advice**: "Focus on healing. It’s okay to not have closure. Give it time."

---

## 📊 Dataset

* Source: Reddit [r/BreakUps](https://www.reddit.com/r/BreakUps/)
* Columns: `title`, `body`, `top_comments`, `upvotes`, `comments_count`, etc.
* Rows: 948 posts

---

## 🛠️ Built With

* [Streamlit](https://streamlit.io/) – UI
* [SentenceTransformers](https://www.sbert.net/) – Embedding model
* [scikit-learn](https://scikit-learn.org/) – Similarity matching
* [NLTK (VADER)](https://github.com/cjhutto/vaderSentiment) – Sentiment detection

---

## 📌 Future Enhancements

* Advice summarization using `T5` or `BART`
* Keyword search or filters (e.g., relationship length)
* User story logging for feedback or journaling
* Deployment (Streamlit Cloud or Render)

---

## 🤝 Contributing

PRs are welcome! If you have ideas or feedback, feel free to open an issue.

---

## 📄 License

MIT License. Use for learning, research, or emotional support apps 💙

## 🙋‍♂️ Author
Mohammed Yousuf
AI Engineering Student | Passionate about Machine Learning, Computer Vision, and Real-World Applications 🚀
Feel free to reach out or contribute!

## 🌟 Star this repository
If you found this helpful, give it a ⭐ on GitHub!
