from flask import Blueprint, render_template, request, redirect, current_app
from services.caption_service import caption_service
from werkzeug.utils import secure_filename
import os
from services.ocr_service import ocr_service

main = Blueprint("main", __name__)


def allowed_file(filename):
    allowed_extensions = {"png", "jpg", "jpeg"}

    return "." in filename and \
           filename.rsplit(".", 1)[1].lower() in allowed_extensions


@main.route("/", methods=["GET", "POST"])
def home():

    image_name = None
    caption = None
    ocr_text = None

    if request.method == "POST":

        if "image" not in request.files:
            return redirect(request.url)

        file = request.files["image"]

        if file.filename == "":
            return redirect(request.url)

        if file and allowed_file(file.filename):

            filename = secure_filename(file.filename)

            save_path = os.path.join(
                current_app.config["UPLOAD_FOLDER"],
                filename
            )

            file.save(save_path)

            caption = caption_service.generate_caption(save_path)
            ocr_text = ocr_service.extract_text(save_path)

            image_name = filename

    return render_template(
    "index.html",
    image_name=image_name,
    caption=caption,
    ocr_text=ocr_text
)