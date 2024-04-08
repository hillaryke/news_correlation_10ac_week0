from src.config import cfg  # Import the config file
from src.loader import DataLoader
from src.utils import largest_news_count_websites
from src.utils import largest_number_of_traffic_websites
from src.utils import get_countries_with_most_media_organizations
from src.utils import get_countries_with_articles_written_about_them

data_path = cfg.news_data_path

loader = DataLoader()
traffic_data = loader.load_traffic_data()
news_data = loader.load_news_data()
domain_info = loader.load_domain_info()

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
print(get_countries_with_articles_written_about_them(news_data, top_N))