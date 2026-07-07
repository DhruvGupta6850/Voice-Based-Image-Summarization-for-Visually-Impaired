from flask import Flask
from config import SECRET_KEY, UPLOAD_FOLDER, AUDIO_FOLDER
from routes.main import main
import os

app = Flask(__name__)

app.config["SECRET_KEY"] = SECRET_KEY
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["AUDIO_FOLDER"] = AUDIO_FOLDER

app.register_blueprint(main)

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 3000)),
        debug=False
    )