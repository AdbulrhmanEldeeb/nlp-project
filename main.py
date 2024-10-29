import wikipedia
from textblob import TextBlob
import nltk

# nltk.download('punkt_tab')
# print(wikipedia.search('Muhammad'))

article = wikipedia.summary("Muhammad Yunus")

blob = TextBlob(article)
# print(blob.sentiment)
# print(blob.polarity)
# print(blob.sentences[0])
# print(blob.noun_phrases)
import fire

def welcome(name="sayed"):
    """i am docstring"""
    return f"hello {name}"


# how to use
# python main.py --name=ali
# python main.py --help
if __name__ == "__main__":
    fire.Fire(welcome)
