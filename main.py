import pandas as pd
from src.config import cfg  # Import the config file
from src.loader import DataLoader
from src.regions import AFRICA, EU, MIDDLE_EAST
from src.utils import largest_news_count_websites, preprocess_source_id
from src.utils import largest_number_of_traffic_websites
from src.utils import get_countries_with_most_media_organizations
from src.utils import get_countries_with_articles_written_about_them
from src.utils import get_websites_reporting_on_regions
from src.utils import sentiment_statistics
from src.keyword_extraction.custom_tfidf_keyword_extraction import extract_keywords_custom_tfidf
from src.utils import categorize_headlines
from src.utils import clean_text, create_tags_df, save_df_to_csv
from src.defined_tags import defined_tags
from src.utils import plot_tag_counts
from src.utils import categorize_word_count, create_pie_chart

from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

from database.db_manager import save_to_db
from database.db_manager import save_to_csv
import matplotlib.pyplot as plt
from src.utils import create_countries_most_common_pie_chart_from_csv
from src.source_domain_mapping import source_domain_mapping
from src.utils import calculate_sentiment
import altair as alt

data_path = cfg.news_data_path

data_loader = DataLoader()

traffic_data = data_loader.load_traffic_data()
news_data = data_loader.load_news_data()
domain_info = data_loader.load_domain_info()
top_N = 10

# Get the top 5 websites with the largest number of news articles
top_news_websites = largest_news_count_websites(news_data, 5)
print(top_news_websites)

# Preprocess the text
news_data['title'] = news_data['title'].apply(clean_text)

# Add a new column 'url' to the DataFrame
news_data['url'] = news_data['source_name'].map(source_domain_mapping)


# Step 1: Calculate total number of reports by each website
total_reports = news_data['source_name'].value_counts().reset_index()
total_reports.columns = ['source_name', 'total_reports']

# Step 2: Add a new column 'url' to the DataFrame
total_reports['url'] = total_reports['source_name'].map(source_domain_mapping)

# Drop the irrelevant columns in the traffic data
domain_global_rank = traffic_data.drop(['TldRank', 'TLD', 'IDN_Domain', 'PrevGlobalRank','RefSubNets', 'IDN_TLD', 'RefIPs', 'PrevTldRank', 'PrevRefSubNets', 'PrevRefIPs'], axis=1)

# Merge total_reports with traffic_data on 'url'
merged_data = pd.merge(total_reports, domain_global_rank, left_on='url', right_on='Domain')


# Apply function to calculate sentiment
news_data['title_sentiment'] = news_data['title'].apply(calculate_sentiment)

# Group by source_name and calculate mean sentiment
title_sentiment_stats = news_data.groupby('source_name')['title_sentiment'].mean().reset_index()

# Merge merged_data with title_sentiment_stats on 'source_name'
global_rank_sentiment_report = pd.merge(merged_data, title_sentiment_stats, on='source_name')


# Merge total_reports with traffic_data on 'url'
merged_data = pd.merge(total_reports, traffic_data, left_on='url', right_on='Domain')


# save the title sentiment statistics to a CSV file
save_to_csv(title_sentiment_stats, 'data/findings/title_sentiment_stats.csv')


# save the final data to a CSV file
save_to_csv(global_rank_sentiment_report, 'data/findings/global_rank_sentiment_report.csv')


# Impact of Frequent News Reporting and Sentiment on Website's Global Ranking
# Filter the DataFrame
global_rank_sentiment_report_top_10000 = global_rank_sentiment_report[global_rank_sentiment_report['GlobalRank'] <= 10000]

# Example display Scatter plot graph
scatter = alt.Chart(global_rank_sentiment_report_top_10000).mark_circle(size=60).encode(
    x='total_reports:Q',
    y='GlobalRank:Q',
    color=alt.Color('title_sentiment:Q', scale=alt.Scale(scheme='blueorange')),
    tooltip=['Domain:N', 'total_reports:Q', 'GlobalRank:Q', 'title_sentiment:Q']
).properties(
    width=600,
    height=400,
    title='Impact of Frequent News Reporting and Sentiment on Website\'s Global Ranking'
)

scatter.display()


# Create tags for the headlines
news_data['tags'] = categorize_headlines(news_data['title'], defined_tags)

# Create a DataFrame for the tags and their counts
tags_df = create_tags_df(news_data)

# Remove the "Other" tag for meaningful analysis
tags_df = tags_df[tags_df['Tag'] != 'Other']

# Plot the tag counts
plot_tag_counts(tags_df)

# Save the DataFrame to a CSV file
save_df_to_csv(tags_df, 'data/findings/tags_count.csv')


countries_written_about = get_countries_with_articles_written_about_them(news_data, top_N)
df_countries_most_common = pd.DataFrame(countries_written_about, columns=['Country', 'Count'])
save_df_to_csv(df_countries_most_common, 'data/findings/countries_most_common.csv')
print(countries_written_about)

# plot a graph of countries with articles written about them
create_countries_most_common_pie_chart_from_csv('data/findings/countries_most_common.csv')


countries_in_articles = get_countries_with_articles_written_about_them(news_data, 100)
df_countries_in_articles = pd.DataFrame(countries_in_articles, columns=['Country', 'Count'])
save_df_to_csv(df_countries_in_articles, 'data/findings/countries_in_articles.csv')