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

from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer


data_path = cfg.news_data_path

data_loader = DataLoader()
traffic_data = data_loader.load_traffic_data()
news_data = data_loader.load_news_data()
domain_info = data_loader.load_domain_info()

# Apply the function to the source_name column to create the source_id column
news_data['source_id'] = news_data['source_name'].apply(preprocess_source_id)

top_N = 10

# Display the top 10 websites with the largest count of news articles
print("Top 10 websites with the largest number of news articles:")
# print(largest_news_count_websites(news_data, top_N))

# Display the top 10 websites with the largest number of visitors
print("Top 10 websites with the largest number of visitors:")
# print(largest_number_of_traffic_websites(traffic_data, top_N))

# Display the top 10 countries with the highest number of news media organizations
print("Top 10 countries with the highest number of news media organizations:")
# print(get_countries_with_most_media_organizations(domain_info, top_N))

# Display the top 10 countries with the highest number of articles written about them
print("Top 10 countries with the highest number of articles written about them:")
# print(get_countries_with_articles_written_about_them(news_data, top_N))

# # Define the regions
# regions = {
#     'Africa': AFRICA,
#     'EU': EU,
#     'Middle East': MIDDLE_EAST,
#     'US': ['United States'],
#     'China': ['China'],
#     'Russia': ['Russia'],
#     'Ukraine': ['Ukraine']
# }
#
# # Get the websites that reported about the specified regions
# region_counts = get_websites_reporting_on_regions(news_data, regions)

# Print the results
# for region, counts in region_counts.items():
#     print(f"Websites that reported about {region}:")
#     print(counts.most_common(10))
#     print()

# Calculate sentiment statistics
# sentiment_stats = sentiment_statistics(news_data)
#
# # Display the sentiment statistics
# print("Sentiment Statistics:")
# print(sentiment_stats)

# Extract keywords using custom TF-IDF
custom_tfidf_keywords = extract_keywords_custom_tfidf(news_data)

print("Custom TF-IDF keywords:")
for i, keywords in enumerate(custom_tfidf_keywords):
    print(f"Keywords of article {i+1}: {keywords}")

# COMPARE SIMILARITY BETWEEN KEYWORDS IN TITLE AND CONTENT

# Extract keywords using custom TF-IDF for both title and content
news_data['title_keywords'] = extract_keywords_custom_tfidf(news_data['title'])
news_data['content_keywords'] = extract_keywords_custom_tfidf(news_data['content'])

# Calculate the similarity between the keywords in the title and the content
vectorizer = TfidfVectorizer()
title_tfidf = vectorizer.fit_transform([' '.join(keywords) for keywords in news_data['title_keywords']])
content_tfidf = vectorizer.transform([' '.join(keywords) for keywords in news_data['content_keywords']])
similarity_scores = cosine_similarity(title_tfidf, content_tfidf)

# Print the similarity scores
for i, score in enumerate(similarity_scores):
    print(f"Similarity between keywords in the title and content of article {i+1}: {score[0]}")
