import pandas as pd
import streamlit as st
from model_utils import load_data, load_embeddings, analyze_sentiment, find_similar_stories

st.set_page_config(page_title="Breakup Story Analyzer", layout="wide")
st.title("💔 Breakup Story Analyzer")

# Load data
st.session_state.df = load_data()
st.session_state.embeddings = load_embeddings()

# User Input
user_input = st.text_area("✍️ Share your breakup story here", height=200)

if st.button("🔍 Analyze"):
    if user_input.strip() == "":
        st.warning("Please enter a story to analyze.")
    else:
        sentiment = analyze_sentiment(user_input)
        st.subheader(f"🧠 Sentiment: {sentiment}")

        st.subheader("📖 Most Similar Stories:")
        similar_df, scores = find_similar_stories(user_input, st.session_state.df, st.session_state.embeddings)

        for i, row in similar_df.iterrows():
            st.markdown(f"**Title**: {row['title']}")
            st.markdown(f"*Upvotes:* {row['upvotes']}, *Comments:* {row['comments_count']}")
            st.markdown(f"`Similarity Score:` {scores[list(similar_df.index).index(i)]:.2f}")
            st.markdown(row['body'][:500] + "...")
            st.markdown(f"💬 **Top Advice:** {row['top_comments'][:300] if pd.notna(row['top_comments']) else 'No advice available.'}")
            st.markdown("---")
