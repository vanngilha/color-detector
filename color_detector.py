import cv2
import pandas as pd

color_data = pd.read_csv('colors.csv')

def getColorName(R, G, B):
    min_dist = float('inf')
    cname = ""
    for i in range(len(color_data)):
        d = abs(R - int(color_data.loc[i, "R"])) + abs(G - int(color_data.loc[i, "G"])) + abs(B - int(color_data.loc[i, "B"]))
        if d < min_dist:
            min_dist = d
            cname = color_data.loc[i, "color_name"]
    return cname

clicked = False
r = g = b = xpos = ypos = 0

def drawFunction(event, x, y, flags, param):
    global b, g, r, xpos, ypos, clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        clicked = True
        xpos = x
        ypos = y
        b, g, r = frame[y, x]
        b = int(b)
        g = int(g)
        r = int(r)

cap = cv2.VideoCapture(0)
cv2.namedWindow('Detector de Cores')
cv2.setMouseCallback('Detector de Cores', drawFunction)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    if clicked:
        cv2.rectangle(frame, (20, 20), (750, 60), (b, g, r), -1)
        text = getColorName(r, g, b) + f' R={r} G={g} B={b}'
        cv2.putText(frame, text, (30, 50), 2, 0.8, (255, 255, 255) if r+g+b < 600 else (0, 0, 0), 2)

    cv2.imshow("Detector de Cores", frame)
    
    if cv2.waitKey(1) & 0xFF == 27: 
        break

cap.release()
cv2.destroyAllWindows()
