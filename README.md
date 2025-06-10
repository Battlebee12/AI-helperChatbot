# 🤖 HelpBot AI

An AI-powered assistant that answers user questions based on help center documentation — built as a technical interview prototype.

> “How do I reset my password?”  
> “Where can I update my payment info?”  
> “How do I invite teammates?”  

HelpBot delivers fast, relevant answers by searching through help articles and using GPT to provide clear, human-like responses.

---

## 🧠 What It Does

- 🔍 **Understands user questions** using OpenAI embeddings  
- 📚 **Searches help documents** for the most relevant matches  
- 🧾 **Summarizes the best answer** using GPT (optional layer)  
- 🖥️ **Simple CLI or UI interface** for testing and demonstration  

---

## 🗂️ Project Structure

helpbot/
├── data/
│ └── help_articles.json # Sample help docs
├── embeddings/
│ └── index.faiss # Saved vector index (optional)
├── src/
│ ├── main.py # CLI / entrypoint
│ ├── embedder.py # Embedding + retrieval logic
│ ├── summarizer.py # GPT-based answer generator
│ └── utils.py # Utility functions (load data, etc.)
├── .env # API key
├── requirements.txt
└── README.md


## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/helpbot.git
cd helpbot
```
### 2. Create Virtual Environment
```bash

python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash

pip install -r requirements.txt
```

### 4. Add Your API Key
Create a .env file in the root directory with:
```bash
ini

OPENAI_API_KEY=your-api-key-here
```

### 5. Run the Bot
```bash
python src/main.py
```

💬 Example Questions You Can Ask
"How do I reset my password?"

"Where can I view my past orders?"

"How do I update my email address?"

"What’s the cancellation policy?"

🛠️ Tech Stack
🧠 OpenAI Embeddings + GPT (openai)

🔍 FAISS (optional) for vector search

📚 Python 3, NumPy, Scikit-learn

🖼️ Streamlit (optional UI layer)

🔐 .env config for key management

📌 Future Enhancements
Role-based or user-context filtering

Live web deployment with Streamlit or Flask

Real-time feedback (like 👍 / 👎 answers)

API wrapper to connect to live help center data

✍️ Author
Built by Sarab as part of a technical prototype project.

🚀 Smarter help, faster answers.
