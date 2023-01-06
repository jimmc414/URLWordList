import requests
import nltk
import re

def read_page(url):
    if not re.match(r'^https?://', url):
        url = 'http://' + url
    response = requests.get(url)
    html = response.text
    return html

def read_all_pages(url):
    html = read_page(url)
    words = extract_words(html)
    return words

def extract_words(html):
    # Get English stopwords from nltk
    stopwords = set(nltk.corpus.stopwords.words())

    # Get list of words from the HTML
    words = nltk.tokenize.word_tokenize(html)

    # Convert words to lowercase and remove stopwords
    words = [word.lower() for word in words if word.isalpha() and word.lower() not in stopwords]

    return words

def count_words(words):
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts

def main():
    url = input("Enter the URL of the website: ")
    words = read_all_pages(url)
    word_counts = count_words(words)
    with open("wordcounts.csv", "w", encoding="utf-8") as f:
        for word, count in word_counts.items():
            f.write(f'{word},{count}\n')

if __name__ == '__main__':
    main()
