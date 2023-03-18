#importing libraries
import cv2
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation

# Load the video and the background image
vid = cv2.VideoCapture("video.mp4")
bg_img = cv2.imread("sample01.jpg")

# Get the size of the video frame
width = int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Resize the background image to match the video frame size
bg_img = cv2.resize(bg_img, (width, height))

# Initialize the SelfiSegmentation object
seg = SelfiSegmentation()

# Loop through the frames of the video
while True:
    # Read a frame from the video
    _, frame = vid.read()

    # Check if the frame was successfully read
    if not _:
        break

    # Remove the background from the frame using the background image
    frame_rmbg = seg.removeBG(frame, bg_img, threshold=0.8)

    # Display the resulting image
    cv2.imshow("Video", frame_rmbg)

    # Check if the user pressed the 'x' key to exit
    if cv2.waitKey(1) == ord('x'):
        break

# Release the video capture and destroy the windows
vid.release()
cv2.destroyAllWindows()
