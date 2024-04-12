import matplotlib.pyplot as plt

def load_data():
    news_data = pd.read_csv('data.csv')
    return news_data

def create_chart(news_data):
    news_data['date'] = pd.to_datetime(news_data['date'])
    news_data.set_index('date', inplace=True)
    news_data['count'].plot()
    plt.title('News count over time')
    plt.xlabel('Date')
    plt.ylabel('Count')
    st.pyplot()
