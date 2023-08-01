# Yolo Video Search

Yolo Video Search - Search through video for objects using text, find all occurrences of specific object in video.
Sure! Here's a README file for the Flask app: Video Search project.

---

# Flask App: Video Search

This is a Flask web application that allows users to upload a video, perform object detection on the video using YOLO, and view the results on the video in the browser. The app uses the Ultralytics YOLO implementation for object detection.

## Requirements

- Python 3.x
- Flask
- Ultralytics YOLO
- OpenCV
- Numpy
- Pillow

Install the required packages using the following command:

```bash
pip install -r requirements.txt
```

## How to Run

To run the Flask app, execute the following command:

```bash
python app.py --port <PORT_NUMBER>
```

```
make run
```

Replace `<PORT_NUMBER>` with the desired port number (default is 5001).

## Usage

1. Start the Flask app using the above command.
2. Open your web browser and go to `http://localhost:<PORT_NUMBER>/` (replace `<PORT_NUMBER>` with the actual port number used).
3. Upload a video file using the provided form and specify a label for object detection.
4. Click the "Submit" button to process the video and view the results.
5. The app will detect the specified objects in the video, draw bounding boxes around them, and display the video with the detection results.

## File Structure

- `app.py`: The main Flask application file that handles routes and runs the app.
- `utils.py`: Contains the function for processing the video and performing object detection.
- `static/`: Directory to store the saved video clips.
- `templates/`: Directory containing the HTML templates for rendering the web pages.

## Acknowledgments

This app uses the Ultralytics YOLO implementation for object detection. The Ultralytics YOLO repository can be found at: https://github.com/ultralytics/yolov5

## License

This project is licensed under the MIT License - see the LICENSE file for details.
