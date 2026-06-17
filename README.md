# Documentation Summarizer

A simple Generative AI application built using LangChain and Mistral AI that loads Azure documentation from a text file and generates a concise summary of the content.

## Features

* Load Azure documentation from a text file
* Generate AI-powered summaries using Mistral AI
* Built with LangChain Prompt Templates
* Environment variable support using dotenv
* Easy to customize for other documents

## Tech Stack

* Python
* LangChain
* Mistral AI
* python-dotenv

## Project Structure

```text
project/
│
├── main.py
├── .env
├── .gitignore
├── requirements.txt
├── README.md
│
└── document_loaders/
    └── Microsoft Azure Documentation.txt
    └── AWS Documentation.pdf
    |__test.py
```

## Installation

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd <repository-name>
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the virtual environment:

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Create a .env File

```env
MISTRAL_API_KEY=your_api_key_here
```

## Usage

Run the application:

```bash
python main.py
```

The application will:

1. Load the Azure documentation text file.
2. Send the document content to Mistral AI.
3. Generate a summarized version of the document.
4. Display the summary in the terminal.

## Sample Code Flow

* Load document using TextLoader
* Create a ChatPromptTemplate
* Pass document content to the prompt
* Invoke Mistral AI model
* Print generated summary

## Dependencies

```text
langchain
langchain-core
langchain-community
langchain-mistralai
python-dotenv
```

## Future Enhancements

* PDF document support
* Multiple document summarization
* Streamlit user interface
* RAG (Retrieval-Augmented Generation)
* Vector Database Integration
* Question Answering over documents


