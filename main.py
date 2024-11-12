# main.py
from src.gui.gui_manager import GUIManager
from src.core.text_processor import TextProcessor
from src.core.voice_manager import VoiceManager

class MainApp:
    def __init__(self):
        self.gui = GUIManager()
        self.text_processor = TextProcessor()
        self.voice_manager = VoiceManager()

    def run(self):
        # Placeholder for integrating future events, like button clicks for interaction
        input_text = "Hello, this is a test!"
        processed_text = self.text_processor.process_text(input_text)
        self.voice_manager.speak(processed_text)
        print(processed_text)

if __name__ == "__main__":
    app = MainApp()
    app.run()
