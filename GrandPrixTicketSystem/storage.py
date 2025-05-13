import pickle
import os

def save_data(filename, data):
    with open(os.path.join("data", filename), "wb") as f:
        pickle.dump(data, f)

def load_data(filename):
    try:
        with open(os.path.join("data", filename), "rb") as f:
            return pickle.load(f)
    except (FileNotFoundError, EOFError):
        return []