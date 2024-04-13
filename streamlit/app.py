import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt


def load_data(file_path):
    news_data = pd.read_csv(file_path)
    return news_data

##################################
# Page configuration
st.set_page_config(
    page_title="News analysis and correlation",
    page_icon=":newspaper:",
    layout="wide",
    initial_sidebar_state="expanded",
)

def create_headline_tag_chart(tags_df):
    plt.figure(figsize=(6, 4))  # Increase the size of your plot
    ax = plt.gca()
    ax.bar(tags_df['Tag'], tags_df['Count'])
    ax.set_xlabel('Tag')
    ax.set_ylabel('Count')
    ax.set_title('Headline tag counts')
    plt.xticks(rotation=25)  # Rotate the x-axis labels
    st.pyplot(plt.gcf())  # Use plt.gcf() to get the current figure


# plot a pie chart of the common countries with articles written about them
def create_countries_most_common_pie_chart_from_csv(file_path):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)

    fig, ax = plt.subplots()

    st.title('Countries with most articles written about them')

    # Create the pie chart
    df.set_index('Country')['Count'].plot.pie(autopct='%1.1f%%')
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

    # plot a graph of countries with articles written about them
    create_countries_most_common_pie_chart_from_csv('../data/findings/countries_most_common.csv')


if __name__ == '__main__':
    main()
