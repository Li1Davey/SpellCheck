
import re

def is_valid_ngram(ngram):
    # Define a regular expression to match valid n-grams
    ngram_pattern = re.compile(r'^[a-zA-Z\-,.?!;:"\'\s]+$')  # Allow spaces as well

    # Check if the entire n-gram matches the pattern and does not have consecutive punctuation marks
    ngram_str = ''.join(ngram)
    
    return (
        ngram_pattern.match(ngram_str) is not None
        and ' ' not in ngram_str
        and sum(1 for char in ngram_str if char.isupper()) <= 2
        and sum(1 for char in ngram_str if char in '-,.?!;:"\'') <= 2
        and all(char.isalpha() or char in '-,.' for char in ngram_str)
    )

def filter_ngram_file(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as infile, open(output_path, 'w', encoding='utf-8') as outfile:
        for line in infile:
            frequency, *ngram = line.strip().split('\t')
            
            # Convert frequency to an integer
            frequency = int(frequency)
            
            # Skip lines with frequency less than 2
            if frequency < 5:
                continue
            
            # Check if the n-gram is valid
            if is_valid_ngram(ngram):
                # Write the line to the output file
                outfile.write(line)

                
# Usage:
input_ngram_path = 'wp_2gram.txt'
output_ngram_path = 'new_wp_2gram.txt'

filter_ngram_file(input_ngram_path, output_ngram_path)
print("Done")
