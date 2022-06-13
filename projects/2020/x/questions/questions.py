import nltk
import sys
import os
import string
import math

FILE_MATCHES = 1
SENTENCE_MATCHES = 1


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python questions.py corpus")

    # Calculate IDF values across files
    files = load_files(sys.argv[1])
    file_words = {
        filename: tokenize(files[filename])
        for filename in files
    }
    file_idfs = compute_idfs(file_words)

    # Prompt user for query
    query = set(tokenize(input("Query: ")))

    # Determine top file matches according to TF-IDF
    filenames = top_files(query, file_words, file_idfs, n=FILE_MATCHES)

    # Extract sentences from top files
    sentences = dict()
    for filename in filenames:
        for passage in files[filename].split("\n"):
            for sentence in nltk.sent_tokenize(passage):
                tokens = tokenize(sentence)
                if tokens:
                    sentences[sentence] = tokens

    # Compute IDF values across sentences
    idfs = compute_idfs(sentences)

    # Determine top sentence matches
    matches = top_sentences(query, sentences, idfs, n=SENTENCE_MATCHES)
    for match in matches:
        print(match)


def load_files(directory):
    """
    Given a directory name, return a dictionary mapping the filename of each
    `.txt` file inside that directory to the file's contents as a string.
    """
    files = {}
    for file in os.listdir(directory):
        if file.endswith(".txt"):
            with open(os.path.join(directory, file), encoding="utf-8") as f:
                files[file] = f.read()

    return files


def tokenize(document):
    """
    Given a document (represented as a string), return a list of all of the
    words in that document, in order.

    Process document by coverting all words to lowercase, and removing any
    punctuation or English stopwords.
    """
    words = []
    for word in nltk.tokenize.word_tokenize(document):
        word = word.lower()
        if word in string.punctuation or word in nltk.corpus.stopwords.words("english"):
            continue
        words.append(word)

    return words


def compute_idfs(documents):
    """
    Given a dictionary of `documents` that maps names of documents to a list
    of words, return a dictionary that maps words to their IDF values.

    Any word that appears in at least one of the documents should be in the
    resulting dictionary.
    """
    all_words = []
    for words in documents.values():
        all_words += words
    all_words = list(set(all_words))

    idfs = {}
    for word in all_words:
        contains = 0
        for words in documents.values():
            if word in words:
                contains += 1
        idfs[word] = math.log(len(documents) / contains)

    return idfs


def top_files(query, files, idfs, n):
    """
    Given a `query` (a set of words), `files` (a dictionary mapping names of
    files to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the filenames of the the `n` top
    files that match the query, ranked according to tf-idf.
    """
    file_ranks = []
    for filename, words in files.items():
        file_tfidf = 0
        for word in query:
            tf = words.count(word)
            file_tfidf += tf * idfs[word]
        file_ranks.append((file_tfidf, filename))

    file_ranks.sort(key=lambda file_rank: file_rank[0], reverse=True)
    return [file_rank[1] for file_rank in file_ranks[:n]]


def top_sentences(query, sentences, idfs, n):
    """
    Given a `query` (a set of words), `sentences` (a dictionary mapping
    sentences to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the `n` top sentences that match
    the query, ranked according to idf. If there are ties, preference should
    be given to sentences that have a higher query term density.
    """
    sentence_ranks = []
    for sentence, words in sentences.items():
        contains = 0
        idf = 0
        for word in query:
            contains += words.count(word)
            if word in words:
                idf += idfs[word]
        sentence_ranks.append((idf, contains / len(words), sentence))

    sentence_ranks.sort(key=lambda sentence_rank: (sentence_rank[0], sentence_rank[1]), reverse=True)
    return [sentence_rank[2] for sentence_rank in sentence_ranks[:n]]

if __name__ == "__main__":
    main()
