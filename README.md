# AzureAI Translator Project

This repo contains two Python scripts that use Azure AI Translator:

- `translate_doc.py` → translates `.docx` documents from English to Portuguese (pt-br).
- `translate_site.py` → fetches and translates website text from English to Portuguese (pt-br).
## Project structure
azure-translate-project/
│
├── translate_doc.py        # Script to translate .docx files
├── translate_site.py       # Script to translate website text
├── requirements.txt        # Dependencies for easy installation
├── README.md               # Documentation for your project

## Notes on Each File
-translate_doc.py → Handles translation of Word documents (.docx) from English to Portuguese.
-translate_site.py → Fetches text from a website, translates it, and saves the output into a .docx.
-requirements.txt → Lists dependencies so anyone can install them with:
  >pip install -r requirements.txt

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt

