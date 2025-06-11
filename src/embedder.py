
import openai
import faiss
import numpy as np
import json
import os
from dotenv import load_dotenv


load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


EMBEDDING_MODEL = "text-embedding-3-small"

# This function sends text to OpenAI and gets back a vector (embedding)
def get_embedding(text):
    response = openai.embeddings.create(
        input=[text],
        model=EMBEDDING_MODEL
    )
    
    embedding = response.data[0].embedding
    return np.array(embedding, dtype=np.float32)

# This function builds the FAISS search index from a list of help articles
def build_index(help_articles):
    # The size 1536 comes from the embedding model
    index = faiss.IndexFlatL2(1536)

    
    texts = []
    all_embeddings = []

    for article in help_articles:
       
        full_text = article["title"] + "\n" + article["content"]
        embedding = get_embedding(full_text)

        texts.append(article)
        all_embeddings.append(embedding)

   
    all_embeddings = np.vstack(all_embeddings)

    
    index.add(all_embeddings)

    return index, texts

# This function takes a user question and finds the most similar articles
def search_index(index, texts, user_question, top_k=3):
    
    question_embedding = get_embedding(user_question).reshape(1, -1)

   
    distances, indices = index.search(question_embedding, top_k)

    
    results = []
    for i in indices[0]:
        results.append(texts[i])

    return results
