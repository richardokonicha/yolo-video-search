from werkzeug.utils import secure_filename
import cv2
import numpy as np
import config
import os


def process_video_and_label(file, label, model):
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(config.UPLOAD_FOLDER, filename)
        file.save(filepath)

        clip_num = 0
        clip_frames = []
        SAVE_INTERVAL = 300  # Number of frames between each saved clip
        saved_video_links = []  # List to store the links to saved video clips

        cap = cv2.VideoCapture(filepath)
        try:
            frame_num = 0
            while cap.isOpened():
                success, frame = cap.read()

                if not success:
                    break

                frame_num += 1

                # Skip frames if needed (e.g., only process every 10th frame)
                if frame_num % 10 != 0:
                    continue

                # Resize the frame to a smaller size (optional)
                resized_frame = cv2.resize(frame, (640, 480))

                results = model(resized_frame, conf=0.5, verbose=False)
                for box in results[0].boxes:
                    result_label = results[0].names[box.cls[0].item()]
                    conf = round(box.conf[0].item(), 2)
                    res = {
                        "Object type": label,
                        "Probability": conf
                    }
                    print(res)

                    if label == result_label:
                        x, y, w, h = map(int, box.xyxy[0].tolist())

                        # Draw the bounding box
                        cv2.rectangle(resized_frame, (x, y),
                                      (w, h), (0, 0, 255), 2)

                        # Calculate label text size and position
                        label_text = f'{label} ({conf}%)'
                        label_font = cv2.FONT_HERSHEY_SIMPLEX
                        label_font_scale = 0.8
                        label_font_thickness = 2

                        (label_width, label_height), _ = cv2.getTextSize(
                            label_text, label_font, label_font_scale, label_font_thickness)

                        label_x = x
                        label_y = y - 10

                        # Draw the label text
                        cv2.rectangle(
                            resized_frame, (x, y), (x + label_width, y - label_height - 10), (0, 0, 255), -1)
                        cv2.putText(resized_frame, label_text, (label_x, label_y), label_font,
                                    label_font_scale, (255, 255, 255), label_font_thickness, cv2.LINE_AA)

                        clip_frames.append(resized_frame.copy())
                        print(f"Found {label} in frame {frame_num}")

                if len(clip_frames) >= SAVE_INTERVAL:
                    save_path = save_clip(clip_num, clip_frames)
                    saved_video_links.append(save_path)
                    clip_num += 1
                    clip_frames.clear()

            if clip_frames:
                save_path = save_clip(clip_num, clip_frames)
                saved_video_links.append(save_path)

            print("Reached the end of the video.")
        finally:
            cap.release()

        return saved_video_links

    return []


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in config.ALLOWED_EXTENSIONS


def save_clip(clip_num, clip_frames):
    clip_num += 1
    save_path = secure_filename(f"clip_{clip_num}.mp4")
    save_path = os.path.join(config.UPLOAD_FOLDER, save_path)

    out = cv2.VideoWriter(save_path, cv2.VideoWriter_fourcc(
        *'h264'), 15, (clip_frames[0].shape[1], clip_frames[0].shape[0]))

    for clip_frame in clip_frames:
        out.write(clip_frame)
    out.release()
    print(f"Saved {save_path}")
    return save_path
