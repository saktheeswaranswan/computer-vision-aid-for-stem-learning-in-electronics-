import cv2
import pandas as pd

# Read the coordinates.csv file
df = pd.read_csv('coordinates.csv', header=None)

# Open a video capture object to capture live video stream
cap = cv2.VideoCapture(0)

while True:
    # Read the next frame from the video stream
    ret, frame = cap.read()

    # Draw a red blinking circle at each specified coordinate
    for i in range(len(df)):
        x = int(df.iloc[i, 0])
        y = int(df.iloc[i, 1])
        cv2.circle(frame, (x, y), 10, (0, 0, 255), -1)
        # Display the text from the third column of the CSV file in rich yellow color
        text = str(df.iloc[i, 2])
        cv2.putText(frame, text, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

    # Display the resulting frame
    cv2.imshow('frame', frame)

    # Exit if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()

