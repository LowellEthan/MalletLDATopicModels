import subprocess

datasets = [
    '/path/to/pop1.csv',
    '/path/to/pop2.csv',
    '/path/to/pop3.csv'
]

for i, dataset_path in enumerate(datasets, start=1):
    # Mallet command to import file
    import_cmd = [
        '/path/to/mallet',  # Replace with your Mallet path
        'import-file',
        '--input', dataset_path,
        '--output', f'pop25topic.mallet',
        '--keep-sequence'
    ]

    # Run Mallet import command
    subprocess.run(import_cmd)

    # Mallet command to train topics
    train_cmd = [
        '/path/to/mallet',  # Replace with your Mallet path
        'train-topics',
        '--input', f'pop25topic.mallet',
        '--num-topics', '10',  # Number of topics
        '--output-state', f'pop25topic_model_state.gz',
        '--output-doc-topics', f'pop25topic_doc_topics.txt',
        '--output-topic-keys', f'pop25topic_word_topics.txt'
    ]

    # Run Mallet train topics command
    subprocess.run(train_cmd)
