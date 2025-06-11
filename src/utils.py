import json

def load_help_articles(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)
