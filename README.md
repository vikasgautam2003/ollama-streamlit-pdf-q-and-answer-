# 📄 Ollama PDF Q & Ans

An AI-powered PDF Question-Answering and Summarization app built with **Streamlit** and **Ollama (TinyLlama)**.  
This project demonstrates how to integrate **local LLMs** with a modern web UI for document understanding.  

---

## 🚀 Features  
- 📑 Upload any PDF document  
- 🤖 Ask questions about the document content  
- 📝 Generate AI-powered summaries  
- ⚡ Powered by [Ollama](https://ollama.ai/) running **TinyLlama** locally  
- 🌐 Web UI built with [Streamlit](https://streamlit.io/)  

---

## 🛠️ Tech Stack  
- **LLM Backend** → Ollama (TinyLlama)  
- **Frontend** → Streamlit  
- **Containerization** → Docker  
- **Language** → Python 3.10+  

---

## 📂 Project Structure  
├── app.py / pdfSummary.py # Main Streamlit app
├── requirements.txt # Python dependencies
├── start.sh # Startup script (Ollama + Streamlit)
├── Dockerfile # Container setup
├── notes.txt # Development notes
└── README.md # Project documentation




---

## ⚙️ Setup Instructions  

### 🔹 Option A: Run Locally  
1. Install [Ollama](https://ollama.ai/)  
2. Pull the TinyLlama model:  
   ```bash
   ollama pull tinyllama



Install Python dependencies:

pip install -r requirements.txt


Run the app:

streamlit run pdfSummary.py --server.port 8501 --server.address 0.0.0.0

🔹 Option B: Run with Docker

Build the image:

docker build -t ollama_pdf_app .


Run the container:

docker run -p 8501:8501 ollama_pdf_app

🎯 Use Case

This project is ideal for:

Showcasing LLM integration skills

Building AI-powered portfolio projects

Demonstrating document question answering

📸 Demo (Screenshots / Video)

👉 Add screenshots of your UI here
👉 (Optional) Upload a short demo video / GIF

💡 Future Improvements

Support for larger models (Mistral, Llama 3)

Deploy lightweight version on free hosting (Render / Railway)

Hugging Face Space demo

👨‍💻 Author

Vikas Gautam
