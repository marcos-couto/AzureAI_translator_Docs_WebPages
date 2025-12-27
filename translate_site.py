import requests
import os
from bs4 import BeautifulSoup
from docx import Document
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
subscription_key = os.getenv("AZURE_TRANSLATOR_KEY")
endpoint = os.getenv("AZURE_TRANSLATOR_ENDPOINT")
location = os.getenv("AZURE_TRANSLATOR_REGION")
target_language = "en-us"

def translator_text(text, target_language):
    headers = {
        "Ocp-Apim-Subscription-Key": subscription_key,
        "Ocp-Apim-Subscription-Region": location,
        "Content-type": "application/json",
        "X-ClientTraceId": str(os.urandom(16))
    }

    body = [{ "text": text }]
    params = { "from": "pt-br", "to": target_language }

    response = requests.post(endpoint, params=params, headers=headers, json=body)
    result = response.json()
    return result[0]["translations"][0]["text"]

def translate_site(url, output_filename="translated_site.docx"):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    texts = [p.get_text() for p in soup.find_all("p")]
    translated_texts = [translator_text(t, target_language) for t in texts if t.strip()]

    doc = Document()
    for line in translated_texts:
        doc.add_paragraph(line)

    doc.save(output_filename)
    print(f"Translated site content saved as: {output_filename}")
    return output_filename

if __name__ == "__main__":
    url = "https://marcos-couto.github.io/"
    output_file = translate_site(url, "site_translation_en-us.docx")
