# PDF to Audiobook Converter (Python)

This is a beginner-friendly Python project that converts a PDF file into an audiobook using text-to-speech.

The project is designed for students and beginners who want to learn how to work with PDF files and basic text-to-speech in Python.

---

## Project Overview

Reading PDFs for long periods can be tiring.  
This program allows users to select a PDF file and listen to its content instead of reading it.

The focus of this project is:
- Simple logic
- Easy to understand code
- Learning-oriented structure

---

## What This Project Does

1. Opens a file dialog to select a PDF file  
2. Reads the PDF page by page  
3. Extracts text from each page  
4. Converts the extracted text into speech  

The audio is played directly using Python.

---

## Who Can Use This Project

- Python beginners  
- Students working on small projects  
- Anyone learning file handling and text-to-speech  

No advanced Python knowledge is required.

---

## Technologies Used

- Python 3  
- PyPDF2 (for reading PDF files)  
- pyttsx3 (for text-to-speech)  
- tkinter (for file selection dialog)

---

## Project Structure
pdf-to-audiobook/
│
├── main.py
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore

---


Only one Python file is used to keep the project easy to understand.

---

## How the Program Works

- The user selects a PDF file
- The program opens the PDF
- Text is extracted from each page
- The text is passed to the text-to-speech engine
- The audio is played

Each step is written clearly in the code with comments.

---

## How to Run the Project

### Step 1: Install Python

Make sure Python 3 is installed on your system.

Check using:
```base
python --version
```
###Step 2: Install Required Libraries

Open terminal or command prompt in the project folder and run:
```
pip install -r requirements.txt
```
###Step 3: Run the Program
```
python main.py
```
A file selection window will open.
Select any text-based PDF file to start listening.
