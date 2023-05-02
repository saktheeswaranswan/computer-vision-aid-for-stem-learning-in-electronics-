import csv
import numpy as np
import cv2

# Define the screen size
screen_size = (640, 480)

# Load the coordinates from the CSV file
with open('coordinates.csv', 'r') as f:
    reader = csv.reader(f)
    coordinates = [[int(row[0]), int(row[1])] for row in reader]

# Create a window to display the video
cv2.namedWindow("Video")

# Initialize the point index and the number of points to plot
point_index = 0
num_points_to_plot = 0

# Define the keyboard callback function to change the number of points to plot
def on_keyboard_event(event, x, y, flags, param):
    global num_points_to_plot
    if event == cv2.EVENT_KEYDOWN:
        if chr(event & 0xFF) == 'n':
            point_index += 1
            if point_index > len(coordinates):
                point_index = 1
            print(f'Point {point_index}: ({coordinates[point_index-1][0]}, {coordinates[point_index-1][1]})')
        elif chr(event & 0xFF) == 'p':
            num_points_to_plot = int(input('How many points to plot: '))

# Set the keyboard callback to on_keyboard_event function
cv2.setMouseCallback("Video", on_keyboard_event)

# Initialize the video capture object
cap = cv2.VideoCapture(2)

# Start the video loop
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Resize the frame to the desired screen size
    frame = cv2.resize(frame, screen_size)

    # Plot the specified number of red circles on the live video stream
    for i in range(num_points_to_plot):
        if point_index+i <= len(coordinates):
            cv2.circle(frame, (coordinates[point_index+i-1][0], coordinates[point_index+i-1][1]), 5, (0, 0, 255), -1)

    # Display the frame
    cv2.imshow("Video", frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object
cap.release()

# Close all windows
cv2.destroyAllWindows()

