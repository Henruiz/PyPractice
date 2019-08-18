import cv2, time, pandas
from datetime import datetime

first_frame=None
status_list=[None,None]
times=[]
df=pandas.DataFrame(columns=["Start","End"])

video=cv2.VideoCapture(0)

while True:
#    setting frame and check variables
    check, frame = video.read()
    status = 0
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) # converting frame to gray
    # 21,21 is the height and width of the image & making it blurry
    gray = cv2.GaussianBlur(gray,(21,21),0)

#    Making 1st frame gray
    if first_frame is None:
        first_frame = gray
        continue

    delta_frame = cv2.absdiff(first_frame,gray) # comparing 1st frame to gray frame
    thresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1] # using thresh hold binary

#   DILATING the image by 2 layers at a time; used for smoothing white areas
    thresh_frame = cv2.dilate(thresh_frame, None, iterations = 2)


# Showing types of frames
    cv2.imshow("Gray Frame", gray)
    cv2.imshow("Delta Frame", delta_frame)
    cv2.imshow("Threshold Frame", thresh_frame)
    cv2.imshow("Color Frame", frame)

    key=cv2.waitKey(1)

# continue show unless q is pressed to quit the program
    if key == ord('q'):
        if status == 1:
            times.append(datetime.now())
        break

print(status_list)
print(times)

# saving my times in a csv file for data collection
for i in range(0, len(times), 2):
    df = df.append({"Start":times[i], "End":times[i+1]}, ignore_index=True)

df.to_csv("Times.csv")

video.release()
cv2.destroyAllWindows
