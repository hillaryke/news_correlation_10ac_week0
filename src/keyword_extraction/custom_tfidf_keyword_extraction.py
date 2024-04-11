from sklearn.feature_extraction.text import CountVectorizer
from numpy import array, log
import pandas as pd

def extract_keywords_custom_tfidf(text_data, max_features=10):
    # Use the 'article' column as the text data
    array_text = text_data.dropna().tolist()

    vectorizer = CountVectorizer()
    # Fit the vectorizer on the text data
    tf = vectorizer.fit_transform([x.lower() for x in array_text])
    tf = tf.toarray()
    tf = log(tf + 1)

    # Compute IDF values
    df = pd.DataFrame(tf, columns=vectorizer.get_feature_names_out())
    # calculates the Inverse Document Frequency (IDF) for each word in the text data.
    idf = (len(array_text) / (df > 0).sum()).apply(log)

    # We are ready to multiply the TF and IDF values to get the TF-IDF values.
    tfidf = tf.copy()
    words = array(vectorizer.get_feature_names_out())

    for word in words:
        tfidf[:, words == word] = tfidf[:, words == word] * idf[words]

    keywords = []
    for j in range(tfidf.shape[0]):
        # Get the top 5 words with the highest TF-IDF values
        top_words = [words[i] for i in tfidf[j].argsort()[-5:][::-1]]
        keywords.append(top_words)

    return keywords
