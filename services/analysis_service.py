from services.caption_service import caption_service
from services.ocr_service import ocr_service
from services.object_detection_service import object_detection_service
from services.summary_service import summary_service


class AnalysisService:

    def analyze_image(self, image_path):

        caption = caption_service.generate_caption(image_path)

        text = ocr_service.extract_text(image_path)

        objects = object_detection_service.detect_objects(image_path)

        summary = summary_service.generate_summary(
        caption,
        objects,
        text
        )

        return {
            "caption": caption,
            "text": text,
            "objects": objects,
            "summary": summary
        }


analysis_service = AnalysisService()