from ultralytics import YOLO
import cv2
import time

def main():
    # Load the YOLO11 model (it will download the default model if not present)
    model = YOLO('yolov11n.pt')  # Using YOLO11 nano model for efficiency

    # Open the webcam (0 is usually the default USB camera)
    cap = cv2.VideoCapture(0)

    # Check if the webcam is opened correctly
    if not cap.isOpened():
        print("Error: Could not open webcam")
        return

    # Set the window name
    window_name = "YOLO11 Webcam Detection"
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)

    try:
        while True:
            # Read a frame from the webcam
            ret, frame = cap.read()
            if not ret:
                print("Error: Could not read frame")
                break

            # Run YOLO11 inference on the frame
            results = model(frame)

            # Visualize the results on the frame
            annotated_frame = results[0].plot()

            # Display the annotated frame
            cv2.imshow(window_name, annotated_frame)

            # Break the loop if 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                print("Quitting...")
                break

    finally:
        # Release the webcam and destroy all windows
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()