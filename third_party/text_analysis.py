from pathlib import Path

from textblob import TextBlob


path = Path("src/text.txt")

with open(path) as f:
    text = f.read()

blob = TextBlob(text)

for sentence in blob.sentences:
    print(sentence.sentiment.polarity)
