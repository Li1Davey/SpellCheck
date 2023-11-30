'''
Program by Cristian Pedroza & David Sanchez

'''
import string
from nltk.tokenize import word_tokenize
from nltk.metrics import edit_distance

# Function to identify misspelled words using the loaded 1-gram file
def find_misspelled_words(document_text, valid_words):
    words = word_tokenize(document_text)
    misspelled = [word for word in words if word.lower() not in valid_words and word.isalpha()]
    return set(misspelled)

# Function to replace misspelled words with the closest match from valid words and 2-gram probabilities
def replace_misspelled_words(document_text, misspelled_words, valid_words, valid_2grams):
    words = word_tokenize(document_text)
    corrected_text = []
    for i, word in enumerate(words):
        if word.lower() in misspelled_words:
            # Find the closest match using edit distance
            closest_match = min(valid_words.keys(), key=lambda x: edit_distance(word.lower(), x))
            
            # Use a simple bigram model to improve replacement based on context and frequencies
            if i > 0:
                prev_word = words[i - 1].lower()
                bigram = (prev_word, closest_match)
                if bigram in valid_2grams:
                    freq_bigram = valid_2grams[bigram]
                    freq_closest_match = valid_words[closest_match]
                    if freq_bigram > freq_closest_match:
                        corrected_text.append(closest_match)
                    else:
                        corrected_text.append(bigram[1])
                else:
                    corrected_text.append(closest_match)
            else:
                corrected_text.append(closest_match)

            # Print misspelled words
            #print(f"Misspelled word: {word}, Corrected word: {closest_match}")
        else:
            corrected_text.append(word)

    # Combine words and punctuation correctly
    combined_text = []
    for word in corrected_text:
        # If the word is a punctuation mark, combine it with the preceding word
        if word in string.punctuation:
            if combined_text and combined_text[-1] not in string.punctuation:
                combined_text[-1] += word
            else:
                combined_text.append(word)
        else:
            combined_text.append(word)

    return ' '.join(combined_text)
