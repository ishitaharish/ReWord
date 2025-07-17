# ReWord

ReWord is a lightweight, standalone desktop application developed in Python that allows users to automatically restructure and rephrase text, making it suitable for use in professional messages or emails. The application combines a Tkinter UI with backend NL processing using Cohere's API to offer an easy way to rephrase and transform content.

## Features

- User-friendly graphical interface
- Input text box and output display for restructured content
- Standalone `.app` file for macOS created using PyInstaller

## Tech Stack

- **Language:** Python 3.11  
- **GUI:** Tkinter  
- **Packaging:** PyInstaller  
- **Environment:** Conda-managed virtual environment  

---

## Installation & Usage

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/ReWord.git
cd ReWord
```
Note: At this point you must add your API key from Cohere, and make any changes to the prompt necessary. 

### 2. Set Up a Virtual Environment (Recommended)
This project was developed and packaged within a clean Conda virtual environment to avoid package conflicts.
```bash
conda create --name clean-env python=3.11
conda activate clean-env
pip install -r requirements.txt
```
Note: Do not install pathlib via pip. It is part of Python’s standard library and installing it explicitly causes packaging errors with PyInstaller.

### 3. Run the Script (for development)


```bash
python ReWord.py
```

### 4. Build the Standalone App (macOS)
```bash
pyinstaller --onefile --windowed ReWord.py
```

The output .app or .exe file will be located in the dist/ directory.

































































