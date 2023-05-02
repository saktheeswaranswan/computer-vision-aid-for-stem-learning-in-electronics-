import cv2
import pandas as pd

# Read the coordinates.csv file
df = pd.read_csv('coordinates.csv', header=None)

# Prompt the user to enter the screen size
width = int(input("Enter the screen width: "))
height = int(input("Enter the screen height: "))

# Open a video capture object to capture live video stream
cap = cv2.VideoCapture(2)

# Initialize index to zero
i = 0

while True:
    # Read the next frame from the video stream
    ret, frame = cap.read()

    # Draw red blinking circle at a time
    if i < len(df)-1:
        x1 = int(df.iloc[i, 0])
        y1 = int(df.iloc[i, 1])
        x2 = int(df.iloc[i+1, 0])
        y2 = int(df.iloc[i+1, 1])
        cv2.circle(frame, (x1, y1), 10, (0, 0, 255), -1)
        cv2.circle(frame, (x2, y2), 10, (0, 0, 255), -1)
        # Display the text from the third column of the CSV file in rich yellow color
        text1 = str(df.iloc[i, 2])
        text2 = str(df.iloc[i+1, 2])
        cv2.putText(frame, text1, (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
        cv2.putText(frame, text2, (x2, y2), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

    # Resize the frame to the specified screen size
    frame = cv2.resize(frame, (width, height))

    # Display the resulting frame
    cv2.imshow('frame', frame)

    # Exit if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # Move to the next point when 'n' is pressed
    if cv2.waitKey(1) & 0xFF == ord('n'):
        i += 2
        if i >= len(df):
            i = 0

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()

