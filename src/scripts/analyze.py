import pandas as pd

def load_data(speakers_file, topics_file, sessions_file):
    speakers = pd.read_csv(speakers_file)
    topics = pd.read_csv(topics_file)
    sessions = pd.read_csv(sessions_file)
    return speakers, topics, sessions

def analyze_speakers(speakers):
    # 分析講者的活躍度
    active_speakers = speakers.groupby('speaker_name').size().reset_index(name='session_count')
    return active_speakers.sort_values(by='session_count', ascending=False)

def analyze_topics(topics):
    # 分析主題的關鍵字出現次數
    topic_counts = topics['topic'].value_counts().reset_index()
    topic_counts.columns = ['topic', 'count']
    return topic_counts

def analyze_sessions(sessions):
    # 分析議程的主題分布
    session_topics = sessions['topic'].value_counts().reset_index()
    session_topics.columns = ['topic', 'session_count']
    return session_topics

if __name__ == "__main__":
    speakers_file = '../data/processed/speakers.csv'
    topics_file = '../data/processed/topics.csv'
    sessions_file = '../data/processed/sessions.csv'
    
    speakers, topics, sessions = load_data(speakers_file, topics_file, sessions_file)
    
    active_speakers = analyze_speakers(speakers)
    topic_analysis = analyze_topics(topics)
    session_analysis = analyze_sessions(sessions)
    
    print("Active Speakers:\n", active_speakers.head(10))
    print("\nTopic Analysis:\n", topic_analysis.head(10))
    print("\nSession Analysis:\n", session_analysis.head(10))