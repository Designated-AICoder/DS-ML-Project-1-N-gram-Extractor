


# N-gram Extractor

## Introduction
This project is part of the INFO6145 Data Science and Machine Learning course at Fanshawe College. The goal is to create an N-gram extractor that processes text files, generates 2-grams, 3-grams, and 4-grams, and retrieves their definitions using the WordNet lexical database.

## Requirements
- Python 3.x
- NLTK library
- WordNet data files (`NounsData.txt` and `NounsIndex.txt`)
- Test files (`test_text1.txt` to `test_text8.txt`) in the `S24 test_files` folder

## Setup
1. Clone the repository.
2. Ensure `NounsData.txt` and `NounsIndex.txt` are in the same directory as the script.
3. Place the test files in the `S24 test_files` folder.

## Usage
Run the script to process the test files and generate n-grams with their definitions.

```bash
python ngram_extractor.py
```

## Functions

### `read_file(file_path)`
Reads the input text file and returns the content as a string.
- **Parameters:**
  - `file_path` (str): Path to the input text file.
- **Returns:**
  - `str`: Content of the input file.

### `tokenize_sentences(text)`
Tokenizes the input text into sentences.
- **Parameters:**
  - `text` (str): The input text as a string.
- **Returns:**
  - `list`: List of sentences.

### `tokenize_words(sentence)`
Tokenizes a sentence into words.
- **Parameters:**
  - `sentence` (str): A single sentence as a string.
- **Returns:**
  - `list`: List of words.

### `generate_ngrams(words, n)`
Generates n-grams from the list of words.
- **Parameters:**
  - `words` (list): A list of words.
  - `n` (int): The number of words in each n-gram.
- **Returns:**
  - `list`: List of n-grams.

### `wordnet_data(index_file, data_file)`
Loads WordNet index and data files into dictionaries.
- **Parameters:**
  - `index_file` (str): Path to the WordNet index file.
  - `data_file` (str): Path to the WordNet data file.
- **Returns:**
  - `tuple`: Two dictionaries, one for the index and one for the data.

### `lookup_definition(token, index_dict, data_dict)`
Looks up the definition of a token using the WordNet data.
- **Parameters:**
  - `token` (str): The n-gram token.
  - `index_dict` (dict): Dictionary containing WordNet index data.
  - `data_dict` (dict): Dictionary containing WordNet data definitions.
- **Returns:**
  - `str`: Definition of the token if found, else `None`.

### `print_ngrams_with_definitions(ngrams, definitions)`
Prints n-grams along with their definitions.
- **Parameters:**
  - `ngrams` (dict): Dictionary containing n-grams.
  - `definitions` (dict): Dictionary containing definitions for the n-grams.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Citations
- NLTK: Natural Language Toolkit. (n.d.). Retrieved from [https://www.nltk.org/](https://www.nltk.org/)
- WordNet: Princeton University "About WordNet." WordNet. Princeton University. 2010.
