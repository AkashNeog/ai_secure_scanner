# 🔐 AI Secure Scanner

An AI-powered code vulnerability scanner that analyzes Python source code for potential security issues using Abstract Syntax Trees (AST) and NLP on comments. This tool helps developers detect unsafe patterns, hardcoded secrets, and risky functions before deployment.

### 🌐 Live App

👉 [Try the Live Streamlit App](https://aisecurescanner-4tjwymq5gocjsqhy69krkn.streamlit.app/)

---

## 🚀 Features

- ✅ Detects use of unsafe functions like `eval()` and `exec()`
- ✅ Identifies hardcoded passwords in code
- ✅ Flags insecure imports like `pickle`
- ✅ Uses NLP-like scanning to detect suspicious keywords in comments (e.g., `TODO`, `fixme`, `insecure`)
- ✅ Fast, lightweight, and easy to use via web

---

## 📂 How It Works

The app uses:

- **AST (Abstract Syntax Tree)** to traverse and inspect code structure.
- **Regex and heuristics** to identify patterns like hardcoded secrets.
- **Streamlit** to provide a clean web UI for scanning and viewing results.

---

## 🛠️ Usage

### 1. Run Locally

```bash
git clone https://github.com/AkashNeog/ai_secure_scanner.git
cd ai_secure_scanner
pip install -r requirements.txt
streamlit run streamlit_app.py
