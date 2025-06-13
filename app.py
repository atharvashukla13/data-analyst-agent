import streamlit as st
import pandas as pd
import pytesseract
from PIL import Image
import pdfplumber
import docx
from pdf2image import convert_from_path
import requests
import os

# Setup paths
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
poppler_path = r"C:\poppler\Library\bin"  # Update if needed

# Together API config
TOGETHER_API_KEY = "56c1259c01c51607d384ec352955a3703582969e2e8fd4f35480787acc164840"
MODEL_NAME = "meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8"

# LLaMA prompt
def query_llama(prompt):
    url = "https://api.together.xyz/inference"
    headers = {"Authorization": f"Bearer {TOGETHER_API_KEY}"}
    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "max_tokens": 512,
        "temperature": 0.7,
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        result = response.json()

        if "choices" in result:
            return result["choices"][0]["text"].strip()
        elif "error" in result:
            return f"[API ERROR] {result['error']}"
        else:
            return f"[UNKNOWN ERROR] Raw response: {result}"
    except Exception as e:
        return f"[EXCEPTION] {str(e)}"


# File parser
def load_file(file):
    ext = file.name.split(".")[-1].lower()
    if ext == "csv":
        return pd.read_csv(file)
    elif ext in ["xls", "xlsx"]:
        return pd.read_excel(file)
    elif ext == "txt":
        return file.read().decode("utf-8")
    elif ext == "docx":
        doc = docx.Document(file)
        return "\n".join([p.text for p in doc.paragraphs])
    elif ext == "pdf":
        with pdfplumber.open(file) as pdf:
            text = "\n".join([page.extract_text() or '' for page in pdf.pages])
        if len(text.strip()) < 10:
            pages = convert_from_path(file, poppler_path=poppler_path)
            text = "\n\n".join([pytesseract.image_to_string(p) for p in pages])
        return text
    elif ext in ["png", "jpg", "jpeg"]:
        return pytesseract.image_to_string(Image.open(file))
    else:
        return "[Unsupported file type]"

# Streamlit UI
st.title("📊 Data Analyst Agent")
st.markdown("Upload a file and ask questions powered by LLaMA-4 Maverick!")

uploaded_file = st.file_uploader("Upload your file", type=["csv", "xlsx", "txt", "pdf", "docx", "png", "jpg", "jpeg"])

question = st.text_input("Ask a question about your file")

if uploaded_file and question:
    result = load_file(uploaded_file)

    if isinstance(result, pd.DataFrame):
        st.write("Here's a preview of your dataset:")
        st.dataframe(result.head())

        summary = result.describe().to_string()
        prompt = f"Dataset summary:\n{summary}\n\nQuestion: {question}"
        answer = query_llama(prompt)
        st.markdown("### 🧠 LLaMA's Answer")
        st.write(answer)

    else:
        st.markdown("### 📄 Extracted Text (Preview)")
        st.text(result[:1000])

        prompt = f"Here is a document:\n{result[:1500]}\n\nAnswer this question:\n{question}"
        answer = query_llama(prompt)
        st.markdown("### 🧠 LLaMA's Answer")
        st.write(answer)
