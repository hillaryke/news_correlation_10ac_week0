def largest_news_count_websites(news_data, top_N):
    """Get the top N websites with the largest number of news articles"""

    # Use the value_counts() function to count the number of articles from each source
    article_counts = news_data['source_name'].value_counts()

    # Sort the counts in descending order
    article_counts = article_counts.sort_values(ascending=False)

    # Return the top N website sources
    return article_counts.head(top_N)

def largest_number_of_traffic_websites(traffic_data, top_N):
    """Get the top N websites with the largest number of visitors traffic"""

    # Sor the DataFrame by 'RefIPs' in descending order
    sorted_traffic_data = traffic_data.sort_values(by='RefIPs', ascending=False)

    # Return the top N website sources
    return sorted_traffic_data[['Domain', 'RefIPs']].head(top_N)

def get_countries_with_most_media_organizations(domain_info, top_N):
    """Get the top N countries with the highest number of news media organizations"""

    # Use the `value_counts()` function on the 'location' column
    country_counts = domain_info['location'].value_counts()

    # Return the top N countries
    return country_counts.head(top_N)