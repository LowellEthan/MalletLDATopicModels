import subprocess

# Mallet command to import file
import_cmd = [
    '/Users/lowellethan/Downloads/mallet-2.0.6/bin/mallet',  # Mallet executable path
    'import-file',
    '--input', '/Users/lowellethan/Desktop/trained/disneyland_reviews_20/DisneylandReviews.csv',  # CSV file path
    '--output', '/Users/lowellethan/Desktop/trained/DisneylandReviews.mallet',
    '--keep-sequence'
]

# Run Mallet import command
subprocess.run(import_cmd)

# Mallet command to train topics
train_cmd = [
    '/Users/lowellethan/Downloads/mallet-2.0.6/bin/mallet',  # Mallet executable path
    'train-topics',
    '--input', '/Users/lowellethan/Desktop/trained/DisneylandReviews.mallet',
    '--num-topics', '15',  # Number of topics
    '--output-state', '/Users/lowellethan/Desktop/trained/DisneylandReviews_model_state.gz',
    '--output-doc-topics', '/Users/lowellethan/Desktop/trained/DisneylandReviews_doc_topics.txt',
    '--output-topic-keys', '/Users/lowellethan/Desktop/trained/DisneylandReviews_word_topics.txt'
]

# Run Mallet train topics command
subprocess.run(train_cmd)
