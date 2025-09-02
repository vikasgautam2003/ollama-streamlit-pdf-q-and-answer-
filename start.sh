#!/bin/bash

# Start Ollama server in the background
ollama serve &

# Give the server a few seconds to start
sleep 5

# Pull TinyLlama model (once server is running)
ollama pull tinyllama

# Start Streamlit app
streamlit run pdfSummary.py --server.port=8501 --server.address=0.0.0.0
