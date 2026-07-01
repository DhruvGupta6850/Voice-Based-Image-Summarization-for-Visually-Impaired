from transformers import (
    BlipProcessor,
    BlipForConditionalGeneration
)

from PIL import Image
import torch


class CaptionService:

    def __init__(self):

        print("Loading BLIP model...")

        self.device = (
            "cuda"
            if torch.cuda.is_available()
            else "cpu"
        )

        self.processor = BlipProcessor.from_pretrained(
            "Salesforce/blip-image-captioning-base"
        )

        self.model = BlipForConditionalGeneration.from_pretrained(
            "Salesforce/blip-image-captioning-base",
            use_safetensors=True
        )

        self.model.to(self.device)

        print("BLIP Loaded Successfully!")

    def generate_caption(self, image_path):

        image = Image.open(image_path).convert("RGB")

        inputs = self.processor(
            image,
            return_tensors="pt"
        ).to(self.device)

        output = self.model.generate(**inputs)

        caption = self.processor.decode(
            output[0],
            skip_special_tokens=True
        )

        return caption


caption_service = CaptionService()