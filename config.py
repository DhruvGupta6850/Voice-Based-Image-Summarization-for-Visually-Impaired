import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

UPLOAD_FOLDER = os.path.join(BASE_DIR, "static", "uploads")
AUDIO_FOLDER = os.path.join(BASE_DIR, "static", "audio")

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}

SECRET_KEY = "secret_key"