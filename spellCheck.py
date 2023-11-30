from extractData import*
from correctError import*
from readDocument import*

# Extract files
one_gram_file_path = 'wp_1gram.txt'
two_gram_file_path = 'new_wp_2gram.txt'
word_document_path = 'sample5-errors.docx'
output_path = 'sample5-output.docx'


# Load the 1-gram file to obtain valid words with frequencies
valid_words = load_1gram(one_gram_file_path)

# Load the 2-gram file to obtain valid 2-grams with frequencies
valid_2grams = load_2gram(two_gram_file_path)

# Read the Word document
text_from_document = read_word_document(word_document_path)

# Find misspelled words in the document using the 1-gram file as the source of valid words
misspelled_words = find_misspelled_words(text_from_document, valid_words)

# Replace misspelled words with the closest match from valid words and 2-gram probabilities
corrected_text = replace_misspelled_words(text_from_document, misspelled_words, valid_words, valid_2grams)

# Write the corrected text to a new Word document
write_corrected_text_to_docx(corrected_text, output_path)
