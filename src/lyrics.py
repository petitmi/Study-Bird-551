import pandas as pd
import lyricsgenius
import pandas as pd
from collections import Counter
import nltk
from nltk.corpus import stopwords
from textblob import TextBlob

#open raw data file
df=pd.read_csv('../data/raw/billboard_hot_100_2012to2022_with_lyrics.csv', encoding='ISO-8859-1')

#preprocess the lyrics
stop_words = stopwords.words('english')

#remove stop words
def preprocess_text(text):
    text = text.lower()  # convert to lowercase
    words = nltk.word_tokenize(text)  # tokenize words
    words = [word for word in words if word.isalpha() and word not in stop_words]  # remove stop words and non-alphabetic characters
    return ' '.join(words)
  
#remove the word starts with translations
def remove_translations(text):
    words = text.split()
    filtered_words = [word for word in words if not word.startswith('translations')]
    return ' '.join(filtered_words)

#remove the word starts with lyrics  
def remove_lyrics(text):
    words = text.split()
    filtered_words = [word for word in words if not word.startswith('lyrics')]
    return ' '.join(filtered_words)
  
#function for count words  
def count_words(string):
    return len(string.split())
  
#create a new column for clean lyrics
df['Clean Lyrics'] = df['Lyrics'].apply(preprocess_text)
df['Clean Lyrics'] = df['Clean Lyrics'].apply(remove_translations)
df['Clean Lyrics'] = df['Clean Lyrics'].apply(remove_lyrics)
df['Clean Lyrics'] = df['Clean Lyrics'].str.replace(r'[^a-zA-Z0-9\s]', '',regex=True)

#create a new column for word count of lyrics
df['Word Count'] = df['Clean Lyrics'].apply(count_words)

#use package TextBlob to analyze sentiment of lyrics, score range from -1 to 1 (inclusive)
#If the socre is negative, then the sentiment of lyrics is negative
#If the socre is positive, then the sentiment of lyrics is positive
#If the socre is 0, then the sentiment of lyrics is neutral
sentiment_scores = []
for index, row in df.iterrows():
    lyrics = row['Clean Lyrics']
    blob = TextBlob(lyrics)
    sentiment_scores.append(blob.sentiment.polarity)

#create a new column for sentiment score of lyrics  
df['Sentiment Polarity'] = sentiment_scores

#create a new column for positive or negative or neutral of lyrics  
df['Sentiment'] = df['Sentiment Polarity'].apply(lambda x: 'Negative' if x < 0 else 'Positive' if x > 0 else 'Neutral')

#create a new column for frequency of love in lyrics  
df['Frequency_love'] = df['Lyrics'].str.count('love')

#save file to data/processed file
df.to_excel(r'../data/processed/lyrics_dataset.xlsx', index=False)
