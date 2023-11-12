import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QHBoxLayout
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt
import cv2
from face_recognition_module import FaceRecognition

class FaceRecognitionApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Face Recognition App")
        self.setGeometry(100, 100, 1280, 720)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.init_ui()

        # Initialize face recognition
        self.face_recognition = FaceRecognition()

        # Create a button to start the recognition
        self.start_button = QPushButton("Start Recognition", self)
        self.start_button.clicked.connect(self.start_recognition)

        # Create a button to stop the recognition
        self.stop_button = QPushButton("Stop Recognition", self)
        self.stop_button.clicked.connect(self.stop_recognition)
        self.stop_button.setEnabled(False)

        # Create an exit button
        self.exit_button = QPushButton("Exit", self)
        self.exit_button.clicked.connect(self.close)

        self.video_frame = QLabel(self)

        layout = QVBoxLayout()
        button_layout = QHBoxLayout()  # Create a horizontal layout for the buttons

        # Add buttons to the horizontal layout
        button_layout.addWidget(self.start_button)
        button_layout.addWidget(self.stop_button)
        button_layout.addWidget(self.exit_button)

        # Add the horizontal layout to the vertical layout
        layout.addLayout(button_layout)

        # Center the video frame horizontally using a separate layout
        video_frame_layout = QHBoxLayout()
        video_frame_layout.addWidget(self.video_frame)

        video_frame_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Set alignment to center

        layout.addLayout(video_frame_layout)
        self.central_widget.setLayout(layout)

        self.video_timer = QTimer(self)
        self.video_timer.timeout.connect(self.update_video_frame)

    def init_ui(self):
        self.show()

    def start_recognition(self):
        # Disable the start button and enable the stop button
        self.start_button.setEnabled(False)
        self.stop_button.setEnabled(True)

        if not self.face_recognition.is_recognizing():  # Check if recognition is not already active
            self.face_recognition.start_recognition()
            self.video_timer.start(1)  # Start the timer

    def stop_recognition(self):
        # Stop face recognition
        self.video_timer.stop()
        self.face_recognition.stop_recognition()

        # Enable the start button and disable the stop button
        self.start_button.setEnabled(True)
        self.stop_button.setEnabled(False)

    def update_video_frame(self):
        frame, face_names = self.face_recognition.process_frame()
        if frame is not None:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            height, width, _ = frame.shape
            bytes_per_line = 3 * width
            q_image = QImage(frame.data, width, height, bytes_per_line, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(q_image)
            self.video_frame.setPixmap(pixmap)

            # Display recognized face names
            if face_names:
                self.setWindowTitle(f"Face Recognition App - Recognized: {', '.join(face_names)}")
            else:
                self.setWindowTitle("Face Recognition App")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FaceRecognitionApp()
    sys.exit(app.exec_())
