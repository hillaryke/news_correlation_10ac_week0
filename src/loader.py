import pandas as pd
import os
import argparse

# Create wrapper classes for using news_sdk
class NewsDataLoader:
    '''
    News exported data IO class.


    '''
    def __init__(self, data_path, domains_path, traffic_path):
        '''
        path: path to the news exported data folder
        '''
        self.data_path = data_path_path
        self.domains_path = domains_path
        self.traffic_path = traffic_path

        self.data_path = self.get_data_path()
        self.domains_data = self.get_domains_data()
        self.traffic_data = self.get_traffic_data()

    def load_new_data(self):
        """Loads news articles from data.csv"""
        news_df = pd.read_csv(os.path.join(self.data_path, "data/data.csv"))
        return news_df

    def load_domain_info(self):
        """Loads info about news source domains"""
        domains_df = pd.read_csv(os.path.join(self.domains_path, "domains_location.csv"))
        return domains_df

    def load_traffic_data(self):
        """Loads website traffic data"""
        traffic_df = pd.read_csv(os.path.join(self.traffic_path, "traffic_data.csv"))
        return traffic_df

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Export News data')

    parser.add_argument('--zip', help="Name of a zip file to import")
    args = parser.parse_args()