

import pandas as pd

df = pd.read_csv('IMDB Dataset.csv')
df.head()

import re

def clean_text(text):
    text = text.lower()
    text = re.sub(r'<.*?>', '', text)  # remove HTML
    text = re.sub(r'[^a-zA-Z\s]', '', text)  # remove punctuation
    text = re.sub(r'\s+', ' ', text).strip()
    return text

df['review'] = df['review'].apply(clean_text)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    df['review'], df['sentiment'], test_size=0.2, random_state=42
)

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

vectorizer = TfidfVectorizer(max_features=5000)
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

model = LogisticRegression()
model.fit(X_train_vec, y_train)

y_pred = model.predict(X_test_vec)
print("Accuracy:", accuracy_score(y_test, y_pred))

from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Word Cloud
pos_text = ' '.join(df[df['sentiment'] == 'positive']['review'])
neg_text = ' '.join(df[df['sentiment'] == 'negative']['review'])

wc = WordCloud(width=800, height=400).generate(pos_text)
plt.figure(figsize=(10,5))
plt.imshow(wc, interpolation='bilinear')
plt.title("Positive Reviews Word Cloud")
plt.axis('off')
plt.show()

wc = WordCloud(width=800, height=400).generate(neg_text)
plt.figure(figsize=(10,5))
plt.imshow(wc, interpolation='bilinear')
plt.title("Negative Reviews Word Cloud")
plt.axis('off')
plt.show()

# Pie chart
df['sentiment'].value_counts().plot.pie(autopct='%1.1f%%', colors=['green', 'red'])
plt.title("Sentiment Distribution")
plt.ylabel("")
plt.show()


import joblib

joblib.dump(model, 'sentiment_model.pkl')
joblib.dump(vectorizer, 'vectorizer.pkl')


