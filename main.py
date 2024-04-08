from src.config import cfg  # Import the config file
from src.loader import NewsDataLoader
from src.utils import largest_news_count_websites

data_path = cfg.news_data_path

loader = NewsDataLoader()
news_data = loader.load_news_data()

# Display the top 10 websites with the largest count of news articles
top_N = 10
print(largest_news_count_websites(news_data, top_N))
