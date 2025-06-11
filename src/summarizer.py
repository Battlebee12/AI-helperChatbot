

import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

MODEL = "gpt-3.5-turbo"

# give it a chunk of help article and a question, ask it to answer like support chat
def summarize_answer(article_text, question):
    prompt = [
        {"role": "system", "content": "You are a helpful support assistant. Answer clearly and briefly."},
        {"role": "user", "content": f"Question: {question}\n\nHelp Article: {article_text}\n\nAnswer the question using the article."}
    ]

    response = openai.chat.completions.create(
        model=MODEL,
        messages=prompt,
        temperature=0.5,
        max_tokens=200
    )

    return response.choices[0].message.content.strip()
