from ultralytics import YOLO


class ObjectDetectionService:

    def __init__(self):

        print("Loading YOLOv8...")

        self.model = YOLO("yolov8n.pt")

        print("YOLO Loaded Successfully!")

    def detect_objects(self, image_path):

        results = self.model(image_path)

        detected = []

        for result in results:

            for box in result.boxes:

                cls = int(box.cls[0])

                detected.append(
                    self.model.names[cls]
                )

        return list(set(detected))


object_detection_service = ObjectDetectionService()