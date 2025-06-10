#  HelpBot AI

An AI-powered assistant that answers user questions based on help center documentation — built as a technical interview prototype.

> “How do I reset my password?”  
> “Where can I update my payment info?”  
> “How do I invite teammates?”  

HelpBot delivers fast, relevant answers by searching through help articles and using GPT to provide clear, human-like responses.

---

##  What It Does

-  **Understands user questions** using OpenAI embeddings  
-  **Searches help documents** for the most relevant matches  
-  **Summarizes the best answer** using GPT (optional layer)  
-  **Simple CLI or UI interface** for testing and demonstration  

---

##  Project Structure

<pre> helpbot/ ├── data/ # Sample or scraped help articles │ └── help_articles.json │ ├── embeddings/ # (Optional) Saved vector index │ └── index.faiss │ ├── src/ # All core logic lives here │ ├── main.py # CLI or app entry point │ ├── embedder.py # Embedding + retrieval functions │ ├── summarizer.py # GPT-based summarizer │ └── utils.py # Data loading, formatting, etc. │ ├── .env # API keys and environment variables ├── requirements.txt # Python dependencies └── README.md # You're looking at it </pre>



##  Installation & Setup

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





Built by Sarab as part of a technical prototype project.


