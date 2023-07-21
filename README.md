# Garden Path Sentences Parser

This is a Python program that demonstrates how to use the spaCy library to tokenize and perform Named Entity Recognition (NER) on a set of garden path sentences. It also looks up and prints the meanings of the entities detected in the sentences.

## Introduction

Garden path sentences are sentences that initially appear to be grammatically correct, but as the reader progresses, they become confusing or difficult to understand. The program aims to tokenize these sentences, identify entities within them, and provide explanations for those entities.

## Dependencies

Before running the program, make sure you have the spaCy library installed:

```bash
pip install spacy
```

Additionally, you'll need to download the "en_core_web_sm" model for English. You can do this using the following command:

```bash
python -m spacy download en_core_web_sm
```

## How the Program Works

1. Import the spaCy library and load the "en_core_web_sm" model:

The program starts by importing the spaCy library and loading the English model "en_core_web_sm".

2. Define Garden Path Sentences:

The program defines a list of garden path sentences to analyze. These sentences are designed to be misleading or difficult to comprehend initially.

3. Tokenize and Perform Named Entity Recognition:

The program processes each garden path sentence using spaCy's NLP pipeline to tokenize the sentences and perform Named Entity Recognition (NER). It identifies entities like CARDINAL (numerical values) and GPE (countries, cities, states).

4. Print Detected Entities and Explanations:

For each sentence, the program prints the original sentence and the detected entities along with their labels and explanations. This provides insights into the entities spaCy has recognized and their types.

5. Print Entity Explanations:

Finally, the program looks up and prints the explanations for the recognized entities. It demonstrates how "CARDINAL" represents numerals and "GPE" refers to countries, cities, and states.

## How to Use

1. Ensure you have Python and the spaCy library with the "en_core_web_sm" model installed on your machine.

2. Clone the repository to your local machine using the following command:

```bash
git clone https://github.com/wasim-jussab/garden-path-sentences.git
```

3. Change to the project directory:

```bash
cd garden-path-sentences
```

4. Run the program:

```bash
python garden_path_sentences.py
```

5. The program will process the garden path sentences, detect entities, and provide explanations for the recognized entities.

## Contributing

If you'd like to contribute to this project or report any issues, please feel free to open a pull request or submit an issue on the GitHub repository.

---
Created by [Wasim Jussab](https://github.com/wasim-jussab)
```
