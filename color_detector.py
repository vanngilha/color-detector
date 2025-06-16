import cv2
import pandas as pd

# Load the color data
color_data = pd.read_csv('colors.csv', encoding='utf-8')

# Load the logo (resize if necessary)
logo = cv2.imread('assets/harvard_logo.png', cv2.IMREAD_UNCHANGED)
logo = cv2.resize(logo, (50, 50))

# Function to get the closest color name based on RGB values
def getColorName(R, G, B):
    min_dist = float('inf')
    cname = ""
    for i in range(len(color_data)):
        d = abs(R - int(color_data.loc[i, "R"])) + abs(G - int(color_data.loc[i, "G"])) + abs(B - int(color_data.loc[i, "B"]))
        if d < min_dist:
            min_dist = d
            cname = color_data.loc[i, "color_name"]
    return cname

# Function to overlay images with alpha channel
def overlay_image(bg, fg, x, y):
    h, w = fg.shape[:2]
    if fg.shape[2] == 4:  # image with alpha channel
        alpha_fg = fg[:, :, 3] / 255.0
        alpha_bg = 1.0 - alpha_fg
        for c in range(0, 3):
            bg[y:y+h, x:x+w, c] = (alpha_fg * fg[:, :, c] + alpha_bg * bg[y:y+h, x:x+w, c])
    else:
        bg[y:y+h, x:x+w] = fg[:, :, :3]
    return bg

# Webcam
cap = cv2.VideoCapture(0)
cv2.namedWindow('Real-Time Color Detector')

while True:
    ret, frame = cap.read()
    if not ret:
        break

    h, w, _ = frame.shape
    cx, cy = w // 2, h // 2
    size = 30

    # Region of interest (center square)
    roi = frame[cy-size:cy+size, cx-size:cx+size]
    avg_color = roi.mean(axis=0).mean(axis=0)
    b, g, r = [int(c) for c in avg_color]
    color_name = getColorName(r, g, b)
    hex_color = '#{:02X}{:02X}{:02X}'.format(r, g, b)

    # Transparent panel
    panel_w, panel_h = 400, 50
    panel_x = (w - panel_w) // 2
    panel_y = 20
    overlay = frame.copy()
    cv2.rectangle(overlay, (panel_x, panel_y), (panel_x + panel_w, panel_y + panel_h), (b, g, r), -1)
    alpha = 0.6
    frame = cv2.addWeighted(overlay, alpha, frame, 1 - alpha, 0)

    # Text
    text = f'{color_name}  RGB({r}, {g}, {b})  HEX: {hex_color}'
    text_size, _ = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 0.8, 2)
    text_x = (w - text_size[0]) // 2
    text_color = (255, 255, 255) if r+g+b < 600 else (0, 0, 0)
    shadow_color = (0, 0, 0) if r+g+b > 600 else (255, 255, 255)
    cv2.putText(frame, text, (text_x + 1, panel_y + 35), cv2.FONT_HERSHEY_SIMPLEX, 0.8, shadow_color, 2)
    cv2.putText(frame, text, (text_x, panel_y + 34), cv2.FONT_HERSHEY_SIMPLEX, 0.8, text_color, 2)

    # Center rectangle
    cv2.rectangle(frame, (cx-size, cy-size), (cx+size, cy+size), (255, 255, 255), 2)

    # Color thumbnail
    cv2.rectangle(frame, (20, h-60), (100, h-20), (b, g, r), -1)
    cv2.putText(frame, color_name, (110, h-30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, text_color, 2)

    # Add logo
    frame = overlay_image(frame, logo, 20, 20)
    cv2.imshow("Real-Time Color Detector", frame)

    # Exit on ESC key
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
