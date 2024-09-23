from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
words = ["running", "runner", "easily", "fairly", "cats", "happily"]
stemmed_words = [stemmer.stem(word) for word in words]
print("Stemmed words:")
for word in stemmed_words:
    print(word)