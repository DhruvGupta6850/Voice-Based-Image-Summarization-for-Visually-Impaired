# 🎙️ Voice-Based Image Summarization for Visually Impaired

An AI-powered web application that helps visually impaired users understand images by generating a natural language summary and converting it into speech.

The application combines Image Captioning, Object Detection, Optical Character Recognition (OCR), and Text-to-Speech (TTS) to describe the contents of an uploaded image.

---

## 📌 Features

- 🖼️ Upload any image
- 🤖 Generate image captions using BLIP
- 🎯 Detect multiple objects using YOLOv8
- 📝 Extract text from images using EasyOCR
- 📄 Generate a meaningful image summary
- 🔊 Convert the summary into speech using Edge-TTS
- 🌐 Simple and user-friendly Flask web interface

---


## 🏗️ Tech Stack

### Backend

- Python 3.11
- Flask

### AI Models

- BLIP (Image Captioning)
- YOLOv8 (Object Detection)
- EasyOCR (Text Recognition)
- Edge-TTS (Speech Synthesis)

### Libraries

- Transformers
- PyTorch
- Ultralytics
- OpenCV
- Pillow

---

## 📂 Project Structure

```
voice-image-summarizer/
│
├── app.py
├── config.py
├── requirements.txt
├── README.md
│
├── routes/
│   └── main.py
│
├── services/
│   ├── analysis_service.py
│   ├── caption_service.py
│   ├── object_detection_service.py
│   ├── ocr_service.py
|   ├── speech_service.py
│   └── summary_service.py
│   
├── templates/
│
├── static/
│   ├── css/
│   ├── uploads/
│   └── audio/
│
├── sample_images/
│
└── .gitignore
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Voice-Based-Image-Summarization-for-Visually-Impaired.git

cd Voice-Based-Image-Summarization-for-Visually-Impaired
```

### Create a virtual environment

#### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

#### macOS/Linux

```bash
python3 -m venv venv

source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
python app.py
```

Open your browser and visit

```
http://127.0.0.1:5000
```

---

## 🧠 How It Works

1. User uploads an image.
2. BLIP generates an image caption.
3. YOLOv8 detects all visible objects.
4. EasyOCR extracts any text present in the image.
5. The Analysis Service combines all AI outputs into a meaningful summary.
6. Edge-TTS converts the summary into speech.
7. The web application displays the summary and plays the generated audio.

---

## 📌 Future Improvements

- Voice command support
- Multilingual summaries
- Real-time camera input
- Mobile application
- Cloud deployment
- User authentication
- History of analyzed images

---

## 👨‍💻 Author

**Dhruv Gupta**

GitHub: https://github.com/DhruvGupta6850

LinkedIn: *(Add your LinkedIn profile link here)*

---

## ⭐ If you like this project

Please consider giving it a ⭐ on GitHub.