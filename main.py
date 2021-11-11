import cv2
import numpy as np
import pytesseract as ocr
import time

ocr.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

try:
    import RPI.GPIO as gpio
except ImportError:
    print("No GPIO SUPPORT")
    from fakeGPIO import gpio

    gpio = gpio()

gpio.setmode(gpio.BCM)
gpio.setup(18, gpio.OUT)

#cap = cv2.VideoCapture('flash test.mp4')  # string for file, number for camera feed
cap = cv2.VideoCapture(1)
cap.set(3, 1920)

cap.set(4, 1080)
# Check if camera opened successfully
if cap.isOpened() == False:
    print("Error opening video stream or file")

# Read until video is completed
while cap.isOpened():
    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret and frame.shape[0] < 1000:
        print(frame.shape)
        cv2.imshow('Frame', frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
        continue
    if ret:
        bankFrame = frame[1030:1060, 1830:1870]
        locationFrame = frame[440:470, 160:300]
        ocrFrames = [bankFrame, locationFrame]
        ocrResults = []
        combined = np.concatenate(ocrFrames, 1)
        for subFrame in ocrFrames:
            gray_frame = cv2.cvtColor(subFrame, cv2.COLOR_BGR2GRAY)
            threshold = cv2.threshold(gray_frame, 200, 255, cv2.THRESH_BINARY)
            read_string = ocr.image_to_string(threshold[1])
            read_string = read_string.replace('\x0C', '')
            print(read_string)
            ocrResults += [read_string != ""]
        cv2.imshow('Frame', frame)
        if not np.any(ocrResults):
            #cv2.imwrite('flashPhotos/{}.png'.format(time.time()), frame)
            print('Flashing')
            gpio.output(18, gpio.HIGH)
        else:
            gpio.output(18, gpio.LOW)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break

# When everything done, release the video capture object
cap.release()

# Closes all the frames
cv2.destroyAllWindows()
