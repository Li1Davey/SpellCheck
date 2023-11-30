'''
Program by Cristian Pedroza & David Sanchez
'''
# Function to load the 1-gram file and create a dictionary of valid words with frequencies
def load_1gram(file_path, num_words=50000):
    valid_words = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        for i, line in enumerate(file):
            parts = line.strip().split('\t')
            word, frequency = parts[1], int(parts[0])  # Use index 1 for the word and index 0 for frequency
            if word.isalpha():
                valid_words[word.lower()] = frequency
            if i >= num_words:
                break
    return valid_words

# Function to load the 2-gram file and create a dictionary of valid 2-grams with frequencies
def load_2gram(file_path, num_ngrams=10000000):
    valid_2grams = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        for i, line in enumerate(file):
            parts = line.strip().split('\t')
            ngram, frequency = tuple(parts[-2:]), int(parts[0])  # Use index -2 for the 2-gram and index 0 for frequency
            valid_2grams[ngram] = frequency
            if i >= num_ngrams:
                break
    return valid_2grams
