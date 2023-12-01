from nltk.tokenize import word_tokenize
from readDocument import read_word_document

# Function to calculate TP, TN, FN, precision, recall, and accuracy
def calculate_metrics(corrected_text, reference_text):
    corrected_tokens = set(word_tokenize(corrected_text))
    reference_tokens = set(word_tokenize(reference_text))

    # Correctly identified and replaced misspelled words.
    tp = len(corrected_tokens & reference_tokens)
    # Incorrectly identified and replaced by another words.
    fp = len(corrected_tokens - reference_tokens)
    # Misspelled words that were not identified and corrected.
    fn = len(reference_tokens - corrected_tokens)

    precision = tp / (tp + fp) if (tp + fp) > 0 else 0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0
    accuracy = (tp) / (tp + fp + fn) if (tp + fp + fn) > 0 else 0

    return precision, recall, accuracy

# Example ground truth Word document path (replace with the actual path to your ground truth document)
reference_document_path = 'sample5-correct.docx'

# Read the ground truth Word document
reference_text = read_word_document(reference_document_path)

# Example corrected Word document path (replace with the actual path to your corrected document)
corrected_document_path = 'sample5-output.docx'
#corrected_document_path = 'sample5-errors.docx'


# Read the corrected Word document
corrected_text = read_word_document(corrected_document_path)

# Calculate precision, recall, and accuracy
precision, recall, accuracy = calculate_metrics(corrected_text, reference_text)

# Print the results
print("Precision:", round(precision, 3))
print("Recall:", round(recall, 3))
print("Accuracy:", round(accuracy, 3))
