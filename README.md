# 📊 Data Analyst Agent

👉 **[🚀 Try the Live App](https://data-analyst-agent-unkan22ogxkebx69fmyy8h.streamlit.app/)**

An intelligent AI assistant that helps you extract insights from your files — just upload a document or dataset and ask plain-English questions. Built using LLaMA-4 Maverick from Together.ai.

---

## 🚀 Features

* 📁 Upload support for `.csv`, `.xlsx`, `.pdf`, `.txt`, `.docx`, `.jpg`, `.png`
* 🧠 LLaMA-4 Maverick 17B via Together API for Q\&A
* 🔍 Natural Language Analysis of both structured and unstructured data
* 📊 Visualization support for numeric data (bar plots, histograms)
* 🧾 OCR support for scanned PDFs and images using Tesseract + Poppler
* 🖥️ Streamlit frontend for an interactive experience
* 📜 Notebook backend (`agent.ipynb`) for reproducibility
* 🌐 Live deployment: **[Click here](https://data-analyst-agent-unkan22ogxkebx69fmyy8h.streamlit.app/)**

---

## 🧠 Tech Stack

* Python 3.11
* Together.ai API (LLaMA-4 Maverick 17B Instruct)
* Pandas, Matplotlib, Seaborn
* PDFPlumber, Pytesseract, pdf2image
* Streamlit (for web app)

---

## 📦 Folder Structure

```
data-analyst-agent/
├── app.py                  # Streamlit app
├── agent.ipynb             # Jupyter notebook backend
├── requirements.txt        # Python dependencies
├── sample.csv              # Sample file to test
├── README.md               # Project overview
├── screenshots/            # UI images (optional)
```

---

## 🛠 Installation

```bash
# Clone the repo
git clone https://github.com/atharvashukla13/data-analyst-agent.git
cd data-analyst-agent

# Install dependencies
pip install -r requirements.txt
```

---

## ▶️ How to Run

### 📓 Option 1: Jupyter Notebook

```bash
jupyter notebook agent.ipynb
```

### 🌐 Option 2: Streamlit App

```bash
python -m streamlit run app.py
```

Make sure to:

* Set your Together.ai API key in `app.py`
* Install Tesseract OCR and Poppler for PDF/image OCR support

---

## 🖼️ Demo Screenshots

![image](https://github.com/user-attachments/assets/9ec82b8c-b3f2-49ec-9688-bc1611e216cd)

---

## 🧪 Sample Use Cases

* Ask "Which department has the highest average salary?" after uploading a CSV
* Upload a PDF assignment file and ask "What are the key project requirements?"
* Upload a scanned receipt and extract text using OCR

---

## 🧠 About the LLM

This project uses the model:

```
meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8
```

Accessed via [Together.ai](https://www.together.ai/) APIs. This is the **mandatory** model as per assignment.

---

## ✨ Highlights

* Multi-format file handling
* LLM integration
* OCR support
* Clean UI and reproducible notebook backend

---

## 📬 Contact

Built with ❤️ by Atharva Shukla
[LinkedIn](https://linkedin.com/in/atharvashukla13) | [GitHub](https://github.com/atharvashukla13)

---

> ⭐ Star this repo if you found it useful — and feel free to fork for your own enhancements!
