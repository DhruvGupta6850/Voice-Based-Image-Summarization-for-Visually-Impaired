---
title: Voice-Based Image Summarization
emoji: 👁️
colorFrom: blue
colorTo: indigo
sdk: docker
pinned: false
---

# Voice-Based Image Summarization for Visually Impaired

This project uses AI to analyze an uploaded image and provide:

- 🖼️ Image Captioning (BLIP)
- 🔍 Object Detection (YOLOv8)
- 📝 OCR Text Extraction (EasyOCR)
- 📖 Intelligent Summary
- 🔊 Text-to-Speech using Edge-TTS

Built with:
- Flask
- Transformers (BLIP)
- Ultralytics YOLOv8
- EasyOCR
- Edge-TTS

Upload an image and the application will generate a natural language description along with spoken audio.