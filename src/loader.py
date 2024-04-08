import pandas as pd
import os

# Create wrapper classes for using news_sdk
class NewsDataLoader:
    '''
    News exported data IO class.


    '''
    def __init__(self, news_data_path, domains_path, traffic_path):
        '''
        path: path to the news exported data folder
        '''
        self.news_data = news_data_path
        self.domains_path = domains_path
        self.traffic_path = traffic_path

        self.news_data = self.get_news_data()
        self.domains_data = self.get_domains_data()
        self.traffic_data = self.get_traffic_data()

    def load_news_data(self):
        """Loads news articles from data.csv"""
        news_df = pd.read_csv(os.path.join(self.news_data, "data.csv"))
        return news_df

    def load_domain_info(self):
        """Loads info about news source domains"""
        domains_df = pd.read_csv(os.path.join(self.domains_path, "domains_location.csv"))
        return domains_df

    def load_traffic_data(self):
        """Loads website traffic data"""
        traffic_df = pd.read_csv(os.path.join(self.traffic_path, "traffic_data.csv"))
        return traffic_df
