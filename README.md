# Wikipedia QA Bot

A **Wikipedia Question Answering Bot** that allows users to input a Wikipedia article title, ask questions about its content, and receive AI-generated answers. The bot uses **LangChain**, **FAISS**, and **Hugging Face Transformers** for efficient document retrieval and QA processing.

## Features
- Scrapes Wikipedia articles based on user-input titles and language selection.
- Uses **FAISS** for efficient document retrieval.
- Employs **Hugging Face's Transformers** for question answering.
- Deployed using **Streamlit** with a Flask backend.

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/WikiBot.git
cd WikiBot
```

### 2. Create a Virtual Environment
```bash
conda create --name wikibot python=3.11
conda activate wikibot
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

## Usage

### Run the Streamlit App
```bash
streamlit run app.py
```

### Input Options
- **Wikipedia Title**: Enter the title of the Wikipedia page to scrape.
- **Language Selection**: Choose between English (`en`) or Arabic (`ar`).
- **Ask a Question**: Once the article is scraped, input a question related to its content.

## Project Structure
```
WikiBot/
│── app.py                  # Streamlit UI
│── controller.py           # Main Controller
│── requirements.txt        # Dependencies
│── LICENSE
|── README.md
|
├── utils/
│   ├── qa_chain.py         # Question Answering Pipeline
│   ├── search.py           # FAISS Document Retrieval
│   ├── wiki_scrap.py       # Wikipedia Scraping Utility
|   |── __init__.py
```

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

# This project is still under development 

