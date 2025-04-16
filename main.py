from video_utils import extract_frames
from ocr_utils import detect_plates

VIDEO_PATH = 'sample_videos/example1.mp4'

print("Extracting frames...")
frames = extract_frames(VIDEO_PATH, every_n_frames=30)

print("Running OCR...")
for i, frame in enumerate(frames):
    plates = detect_plates(frame)
    if plates:
        print(f"[Frame {i}] Detected plates: {plates}")
