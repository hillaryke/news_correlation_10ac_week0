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

from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

from database.db_manager import save_to_db
from database.db_manager import save_to_csv

data_path = cfg.news_data_path

data_loader = DataLoader()

traffic_data = data_loader.load_traffic_data()
news_data = data_loader.load_news_data()
domain_info = data_loader.load_domain_info()




# Save to csv file
# save_to_csv(news_data, 'data/findings/news_data.csv')



top_N = 10

# Perform the analyses and store the results in a dictionary
# findings = {
#     'Top 10 websites with the largest number of news articles': largest_news_count_websites(news_data, top_N),
#     'Top 10 websites with the largest number of visitors': largest_number_of_traffic_websites(traffic_data, top_N),
#     'Top 10 countries with the highest number of news media organizations': get_countries_with_most_media_organizations(domain_info, top_N),
#     'Top 10 countries with the highest number of articles written about them': get_countries_with_articles_written_about_them(news_data, top_N),
#     'Websites that reported about Africa': get_websites_reporting_on_regions(news_data, {'Africa': AFRICA}),
#     'Websites that reported about EU': get_websites_reporting_on_regions(news_data, {'EU': EU}),
#     'Websites that reported about Middle East': get_websites_reporting_on_regions(news_data, {'Middle East': MIDDLE_EAST}),
#     'Websites that reported about US': get_websites_reporting_on_regions(news_data, {'US': ['United States']}),
#     'Websites that reported about China': get_websites_reporting_on_regions(news_data, {'China': ['China']}),
#     'Websites that reported about Russia': get_websites_reporting_on_regions(news_data, {'Russia': ['Russia']}),
#     'Websites that reported about Ukraine': get_websites_reporting_on_regions(news_data, {'Ukraine': ['Ukraine']}),
#     'Sentiment Statistics': sentiment_statistics(news_data),
#     'Custom TF-IDF keywords': extract_keywords_custom_tfidf(news_data)
# }


# Convert the dictionary to a DataFrame
# df_findings = pd.DataFrame(findings)

# Save the DataFrame to a CSV file
# save_to_csv(df_findings, 'data/findings/task1_EDA.csv')



# Preprocess the text
news_data['title'] = news_data['title'].apply(clean_text)

# Create tags for the headlines
news_data['tags'] = categorize_headlines(news_data['title'], defined_tags)

# Create a DataFrame for the tags and their counts
tags_df = create_tags_df(news_data)

# Plot the tag counts
plot_tag_counts(tags_df)

# Save the DataFrame to a CSV file
save_df_to_csv(tags_df, 'data/findings/tags_count.csv')


# # COMPARE SIMILARITY BETWEEN KEYWORDS IN TITLE AND CONTENT
#
# # Extract keywords using custom TF-IDF for both title and content
# news_data['title_keywords'] = extract_keywords_custom_tfidf(news_data['title'])
# news_data['content_keywords'] = extract_keywords_custom_tfidf(news_data['content'])
#
# # Calculate the similarity between the keywords in the title and the content
# vectorizer = TfidfVectorizer()
# title_tfidf = vectorizer.fit_transform([' '.join(keywords) for keywords in news_data['title_keywords']])
# content_tfidf = vectorizer.transform([' '.join(keywords) for keywords in news_data['content_keywords']])
# similarity_scores = cosine_similarity(title_tfidf, content_tfidf)
#
# # Print the similarity scores
# for i, score in enumerate(similarity_scores):
#     print(f"Similarity between keywords in the title and content of article {i+1}: {score[0]}")
