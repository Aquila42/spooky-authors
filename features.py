from nltk import word_tokenize

#get ngrams per author - maybe most common words?
def get_unigrams(df):
    texts = df['text'].apply(lambda row: row.strip().decode("ascii", "ignore").encode("ascii").lower())
    unigrams = set()
    for text in texts.values:
        for word in word_tokenize(text):
            if word not in unigrams:
                unigrams.add(word)
    return unigrams

# n-grams
# punctuation
