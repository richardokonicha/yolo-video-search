"""
Simple app to upload a video via a web form and view the inference results on the video in the browser.
"""

import argparse
import io
# import os
import datetime
from PIL import Image

import torch
from flask import Flask, render_template, request, redirect, send_from_directory

from ultralytics import YOLO
from utils import process_video_and_label


app = Flask(__name__)

DATETIME_FORMAT = "%Y-%m-%d_%H-%M-%S-%f"


@app.route("/", methods=["GET", "POST"])
def predict():
    """Predict Upload Video"""
    if request.method == "POST":
        if "file" not in request.files:
            return redirect(request.url)
        file = request.files['file']
        label = request.values['label']

        result = process_video_and_label(file, label, model)
        return render_template("main.html", video_links=result)

    return render_template("main.html", video_links=[])


@app.route('/display/<filename>')
def display_image(filename):
    return send_from_directory('static', filename)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Flask app: Video Search")
    parser.add_argument("--port", default=5001, type=int, help="port number")
    args = parser.parse_args()

    torch.cuda.empty_cache()
    model = YOLO('yolov8n.pt')

    # debug=True cause Restarting with stats
    app.run(host="0.0.0.0", debug=True, port=args.port, use_reloader=True)
