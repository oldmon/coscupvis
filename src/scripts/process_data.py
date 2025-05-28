def process_data():
    import json
    import pandas as pd
    import os

    # Define the path to the raw data
    raw_data_path = 'src/data/raw/sessions/'
    processed_data_path = 'src/data/processed/'

    # Initialize lists to hold processed data
    speakers = []
    topics = []
    sessions = []

    # Process each year's data
    for year in range(2020, 2025):
        file_path = os.path.join(raw_data_path, f'{year}.json')
        
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            for session in data['sessions']:
                # Extract speaker information
                for speaker in session['speakers']:
                    speakers.append({'name': speaker, 'year': year})

                # Extract topic information
                for topic in session['topics']:
                    topics.append({'topic': topic, 'year': year})

                # Extract session information
                sessions.append({
                    'title': session['title'],
                    'description': session['description'],
                    'year': year,
                    'speakers': ', '.join(session['speakers']),
                    'topics': ', '.join(session['topics'])
                })

    # Create DataFrames and save to CSV
    speakers_df = pd.DataFrame(speakers)
    topics_df = pd.DataFrame(topics)
    sessions_df = pd.DataFrame(sessions)

    speakers_df.to_csv(os.path.join(processed_data_path, 'speakers.csv'), index=False)
    topics_df.to_csv(os.path.join(processed_data_path, 'topics.csv'), index=False)
    sessions_df.to_csv(os.path.join(processed_data_path, 'sessions.csv'), index=False)

if __name__ == "__main__":
    process_data()