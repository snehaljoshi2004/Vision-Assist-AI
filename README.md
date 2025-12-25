# Vision Assist AI System
A real-time assistive computer vision system designed to support visually impaired users through object detection, distance estimation, stair detection, and audio-based warnings using a single camera.
The system focuses on accessibility and safety by converting visual information into meaningful speech feedback while maintaining modular and extensible system design.

---
## Overview
Vision Assist AI provides real-time environmental awareness by detecting objects, estimating their distance from the user, and issuing proximity-based audio warnings. The system supports multiple operating modes and is designed for indoor and outdoor navigation assistance.The project uses deep learning–based object detection models and runs entirely on the user’s device, enabling low-latency responses without relying on cloud-based inference.

---
## Features

- Real-time object detection using YOLO
- Two operational modes:
  - **Custom Detection Mode**
    - Detects stairs and pen
    - Supports stair counting
    - Distance estimation for detected objects
  - **Assistive Mode (COCO)**
    - Detects common everyday objects (COCO classes)
    - Distance estimation and proximity warnings
- Monocular distance estimation using a single webcam
- Audio feedback using offline text-to-speech
- Proximity-based warnings for nearby objects
- Modular and extensible architecture

---
## Technology Used
- **Programming Language**: Python
- **Deep Learning Framework**: PyTorch
- **Object Detection**: Ultralytics YOLO
- **Computer Vision**: OpenCV
- **Numerical Computing**: NumPy
- **Text-to-Speech**: pyttsx3 (offline)
- **Hardware**: Single monocular webcam

---
## Installation
### Prerequisites
- Python 3.8 or higher
- pip package manager
- Webcam (built-in or external)

---
### Setup
1. Clone the repository:
   ```bash
   git clone <repository-url>
   
2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
3. Run the application:
   ```bash
   python main.py
---
## Usage   
- 1. Run the application using python main.py
- 2. Select the operating mode:
  - **(1)Custom Detection Mode**
  - **(2)Assistive Mode** 
- 3. Allow webcam access
- 4. Listen to real-time audio feedback and proximity warnings
- 5. Press q to exit the application
---
## Supported Input
- Live webcam feed
- Indoor and outdoor environments
- Objects from COCO dataset (Assistive Mode)
- Custom-trained classes (Custom Mode)
 ---
## Results & Demonstration
Sample output images demonstrating detection and distance estimation are provided in the results/ folder.

