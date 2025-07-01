from utils.kalman_filter import KalmanFilter

kf = KalmanFilter()

def fuse_data(radar_pos, vision_pos):
    avg_pos = (radar_pos + vision_pos) / 2
    filtered = kf.update(avg_pos)
    return filtered
