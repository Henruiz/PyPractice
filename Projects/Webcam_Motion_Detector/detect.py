import cv2, time


vid = cv2.VideoCapture(0)

# used for vector coordinates
counter = 0

while True:
    counter = counter + 1
    check, frame = vid.read()

    # setting grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # title of the window
    cv2.imshow("Detecting...", gray)

    key = cv2.waitKey(1)
    print(gray)

    # pressing q makes the program stop
    if key == ord("q"):
        break


print(counter)
vid.release()
cv2.destroyAllWindows()

