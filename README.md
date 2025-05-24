# Document Vault

A web app to upload, search, and preview documents (PDF, DOCX, JPG, PNG, JPEG) with OCR support for scanned files, built with Streamlit.

---

## Features

- Upload and tag documents (PDF, DOCX, images)
- Search by keyword and filter by tags
- Extracts text from images and scanned PDFs using Tesseract OCR
- Content preview for each document

---

## Requirements

- Python 3.8+
- [Tesseract-OCR](https://github.com/tesseract-ocr/tesseract) (system dependency)

---

## Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/<your-username>/document_vault.git
   cd document_vault
   ```

2. **Create and activate a virtual environment:**
   ```sh
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On Mac/Linux:
   source venv/bin/activate
   ```

3. **Install Python dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Install Tesseract-OCR:**

   - **Windows:**  
     Download and run the [Tesseract installer](https://github.com/UB-Mannheim/tesseract/wiki).  
     Add the install path (e.g., `C:\Program Files\Tesseract-OCR`) to your system PATH.

   - **Mac (with Homebrew):**
     ```sh
     brew install tesseract
     ```

   - **Linux (Debian/Ubuntu):**
     ```sh
     sudo apt-get install tesseract-ocr
     ```

5. **Verify Tesseract installation:**
   ```sh
   tesseract --version
   ```
   You should see the Tesseract version information.

---

## Running the Application

```sh
streamlit run main.py
```
- The app will open in your browser at [http://localhost:8501](http://localhost:8501)

---

## Notes

- If you get a `TesseractNotFoundError`, ensure Tesseract is installed and its path is in your system PATH.
- You can adjust the Tesseract path in your code if needed:
  ```python
  import pytesseract
  pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
  ```

---


## Acknowledgements

- [Streamlit](https://streamlit.io/)
- [pytesseract](https://github.com/madmaze/pytesseract)
- [PyMuPDF](https://pymupdf.readthedocs.io/)
- [python-docx](https://python-docx.readthedocs.io/)