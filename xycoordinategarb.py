import csv
import numpy as np
import cv2

# Initialize the video capture object
cap = cv2.VideoCapture(2)

# Define the screen size
screen_size = (640, 480)

# Define the mouse callback function to get the coordinates
def get_coords(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        with open('coordinates.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow([x, y])
        print(f'Coordinates saved: {x}, {y}')
        cv2.circle(frame, (x, y), 5, (0, 0, 255), -1)

# Create a window to display the video
cv2.namedWindow("Video")

# Set the mouse callback to get_coords function
cv2.setMouseCallback("Video", get_coords)

# Start the video loop
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Resize the frame to the desired screen size
    frame = cv2.resize(frame, screen_size)

    # Display the frame
    cv2.imshow("Video", frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object
cap.release()

# Close all windows
cv2.destroyAllWindows()
