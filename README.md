# MediBridge: Multilingual Medical Translation Assistant

**MediBridge** is a powerful tool designed to bridge language barriers in healthcare by providing real-time, accurate translation of medical information. It supports voice, text, and image (OCR) inputs to assist medical professionals and patients in multilingual communication.

---

## Features

- Real-time translation of medical text and speech.
- Multilingual support (e.g., English, Tamil, Hindi).
- Voice-enabled interface for seamless doctor-patient conversations.
- OCR (Optical Character Recognition) integration to extract text from medical documents and images.
- Context-aware translation to ensure medical accuracy.
  
---

## Project Structure

- `MedBridge/` – Core translation engine handling text and voice translation.
- `MedVoiceAid/` – Voice interface module for speech recognition and synthesis.
- OCR functionality integrated using Tesseract OCR and `pytesseract`.

---

## Demo
https://youtu.be/DDzoH_HGP9g
---

## Tech Stack

### Frontend (User Interaction)
- **Tkinter** — GUI framework for desktop user interface  
- **SpeechRecognition** — For capturing and recognizing spoken input  
- **pyttsx3** — Offline text-to-speech synthesis  

### Backend (Core Logic & APIs)
- **Python 3.10+** — Main programming language  
- **Google Cloud Translation API** — For multilingual medical translation  
- **pytesseract** — Python wrapper for Tesseract OCR engine  
- **Tesseract OCR Engine** — For extracting text from medical images  
- **Pillow (PIL)** — Image processing for OCR  
- **Flask** — Lightweight API server (if applicable)  
- **Requests** — HTTP requests to external APIs  

---

## Getting Started

### Prerequisites

- Python 3.10+
- Tesseract OCR engine (for text extraction from images)
- Required Python packages (listed in `requirements.txt`)

---

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Sai-Deepan/MediBridge.git
    cd MediBridge
    ```

2. Install required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Install and configure Tesseract OCR (see **OCR Setup** below).

4. Configure translation API keys in `config.json` (copy from `config.example.json`):
    ```json
    {
      "source_language": "en",
      "target_language": "ta",
      "voice_enabled": true
    }
    ```

---
 
### Usage

- **Text Translation**
    ```bash
    python MedBridge/translate.py --text "Do you have any allergies?"
    ```

- **Voice Translation**
    ```bash
    python MedVoiceAid/voice_translate.py
    ```

- **OCR + Translation**
    Pass images of medical documents to the OCR module to extract and translate text.

---

## OCR Setup Instructions

MediBridge uses Optical Character Recognition (OCR) to convert medical documents and images into text for translation.

### Step 1: Install Tesseract OCR Engine

- **Windows:**  
  Download from [UB Mannheim builds](https://github.com/UB-Mannheim/tesseract/wiki) and install.  
  Add the Tesseract installation folder (e.g., `C:\Program Files\Tesseract-OCR`) to your system PATH.

- **Linux (Ubuntu/Debian):**
  ```bash
  sudo apt update
  sudo apt install tesseract-ocr
  ```

- **MacOS (Using Homebrew):**
  ```
  brew install tesseract
  ```

### Step 2: Install Python OCR Packages

```
pip install pytesseract Pillow
```

### Step 3: Verify OCR Installation

Test OCR with this python snippet

```
import pytesseract
from PIL import Image

# If Tesseract is not in your PATH, specify the full path here:
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

img = Image.open('path_to_sample_medical_image.png')
text = pytesseract.image_to_string(img)
print(text)

```

# Supported Languages & Accuracy
- English
- Tamil
- Hindi
 (expandable to other Indian languages).


- OCR tuned for medical fonts and handwriting.

# Why MediBridge?
Effective communication in healthcare is crucial. MediBridge ensures patients and doctors can understand each other clearly, regardless of language barriers, thereby improving diagnosis, treatment, and patient safety.

# Roadmap
- Add support for more languages.
- Offline translation capability.
- Integrate with Electronic Health Record (EHR) systems.
- Develop web and mobile app frontends.

# Contributors
- Deepan Sai
- Shyam Ganesh V
- Nithaesh
- Vivek
- Rohit

# Contact & Support
For questions, issues, or contributions, please open an issue or contact us via GitHub.

Thank you for using MediBridge! Bridging language gaps in healthcare, one translation at a time.









