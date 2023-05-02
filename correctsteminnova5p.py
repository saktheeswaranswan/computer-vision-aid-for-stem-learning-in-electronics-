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

    # Draw red blinking circles for five points at a time
    if i < len(df)-4:
        for j in range(5):
            x = int(df.iloc[i+j, 0])
            y = int(df.iloc[i+j, 1])
            cv2.circle(frame, (x, y), 10, (0, 0, 255), -1)
            # Display the text from the third column of the CSV file in rich yellow color
            text = str(df.iloc[i+j, 2])
            cv2.putText(frame, text, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

    # Resize the frame to the specified screen size
    frame = cv2.resize(frame, (width, height))

    # Display the resulting frame
    cv2.imshow('frame', frame)

    # Exit if the 'q' key is pressed or window is closed
    key = cv2.waitKey(1)
    if key == ord('q') or key == 27:
        break

    # Move to the next five points when 'n' is pressed
    elif key == ord('n'):
        i += 5
        if i >= len(df)-4:
            i = 0

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()

