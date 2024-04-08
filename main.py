from src.config import cfg  # Import the config file
from src.loader import DataLoader
from src.utils import largest_news_count_websites
from src.utils import largest_number_of_traffic_websites

data_path = cfg.news_data_path

loader = DataLoader()
traffic_data = loader.load_traffic_data()
news_data = loader.load_news_data()

top_N = 10

# Display the top 10 websites with the largest count of news articles
print("Top 10 websites with the largest number of news articles:")
# print(largest_news_count_websites(news_data, top_N))

# Display the top 10 websites with the largest number of visitors
print("Top 10 websites with the largest number of visitors:")
print(largest_number_of_traffic_websites(traffic_data, top_N))
