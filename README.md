# AI Resume Screener 🚀

An AI-powered Resume Screening System built using **Endee Vector Database** for semantic search and intelligent candidate matching.

---

## 📌 Project Overview

Recruiters often receive hundreds of resumes for a single position.  
Manually screening resumes is time-consuming and inefficient.

This project uses:

- 🔎 Semantic Search
- 🧠 Sentence Transformers
- 📂 PDF Parsing
- 🗄 Endee Vector Database

to automatically match resumes with job descriptions.

---

## 🏗 System Architecture

1. Resume PDF is uploaded
2. Text is extracted using PDF parser
3. Text is converted into embeddings
4. Embeddings are stored in Endee vector database
5. User enters job description query
6. System performs semantic similarity search
7. Best matching resumes are returned

---

## 🛠 Tech Stack

- Python 3.12
- Sentence Transformers
- Endee Vector Database
- NumPy
- PDF Parser

---

## 📂 Project Structure

AI-Resume-Screener/
│
├── main.py
├── embedder.py
├── vector_store.py
├── pdf_parser.py
├── requirements.txt
└── sample_resume.pdf

## ⚙ Installation & Setup

### 1️⃣ Clone Repository

git clone https://github.com/rohsh22ece-cmd/AI-Resume-Screener.git
cd AI-Resume-Screener


### 2️⃣ Install Dependencies

pip install -r requirements.txt


### 3️⃣ Run the Project

python main.py


## 💡 Features

- Resume text extraction
- Embedding generation
- Vector storage using Endee
- Semantic resume search
- Internship-ready modular structure

## 🎯 Use Case

- HR Resume Screening
- Candidate Shortlisting
- Talent Search Automation
- Semantic Job Matching

## 📌 Future Improvements

- Web Interface (Streamlit/Flask)
- Multiple Resume Upload
- Ranking Score Display
- Cloud Deployment

## 🚀 How to Run

1. Clone the repository
git clone https://github.com/rohsh22ece-cmd/AI-Resume-Screener.git

2. Install dependencies
pip install -r requirements.txt

3. Run the project
python main.py

## 📊 Sample Output

Top Matching Resume:
Score: 0.87
Candidate: John Doe
Matched Skills: Python, Machine Learning, NLP


## 👨‍💻 Author

Rohit Shebinakatti  
GitHub: https://github.com/rohsh22ece-cmd


