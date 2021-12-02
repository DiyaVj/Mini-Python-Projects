import cv2
import numpy as np
import pyautogui
Resolution = (1920,1080) # Specify resolution
codec = cv2.VideoWriter_fourcc(*"XVID") # Specify video codec
Filename = "ScreenRecording.avi" # Name of output file
fps = 60.0 # frame rate
output = cv2.VideoWriter(Filename,codec,fps,Resolution) # Creating a VideoWriter object
cv2.namedWindow("Live", cv2.WINDOW_NORMAL) # Create an Empty Window
cv2.resizeWindow("Live", 480, 270) # Resize the window

while True:
    Image = pyautogui.screenshot()
    frame = np.array(Image)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    output.write(frame)
    cv2.imshow("Live",frame)
    if cv2.waitKey(1) == ord('q'):
        break

output.release()
cv2.destroyAllWindows()
