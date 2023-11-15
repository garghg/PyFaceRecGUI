# PyFaceRecGUI
Real-time face recognition via webcam using Python's face_recognition library and a PyQt5-based GUI for user-friendly controls. Start, stop, and visualize face recognition results easily.


## Recognize and Detect Multiple Faces

## Files

### face_recognition_module.py
Contains the face recognition logic utilizing the face_recognition library to recognize faces through a webcam.

### gui_rec.py
Implements the GUI using PyQt5 to create a user interface for the face recognition functionality.

## Setup

To run the application, follow these steps:

1. Install the required libraries: face_recognition, numpy, cv2, and PyQt5.
   
2. Install Python 3.9.0 on your system.

3. Run face_recognition_module.py and then run gui_rec.py to run the face recognition code and the GUI respectively.

## Usage

1. Run face_recognition_module.py to load the face recognition code in memory for GUI to use.

2. Run gui_rec.py to launch the PyQt5-based GUI for controlling the face recognition app.

3. Use the GUI buttons to start or stop face recognition and exit the app.

## Dependencies

- face_recognition
- numpy
- cv2
- PyQt5

## Notes

- Ensure you have a folder named faces containing images of faces for recognition. (*One image per person should be enough*)
- The GUI allows users to start and stop the recognition process.

## Credits

- The face recognition logic is based on [ageitgey's face_recognition library](https://github.com/ageitgey/face_recognition).
- The PyQt5 GUI functionality is based on the official PyQt documentation.


**_Feel free to contribute, report issues, or suggest improvements!_**
