from flask import Flask
from config import SECRET_KEY, UPLOAD_FOLDER, AUDIO_FOLDER
from routes.main import main

app = Flask(__name__)

app.config["SECRET_KEY"] = SECRET_KEY
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["AUDIO_FOLDER"] = AUDIO_FOLDER

app.register_blueprint(main)

if __name__ == "__main__":
    app.run(debug=True)