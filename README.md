# YOLO11 Windows Real-time Object Detection

This project implements real-time object detection using YOLO11 with webcam input on Windows. It provides an easy-to-use setup for running YOLO11 object detection on live webcam feed.

## Features

- Real-time object detection using YOLO11 (latest version with improved performance)
- Webcam integration for live video feed
- Simple and clean Python implementation
- Visual display of detection results
- Easy to quit with 'q' key

## Prerequisites

- Python 3.8 or higher
- OpenCV (cv2)
- Ultralytics YOLO11
- A working webcam

## Installation

1. Clone this repository:
```bash
git clone https://github.com/samurai-no-shogun/yolo11_windows.git
cd yolo11_windows
```

2. Install the required packages:
```bash
pip install ultralytics opencv-python
```

## Usage

1. Run the webcam detection script:
```bash
python webcam_detection.py
```

2. The script will:
   - Load the YOLO11 model (downloads the default model if not present)
   - Open your default webcam
   - Display the detection results in real-time
   - Press 'q' to quit the application

## Implementation Details

The project uses:
- `ultralytics` package for YOLO11 implementation
- `cv2` (OpenCV) for webcam handling and display
- YOLO11n model (nano version) for efficient real-time detection
- Latest YOLO11 features for improved accuracy and performance

## File Structure

- `webcam_detection.py`: Main script for real-time object detection
- `README.md`: Project documentation
- `.gitignore`: Git ignore file for Python projects

## Contributing

Feel free to open issues or submit pull requests for any improvements.

## License

This project is open source and available under the MIT License.