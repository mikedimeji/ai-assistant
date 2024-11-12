from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QMovie

class AnimationManager(QLabel):
    def __init__(self, gif_path):
        super().__init__()
        self.movie = QMovie(gif_path)
        self.setMovie(self.movie)

    def start_animation(self):
        self.movie.start()

    def stop_animation(self):
        self.movie.stop()
