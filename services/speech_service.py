import asyncio
import os
import edge_tts


class SpeechService:

    VOICE = "en-US-AriaNeural"

    async def _generate(self, text, output_path):
        communicate = edge_tts.Communicate(text, self.VOICE)
        await communicate.save(output_path)

    def text_to_speech(self, text):

        os.makedirs("static/audio", exist_ok=True)

        output_path = os.path.join(
            "static",
            "audio",
            "summary.mp3"
        )

        asyncio.run(
            self._generate(text, output_path)
        )

        return output_path


speech_service = SpeechService()