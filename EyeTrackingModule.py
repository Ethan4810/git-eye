from cv2 import cv2
import mediapipe as mp
import pyautogui

# circle variables
circleRadius1 = 3
circleRadius2 = 16
circleRadius3 = 9

# font variables
fontSize1 = 1.5
fontThickness1 = 2  # integer only
fontSize2 = 2.5
fontThickness2 = 3  # integer only

# line variables
lineThickness1 = 2
lineThickness2 = 4

# color variables
red = (0, 0, 255)
green = (0, 255, 0)
blue = (255, 0, 0)
yellow = (0, 255, 255)
white = (255, 255, 255)
purple = (255, 0, 255)

cam = cv2.VideoCapture(0)
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
screen_w, screen_h = pyautogui.size()

while True:
    _, frame = cam.read()
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = face_mesh.process(rgb_frame)
    landmark_points = output.multi_face_landmarks
    frame_h, frame_w, _ = frame.shape

    if landmark_points:
        landmarks = landmark_points[0].landmark
        for id, landmark in enumerate(landmarks[474:478]):
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), circleRadius1, green)

            if id == 1:
                screen_x = screen_w * landmark.x
                screen_y = screen_h * landmark.y

                pyautogui.moveTo(screen_x, screen_y)
        left = [landmarks[145], landmarks[159]]

        for landmark in left:
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), circleRadius1, yellow)

        if (left[0].y - left[1].y) < 0.004:
            pyautogui.click()
            pyautogui.sleep(0.1)

    cv2.imshow('Eye Controlled Mouse', frame)
    if cv2.waitKey(1) == ord('q'):
        break
