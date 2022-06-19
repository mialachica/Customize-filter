import cv2
import numpy as np
import random

# Opens the camera 
video = cv2.VideoCapture(1)

# Allows for the user to input what they want on their head
user_write = input("\nWelcome to filter maker!\n\t- You can only write a 10 Character phrase\n\nWhat do you want to write: " + "")


# setup text
font = cv2.FONT_HERSHEY_COMPLEX

# get boundary of this text
textsize = cv2.getTextSize(user_write, font, 1, 2)[0]

while True:
    check, frame = video.read()
    
    # Flips the camera
    camera = cv2.flip(frame, 1)

    # Inputs the facial detection to the code
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    # Sets the scale for the face dection to be able to read the camera screen
    faces =  face_cascade.detectMultiScale(frame,
                                            scaleFactor = 1.05,
                                            minNeighbors=5)
    
    # Sets different variables to the size of the faces decected
    for x, y, w, h in faces:
        
        # Puts the text onto the users face
        cv2.putText(camera, user_write, (x, y), font, 1, (255, 255, 255), 2)

    # Creates the name for the camera window and displays the program in use as a filter 
    cv2.imshow('Custom filter', camera)

    # Allows for the 'q' key to close the program and for the 's' key to screenshot a picture of the user using the filter
    if cv2.waitKey(1) == ord('q'):
        break
    elif cv2.waitKey(1) == ord('s'):
            cv2.imwrite("Custom_filter.jpg", camera)

# releases the programs access to the camera
video.release()

# Closes all the windows and shuts off the entire program
cv2.destroyAllWindows