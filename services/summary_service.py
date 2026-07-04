class SummaryService:

    def generate_summary(self, caption, objects, ocr_text):

        summary = caption.strip()

        # Remove duplicate objects
        unique_objects = []

        caption_lower = caption.lower()

        for obj in objects:
            if obj.lower() not in caption_lower:
                unique_objects.append(obj)

        if unique_objects:
            summary += "\n\nObjects detected: "
            summary += ", ".join(unique_objects)

        if ocr_text.strip():
            summary += f"\n\nText in image: {ocr_text}"

        return summary


summary_service = SummaryService()