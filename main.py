from src.config import cfg  # Import the config file
from src.loader import DataLoader
from src.utils import largest_news_count_websites
from src.utils import largest_number_of_traffic_websites
from src.utils import get_countries_with_most_media_organizations
from src.utils import get_countries_with_articles_written_about_them
from src.utils import get_websites_reporting_on_regions

from src.regions import AFRICA, EU, MIDDLE_EAST


data_path = cfg.news_data_path

data_loader = DataLoader()
traffic_data = data_loader.load_traffic_data()
news_data = data_loader.load_news_data()
domain_info = data_loader.load_domain_info()

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

# Define the regions
regions = {
    'Africa': AFRICA,
    'EU': EU,
    'Middle East': MIDDLE_EAST,
    'US': ['United States'],
    'China': ['China'],
    'Russia': ['Russia'],
    'Ukraine': ['Ukraine']
}

# Get the websites that reported about the specified regions
region_counts = get_websites_reporting_on_regions(news_data, regions)

# Print the results
for region, counts in region_counts.items():
    print(f"Websites that reported about {region}:")
    print(counts.most_common(10))
    print()