import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

st.title("CORD-19 Data Explorer")
st.write("Simple exploration of COVID-19 research papers")

# Load cleaned data
df = pd.read_csv('metadata_clean.csv')

# Interactive year selection
year_range = st.slider(
    "Select publication year range",
    int(df['year'].min()),
    int(df['year'].max()),
    (2020, 2021)
)

# Filter dataframe by selected years
df_filtered = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]

# Show filtered data
st.subheader("Sample of filtered papers")
st.dataframe(df_filtered.head(10))

# Plot number of publications by year
st.subheader("Number of Publications by Year")
year_counts = df_filtered['year'].value_counts().sort_index()
st.bar_chart(year_counts)

# Word cloud of titles
st.subheader("Word Cloud of Paper Titles")
text = ' '.join(df_filtered['title'].dropna())
wordcloud = WordCloud(width=800, height=400, stopwords=STOPWORDS).generate(text)
st.image(wordcloud.to_array(), use_column_width=True)