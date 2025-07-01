import numpy as np

class KalmanFilter:
    def __init__(self):
        self.x = np.zeros((2, 1))  # position, velocity
        self.P = np.eye(2)
        self.F = np.array([[1, 1], [0, 1]])
        self.Q = np.eye(2) * 0.01
        self.H = np.array([[1, 0]])
        self.R = np.array([[1]])

    def update(self, z):
        # Predict
        self.x = self.F @ self.x
        self.P = self.F @ self.P @ self.F.T + self.Q
        # Update
        y = z - self.H @ self.x
        S = self.H @ self.P @ self.H.T + self.R
        K = self.P @ self.H.T @ np.linalg.inv(S)
        self.x += K @ y
        self.P = (np.eye(2) - K @ self.H) @ self.P
        return self.x