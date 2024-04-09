import pandas as pd
import os
import argparse
from src import config

# Create wrapper classes for using news_sdk
class DataLoader:
    '''
    News exported data IO class.
    '''

    def __init__(self):
        pass

    def load_news_data(self):
        """Loads news articles from data.csv"""
        news_df = pd.read_csv(os.path.join(config.news_data_path, "data.csv"))
        return news_df
#
    def load_domain_info(self):
        """Loads info about news source domains"""
        domains_df = pd.read_csv(os.path.join(config.domains_path, "domains_location.csv"))
        return domains_df

    def load_traffic_data(self):
        """Loads website traffic data"""
        traffic_df = pd.read_csv(os.path.join(config.traffic_path, "traffic.csv"))
        return traffic_df

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Export News data')

    parser.add_argument('--zip', help="Name of a zip file to import")
    args = parser.parse_args()
