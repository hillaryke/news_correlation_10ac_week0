from __future__ import print_function
import argparse

news_data_path = 'data/'
domains_path = 'data/'
traffic_path = 'data/'

parser = argparse.ArgumentParser(description='cmdArgs')
parser.add_argument('--output', type=str, default='news_analysis.csv',
                help='filename to write analysis output in CSV format')
parser.add_argument('--news_data_path', required=False, type=str,
                    help='directory to where main news dataset reside')


cfg = parser.parse_args()
# print(cfg)