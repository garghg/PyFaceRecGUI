#Reference: https://github.com/ageitgey/face_recognition/blob/master/examples/facerec_from_webcam_faster.py

import face_recognition
import os
import cv2
import numpy as np

class FaceRecognition:
    def __init__(self):
        self.known_face_encodings = []
        self.known_face_names = []
        self.recognizing = False  # Add a flag to track recognition status
        self.encode_faces()

        self.video_capture = cv2.VideoCapture(0)

    def encode_faces(self):
        for image in os.listdir('faces'):
            face_image = face_recognition.load_image_file(f"faces/{image}")
            image = os.path.splitext(image)
            face_encoding = face_recognition.face_encodings(face_image)[0]

            self.known_face_encodings.append(face_encoding)
            self.known_face_names.append(image[0])

    def process_frame(self):
        ret, frame = self.video_capture.read()
        if not ret:
            return None, []  # Return None and empty face names if the frame is not available

        frame = cv2.flip(frame, 1)
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = small_frame[:, :, ::-1]

        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
            name = "Unknown"

            face_distances = face_recognition.face_distance(self.known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = self.known_face_names[best_match_index]

            face_names.append(name)
        
        # Draw a rectangle around faces to show detection and recognition
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            # Scale up face locations to the original size and draw a rectangle around the detected face(s)
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            # Draw a label with a name below the face
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

        return frame, face_names

    def start_recognition(self):
        self.recognizing = True

    def stop_recognition(self):
        self.recognizing = False

    def is_recognizing(self):
        return self.recognizing

    def release_camera(self):
        self.video_capture.release()
