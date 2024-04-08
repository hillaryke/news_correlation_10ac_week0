from src.config import cfg  # Import the config file
from src.loader import NewsDataLoader

data_path = cfg.news_data_path

loader = NewsDataLoader()
news_data = loader.load_news_data()

print(news_data.head())
