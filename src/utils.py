import spacy
from collections import Counter
from textblob import TextBlob
import pandas as pd
import re

# Function to preprocess source_name into source_id
def preprocess_source_id(source_name):
    # Convert to lowercase
    source_id = source_name.lower()
    # Replace spaces with hyphens
    source_id = source_id.replace(" ", "-")
    # Remove special characters
    source_id = re.sub(r'\W+', '', source_id)
    return source_id

def largest_news_count_websites(news_data, top_N):
    """Get the top N websites with the largest number of news articles"""

    # Use the value_counts() function to count the number of articles from each source
    article_counts = news_data['source_name'].value_counts()

    # Sort the counts in descending order
    article_counts = article_counts.sort_values(ascending=False)

    # Return the top N website sources
    return article_counts.head(top_N)


def largest_number_of_traffic_websites(traffic_data, top_N):
    """Get the top N websites with the largest number of visitors traffic"""

    # Sor the DataFrame by 'RefIPs' in descending order
    sorted_traffic_data = traffic_data.sort_values(by='RefIPs', ascending=False)

    # Return the top N website sources
    return sorted_traffic_data[['Domain', 'RefIPs']].head(top_N)


def get_countries_with_most_media_organizations(domain_info, top_N):
    """Get the top N countries with the highest number of news media organizations"""

    # Use the `value_counts()` function on the 'location' column
    country_counts = domain_info['location'].value_counts()

    # Return the top N countries
    return country_counts.head(top_N)


def get_countries_with_articles_written_about_them(news_data, top_N):
    """Get the top N countries with the highest number of articles written about them"""

    # Load the SpaCy model
    nlp = spacy.load("en_core_web_sm")

    # Concatenating all the news articles into a single string
    all_articles = " ".join(news_data['content'].dropna())

    # Using SpaCy to process the text
    doc = nlp(all_articles)

    # Extracting the countries mentioned in the articles
    countries = [ent.text for ent in doc.ents if ent.label_ == "GPE"]

    # Counting the number of times each country is mentioned
    country_counts = Counter(countries)

    # Return the top N countries
    return country_counts.most_common(top_N)

def get_websites_reporting_on_regions(news_data, regions):
    """Get the websites that reported about specific regions"""

    # Load the SpaCy model
    nlp = spacy.load("en_core_web_sm")

    # Initialize a dictionary to store the results
    region_counts = {region: Counter() for region in regions}

    # Process each article
    for _, row in news_data.iterrows():
        doc = nlp(row['content'])

        # Extract country names
        countries = [ent.text for ent in doc.ents if ent.label_ == 'GPE']

        # Check if the country belongs to one of the regions
        for country in countries:
            for region, region_countries in regions.items():
                if country in region_countries:
                    region_counts[region][row['source_name']] += 1

    return region_counts

def calculate_sentiment(text):
    """Calculate sentiment score using TextBlob"""
    return TextBlob(text).sentiment.polarity

def sentiment_statistics(news_data):
    """Calculate sentiment statistics for each website"""
    # Calculate sentiment scores
    news_data['sentiment'] = news_data['content'].apply(calculate_sentiment)

    # Create columns for positive, neutral, and negative sentiment counts
    news_data['positive_sentiment'] = (news_data['sentiment'] > 0).astype(int)
    news_data['neutral_sentiment'] = (news_data['sentiment'] == 0).astype(int)
    news_data['negative_sentiment'] = (news_data['sentiment'] < 0).astype(int)

    # Group by 'source_name' and calculate mean, median, variance, and sentiment counts
    grouped = news_data.groupby('source_name')
    mean_sentiment = grouped['sentiment'].mean()
    median_sentiment = grouped['sentiment'].median()
    variance_sentiment = grouped['sentiment'].var()
    positive_sentiment = grouped['positive_sentiment'].sum()
    neutral_sentiment = grouped['neutral_sentiment'].sum()
    negative_sentiment = grouped['negative_sentiment'].sum()

    # Return the results as a DataFrame
    return pd.DataFrame({
        'mean_sentiment': mean_sentiment,
        'median_sentiment': median_sentiment,
        'variance_sentiment': variance_sentiment,
        'positive_sentiment': positive_sentiment,
        'neutral_sentiment': neutral_sentiment,
        'negative_sentiment': negative_sentiment
    })
