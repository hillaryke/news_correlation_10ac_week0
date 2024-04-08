import json
import argparse
import os



# Create wrapper classes for using news_sdk
class NewsDataLoader:
    '''
    News exported data IO class.


    '''
    def __init__(self, path, domains_path, traffic_path):
        '''
        path: path to the news exported data folder
        '''
        self.path = path
        self.domains_path = domains_path