import pandas as pd

def load_radar_data(file_path):
    df = pd.read_csv(file_path)
    return df[df['signal_strength'] > 30]