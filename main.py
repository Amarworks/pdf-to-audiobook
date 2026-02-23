# -------------------------------
# PDF to Audiobook Converter
# Beginner Friendly Version
# -------------------------------

import pyttsx3                      # Text to Speech library
from PyPDF2 import PdfReader        # PDF reading library
from tkinter.filedialog import askopenfilename  # To select PDF file


# Step 1: Select PDF file
print("Select a PDF file...")
pdf_path = askopenfilename()

# If user cancels file selection
if not pdf_path:
    print("No file selected!")
    exit()

# Step 2: Read PDF
reader = PdfReader(pdf_path)
print("PDF opened successfully!")

# Step 3: Initialize Text-to-Speech engine
engine = pyttsx3.init()

# Step 4: Read each page and speak
for page_number in range(len(reader.pages)):
    page = reader.pages[page_number]
    text = page.extract_text()

    if text:
        print(f"Reading page {page_number + 1}")
        engine.say(text)

# Step 5: Play the audio
engine.runAndWait()

print("Audiobook finished!")