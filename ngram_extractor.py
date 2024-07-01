# Made By Dineth Hettiarachchi
# INFO6145 Data Science and Machine Learning Project

# Import Modules
import os
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

nltk.download('wordnet')
nltk.download('punkt')

def read_file(file_path):
    """
    Reads the input text file and returns the content as a string.
    """
    with open(file_path, 'r') as file:
        text = file.read()
    return text

def tokenize_sentences(text):
    """
    Tokenizes the input text into sentences.
    """
    sentences = sent_tokenize(text)
    return sentences

def tokenize_words(sentence):
    """
    Tokenizes a sentence into words.
    """
    words = word_tokenize(sentence)
    return words

def generate_ngrams(words, n):
    """
    Generates n-grams from the list of words.
    """
    ngrams = ['_'.join(words[i:i+n]).lower() for i in range(len(words)-n+1)]
    return ngrams

def load_wordnet_data(index_file, data_file):
    """
    Loads WordNet index and data files into dictionaries.
    """
    index_dict = {}
    data_dict = {}

    # Load index file
    with open(index_file, 'r') as file:
        for line in file:
            token, refs = line.strip().split('|')
            index_dict[token] = refs.split(',')

    # Load data file
    with open(data_file, 'r') as file:
        for line in file:
            ref, definition = line.strip().split('|', 1)
            data_dict[ref] = definition

    return index_dict, data_dict

def lookup_definition(token, index_dict, data_dict):
    """
    Looks up the definition of a token using the WordNet data.
    """
    if token in index_dict:
        refs = index_dict[token]
        definitions = [data_dict[ref] for ref in refs]
        return '; '.join(definitions)
    return None

def print_ngrams_with_definitions(ngrams, definitions):
    """
    Prints n-grams along with their definitions.
    """
    for n in ngrams:
        print(f"\n{n}-grams:")
        for ngram, definition in zip(ngrams[n], definitions[n]):
            print(f"{ngram}: {definition if definition else 'No definition found'}")

# Define paths
index_file = 'NounsIndex.txt'
data_file = 'NounsData.txt'
test_files_folder = 'S24 test_files'

# Load WordNet data
index_dict, data_dict = load_wordnet_data(index_file, data_file)

# List available test files
test_files = sorted(os.listdir(test_files_folder))
print("Available test files:")
for i, test_file in enumerate(test_files, start=1):
    print(f"{i}. {test_file}")

# Prompt user to select a file to process
file_choice = int(input("\nSelect a file to process by entering the corresponding number: ")) - 1
selected_file = test_files[file_choice]
file_path = os.path.join(test_files_folder, selected_file)

print(f"\nProcessing {selected_file}:\n")

# Read the input text
input_text = read_file(file_path)

# Tokenize sentences and words
sentences = tokenize_sentences(input_text)
words_in_sentences = [tokenize_words(sentence) for sentence in sentences]

# Generate n-grams
ngrams = {n: [generate_ngrams(words, n) for words in words_in_sentences] for n in range(2, 5)}

# Look up definitions for n-grams
definitions = {n: [[lookup_definition(ngram, index_dict, data_dict) for ngram in ngram_list] for ngram_list in ngrams[n]] for n in ngrams}

# Print the n-grams with their definitions
for n in range(2, 5):
    print(f"\n{n}-grams:")
    for ngram_list, def_list in zip(ngrams[n], definitions[n]):
        for ngram, definition in zip(ngram_list, def_list):
            print(f"{ngram} {definition if definition else ''}")
