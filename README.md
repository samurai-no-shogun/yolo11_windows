# YOLOv8 Windows Webcam Object Detection

This project implements real-time object detection using YOLOv8 with a USB webcam on Windows. It uses the Ultralytics YOLOv8 implementation for efficient and accurate object detection.

## Setup

1. Install the required package:
```bash
pip install ultralytics
```

2. The project includes:
- `webcam_detection.py`: Main script for real-time webcam object detection
- `yolov8n.pt`: YOLOv8 nano model weights (downloaded automatically on first run)

## Usage

Run the webcam detection script:
```bash
python webcam_detection.py
```

- Press 'q' to quit the application
- The application will show real-time object detection with bounding boxes and labels

## Features

- Real-time object detection using YOLOv8
- Support for multiple object classes
- Display of detection confidence scores
- Optimized for CPU usage