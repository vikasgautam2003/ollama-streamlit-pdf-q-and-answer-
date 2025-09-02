# import streamlit as st
# from PyPDF2 import PdfReader
# import ollama

# st.title("📄 PDF Q&A with Ollama")

# uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

# if uploaded_file:
#     reader = PdfReader(uploaded_file)
#     document_text = ""
#     for page in reader.pages:
#         document_text += page.extract_text() + "\n"

#     st.success("PDF loaded successfully!")

#     question = st.text_input("Ask a question about the PDF:")

#     if question:
#         prompt = f"Here is a document:\n{document_text}\n\nQuestion: {question}"
#         response = ollama.chat(
#             model="tinyllama",
#             messages=[{"role": "user", "content": prompt}]
#         )
#         st.subheader("Answer:")
#         st.write(response["message"]["content"])













import streamlit as st
from PyPDF2 import PdfReader
import ollama

st.set_page_config(page_title="📄 PDF Q&A with Ollama", page_icon="🤖", layout="wide")

st.markdown("""
<link href="https://cdn.jsdelivr.net/npm/tailwindcss@3.3.3/dist/tailwind.min.css" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
<style>
body { font-family: 'Inter', sans-serif; background-color: #f0f4f8; }
.container { max-width: 66%; margin: auto; }
.glass-card { background: rgba(255,255,255,0.2); backdrop-filter: blur(12px); border-radius:1rem; padding:1.5rem; box-shadow:0 8px 32px rgba(0,0,0,0.1); margin-bottom:1.5rem; }
.header { text-align:center; margin-top:2rem; margin-bottom:3rem; }
.header h1 { font-size:3rem; font-weight:700; background: linear-gradient(90deg,#6B46C1,#D53F8C,#ED64A6); -webkit-background-clip: text; color: transparent; }
.header p { font-size:1.25rem; color:#4a5568; }
.button { background: linear-gradient(135deg,#6B46C1,#D53F8C); color:white; padding:0.5rem 1.5rem; border-radius:9999px; font-weight:600; cursor:pointer; transition:0.3s; margin-bottom:1rem; }
.button:hover { transform: scale(1.05); box-shadow:0 6px 20px rgba(0,0,0,0.15); }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="container">', unsafe_allow_html=True)

st.markdown("""
<div class="header">
    <h1>📄 PDF Q&A with Ollama</h1>
    <p>Upload a PDF and ask questions. Powered by TinyLlama.</p>
</div>
""", unsafe_allow_html=True)

with st.expander("ℹ️ How to Use", expanded=True):
    st.markdown("""
    1️⃣ Upload any PDF file.<br>
    2️⃣ Type your question about the PDF.<br>
    3️⃣ Get AI-powered answers instantly!
    """, unsafe_allow_html=True)

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf", label_visibility="visible")

if uploaded_file:
    reader = PdfReader(uploaded_file)
    document_text = ""
    for page in reader.pages:
        document_text += page.extract_text() + "\n"

    st.markdown('<div class="glass-card text-green-600 font-semibold">✅ PDF loaded successfully!</div>', unsafe_allow_html=True)

    question = st.text_input("Ask a question about the PDF:", placeholder="Type your question here...", key="question_input")

    if question:
        st.markdown('<div class="glass-card text-blue-600 font-semibold">⏳ Processing your question...</div>', unsafe_allow_html=True)
        
        prompt = f"Here is a document:\n{document_text}\n\nQuestion: {question}"
        response = ollama.chat(model="tinyllama", messages=[{"role": "user", "content": prompt}])

        st.markdown(f"""
        <div class="glass-card">
            <h3 class="text-xl font-bold text-purple-600 mb-2">Answer:</h3>
            <p class="text-gray-900">{response['message']['content']}</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown('<div class="glass-card text-green-600 font-semibold">✅ Question processed successfully!</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
