import cv2
import numpy as np

def count_stairs(depth_map):
    edges = cv2.Canny(depth_map.astype(np.uint8), 50, 150)

    lines = cv2.HoughLinesP(
        edges,
        rho=1,
        theta=np.pi / 180,
        threshold=100,
        minLineLength=100,
        maxLineGap=10
    )

    if lines is None:
        return 0

    stair_lines = [
        line for line in lines
        if abs(line[0][1] - line[0][3]) < 10
    ]

    return len(stair_lines)
