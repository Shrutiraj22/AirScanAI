from sensors.radar_processor import load_radar_data
from sensors.vision_processor import detect_objects
from sensors.fusion_engine import fuse_data
import cv2

if __name__ == "__main__":
    radar_data = load_radar_data("data/radar_mock.csv")
    cap = cv2.VideoCapture(0)

    for i, row in radar_data.iterrows():
        ret, frame = cap.read()
        if not ret:
            break
        vision_result = detect_objects(frame)
        radar_pos = row['position']
        vision_pos = row['position'] + 2  # dummy adjustment
        fused = fuse_data(radar_pos, vision_pos)
        print("Fused Target Position:", fused[0][0])

    cap.release()
    cv2.destroyAllWindows()