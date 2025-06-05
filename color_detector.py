import cv2
import pandas as pd

with open('colors.csv', 'r', encoding='utf-8') as f:
    color_data = pd.read_csv(f)

def getColorName(R, G, B):
    min_dist = float('inf')
    cname = ""
    for i in range(len(color_data)):
        d = abs(R - int(color_data.loc[i, "R"])) + abs(G - int(color_data.loc[i, "G"])) + abs(B - int(color_data.loc[i, "B"]))
        if d < min_dist:
            min_dist = d
            cname = color_data.loc[i, "color_name"]
    return cname

cap = cv2.VideoCapture(0)
cv2.namedWindow('Detector de Cores em Tempo Real')

while True:
    ret, frame = cap.read()
    if not ret:
        break

    h, w, _ = frame.shape
    cx = w // 2 
    cy = h // 2 
    size = 30  

    roi = frame[cy-size:cy+size, cx-size:cx+size]
    avg_color = roi.mean(axis=0).mean(axis=0)  
    b, g, r = [int(c) for c in avg_color]

    color_name = getColorName(r, g, b)

    # Desenha a área e o nome da cor
    cv2.rectangle(frame, (cx-size, cy-size), (cx+size, cy+size), (255, 255, 255), 1)
    cv2.rectangle(frame, (20, 20), (750, 60), (b, g, r), -1)
    text = f'{color_name}  R={r} G={g} B={b}'
    cv2.putText(frame, text, (30, 50), 2, 0.8, (255, 255, 255) if r+g+b < 600 else (0, 0, 0), 2)

    cv2.imshow("Detector de Cores em Tempo Real", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
