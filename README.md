# 🎧 PDF to Audiobook Converter (Python)

Convert any PDF document into an **audiobook** using Python.  
Perfect for students, accessibility, and learning on the go 📖➡️🔊

This project extracts text from a PDF and converts it into speech using Python’s text-to-speech capabilities.

---

## 🚀 Why This Project?

Reading PDFs for long hours can be tiring.  
This tool helps you **listen instead of read**, making learning more flexible and accessible.

It is especially useful for:
- Students 📚
- Visually impaired users ♿
- Multitaskers 🎧

---

## ✨ Features

- 📄 Convert any PDF into audio
- 🎙️ Text-to-Speech using Python
- 🎵 Output in MP3/WAV format
- 🧩 Simple and modular code structure
- 🖥️ Easy to run from command line

---

## 🛠️ Tech Stack

- **Python 3**
- **PyPDF2** – for PDF text extraction
- **gTTS / pyttsx3** – for text-to-speech
- **OS / Sys modules** – for file handling

---

## 📂 Project Structure

```text
pdf-to-audiobook/
│
├── input_pdfs/
│   └── sample.pdf
│
├── output_audio/
│   └── sample_audio.mp3
│
├── src/
│   ├── pdf_reader.py
│   ├── audio_generator.py
│   └── main.py
│
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md
