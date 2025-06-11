# src/main.py

from utils import load_help_articles
from embedder import build_index, search_index
from summarizer import summarize_answer
import os
from dotenv import load_dotenv

load_dotenv()

data_path = os.getenv("PATH_TO_FILE")
articles = load_help_articles(data_path)
index, texts = build_index(articles)

print("Type your question. Type 'exit' to quit.")
while True:
    query = input("\nQuestion: ")
    if query.lower() == "exit":
        break
    results = search_index(index, texts, query)
    for i, res in enumerate(results):
        print(f"\nResult {i+1}:")
        print("Title:", res["title"])
        summary = summarize_answer(res["content"], query)
        print("Answer:", summary)
