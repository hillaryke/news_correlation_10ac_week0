import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from src.utils import create_tags_df, plot_tag_counts

def load_data(file_path):
    news_data = pd.read_csv(file_path)
    return news_data

def create_headline_tag_chart(tags_df):
    fig, ax = plt.subplots()
    ax.bar(tags_df['Tag'], tags_df['Count'])
    ax.set_xlabel('Tag')
    ax.set_ylabel('Count')
    ax.set_title('Headline tag counts')
    st.pyplot(fig)



def main():
    st.title('News Headline tags analysis')

    tags_df = load_data('../data/findings/tags_count.csv')

    # Remove the "Other" tag for meaningful analysis
    tags_df = tags_df[tags_df['Tag'] != 'Other']

    # Select the top 10 tags
    tags_df = tags_df.head(10)

    # Plot the tag counts
    create_headline_tag_chart(tags_df)

if __name__ == '__main__':
    main()

