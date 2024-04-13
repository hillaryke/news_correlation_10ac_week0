import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import altair as alt
import plotly.express as px

alt.themes.enable("dark")

##################################
# Page configuration
st.set_page_config(
    page_title="News analysis and correlation",
    page_icon=":newspaper:",
    layout="wide",
    initial_sidebar_state="expanded",
)


#######################
# CSS styling
st.markdown("""
<style>

[data-testid="block-container"] {
    padding-left: 2rem;
    padding-right: 2rem;
    padding-top: 1rem;
    padding-bottom: 0rem;
    margin-bottom: -7rem;
}

[data-testid="stVerticalBlock"] {
    padding-left: 0rem;
    padding-right: 0rem;
}

[data-testid="stMetric"] {
    background-color: #393939;
    text-align: center;
    padding: 15px 0;
}

[data-testid="stMetricLabel"] {
  display: flex;
  justify-content: center;
  align-items: center;
}

[data-testid="stMetricDeltaIcon-Up"] {
    position: relative;
    left: 38%;
    -webkit-transform: translateX(-50%);
    -ms-transform: translateX(-50%);
    transform: translateX(-50%);
}

[data-testid="stMetricDeltaIcon-Down"] {
    position: relative;
    left: 38%;
    -webkit-transform: translateX(-50%);
    -ms-transform: translateX(-50%);
    transform: translateX(-50%);
}

</style>
""", unsafe_allow_html=True)

#######################
# Load data
df_reshaped = pd.read_csv('../data/findings/tags_count.csv')

#######################
# Sidebar
with st.sidebar:
    st.title(':newspaper: News analysis Dashboard')


    color_theme_list = ['blues', 'cividis', 'greens', 'inferno', 'magma', 'plasma', 'reds', 'rainbow', 'turbo',
                        'viridis']
    selected_color_theme = st.selectbox('Select a color theme', color_theme_list)


#######################

def load_data(file_path):
    news_data = pd.read_csv(file_path)
    return news_data


alt.themes.enable("dark")

def create_headline_tag_chart(tags_df):
    plt.figure(figsize=(6, 4))  # Increase the size of your plot
    ax = plt.gca()
    ax.bar(tags_df['Tag'], tags_df['Count'])
    ax.set_xlabel('Tag')
    ax.set_ylabel('Count')
    ax.set_title('Headline tag counts')
    plt.xticks(rotation=25)  # Rotate the x-axis labels
    st.pyplot(plt.gcf())  # Use plt.gcf() to get the current figure


# plot a pie chart of the common countries with articles written about them
def create_countries_most_common_pie_chart_from_csv(file_path):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)

    st.title('Countries with most articles written about them')\



    # Create the pie chart
    pie_chart = alt.Chart(df).transform_window(
        startAngle='sum(Count)',
        endAngle='sum(Count)',
        sort=[alt.SortField('Count')],
        frame=[None, 0]
    ).mark_arc().encode(
        alt.Theta('Count:Q', stack=True, sort=alt.SortField('order'), title=None),
        alt.Color('Country:N', legend=alt.Legend(title='Countries')),
        alt.Tooltip(['Country:N', 'Count:Q'])
    ).properties(
        width=400,
        height=400
    )

    st.altair_chart(pie_chart)

def create_choropleth_map(file_path):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)

    choropleth = px.choropleth(df, locations='Country', color='Count',
                               locationmode="country names",
                               color_continuous_scale='blues',
                               range_color=(0, max(df['Count'])),
                               labels={'Count':'Number of Articles'}
                              )
    choropleth.update_layout(
        template='plotly_dark',
        plot_bgcolor='rgba(0, 0, 0, 0)',
        paper_bgcolor='rgba(0, 0, 0, 0)',
        margin=dict(l=0, r=0, t=0, b=0),
        height=450
    )

    return choropleth

def create_global_rank_report_scatter_graph(file_path):
    final_data = pd.read_csv(file_path)

    final_data_top_10000 = final_data[final_data['GlobalRank'] <= 10000]

    # Create a scatter plot
    scatter = alt.Chart(final_data_top_10000).mark_circle(size=60).encode(
        x='total_reports:Q',
        y='GlobalRank:Q',
        color=alt.Color('title_sentiment:Q', scale=alt.Scale(scheme='blueorange')),
        tooltip=['Domain:N', 'total_reports:Q', 'GlobalRank:Q', 'title_sentiment:Q']
    ).properties(
        width=900,
        height=700,
        title='Impact of Frequent News Reporting and Sentiment on Website\'s Global Ranking'
    )

    return scatter

def main():
    st.title('News Headline tags analysis')
    choropleth = create_choropleth_map('../data/findings/countries_in_articles.csv')

    st.plotly_chart(choropleth)


    # Global rank report scatter graph
    global_rank_report_graph = create_global_rank_report_scatter_graph('../data/findings/global_rank_sentiment_report.csv')

    # Display the global rank report scatter graph
    st.altair_chart(global_rank_report_graph)

    # tags_df = load_data('../data/findings/tags_count.csv')
    #
    # # Remove the "Other" tag for meaningful analysis
    # tags_df = tags_df[tags_df['Tag'] != 'Other']
    #
    # # Select the top 10 tags
    # tags_df = tags_df.head(10)
    #
    # # Create columns
    # col1, col2, col3 = st.columns((1.5, 4.5, 2), gap='medium')
    #
    # # Plot the tag counts in the first column
    # with col1:
    #     create_headline_tag_chart(tags_df)
    #
    # # plot a graph of countries with articles written about them in the second column
    # with col2:
    #     create_countries_most_common_pie_chart_from_csv('../data/findings/countries_most_common.csv')
    #
    # # Create a progress chart in the third column
    # with col3:
    #     st.title('Headline tags')
    #     for index, row in tags_df.iterrows():
    #         st.text(f"Tag: {row['Tag']}")
    #         st.progress(row['Count'] / tags_df['Count'].max())
    #         st.text(f"Count: {row['Count']}")


#######################
# Dashboard Main Panel
col = st.columns((1.5, 4.5, 2), gap='medium')




if __name__ == '__main__':
    main()
