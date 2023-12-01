import subprocess

# Mallet command to import file
import_cmd = [
    '/path/to/mallet',  #malletPath
    'import-file',
    '--input', '/path/to/Stocks15.csv',  #Cricket.csv path
    '--output', 'stocks15.mallet',
    '--keep-sequence'
]

# Run Mallet import command
subprocess.run(import_cmd)

# Mallet command to train topics
train_cmd = [
    '/path/to/mallet',  # malletPath
    'train-topics',
    '--input', 'stocks15.mallet',
    '--num-topics', '10',  #topicNumber
    '--output-state', 'stocks15_model_state.gz',
    '--output-doc-topics', 'stocks15_doc_topics.txt',
    '--output-topic-keys', 'stocks15_word_topics.txt'
]

# Run Mallet train topics command
subprocess.run(train_cmd)
