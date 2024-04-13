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

# Create tags for the headlines
news_data['tags'] = categorize_headlines(news_data['title'], defined_tags)

# Create a DataFrame for the tags and their counts
tags_df = create_tags_df(news_data)

# Remove the "Other" tag for meaningful analysis
tags_df = tags_df[tags_df['Tag'] != 'Other']

# Select the top 10 tags
tags_df = tags_df.head(5)

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


# Websites with highest word count
# # Apply the function to the 'title_word_count' column
# news_data['word_count_category'] = news_data['title_word_count'].apply(categorize_word_count)
#
# # Create the pie chart
# create_pie_chart(news_data)