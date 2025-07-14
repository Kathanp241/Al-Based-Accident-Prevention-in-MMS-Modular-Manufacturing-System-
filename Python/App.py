import cv2
import mediapipe as mp
import serial
import time

# Arduino Serial COM port
arduino = serial.Serial('COM3', 9600, timeout=1)
time.sleep(2)

# Initialize MediaPipe
mp_drawing = mp.solutions.drawing_utils
mp_face = mp.solutions.face_mesh
mp_hands = mp.solutions.hands
mp_pose = mp.solutions.pose

face_mesh = mp_face.FaceMesh()
hands = mp_hands.Hands()
pose = mp_pose.Pose()

# Define Danger Line
DANGER_LINE_Y = 300  # Adjust this based on camera view

# Camera input
cap = cv2.VideoCapture(0)

last_state = None

def send_command(cmd):
    arduino.write(f"{cmd}\n".encode())
    print(f"[ARDUINO] {cmd}")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    height, width, _ = frame.shape

    # Draw the danger line (horizontal)
    cv2.line(frame, (0, DANGER_LINE_Y), (width, DANGER_LINE_Y), (0, 0, 255), 2)
    cv2.putText(frame, "Danger Line", (10, DANGER_LINE_Y - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

    # Process landmarks
    face_result = face_mesh.process(rgb)
    hands_result = hands.process(rgb)
    pose_result = pose.process(rgb)

    danger = False

    # Check face mesh
    if face_result.multi_face_landmarks:
        for face_landmarks in face_result.multi_face_landmarks:
            for lm in face_landmarks.landmark:
                y = int(lm.y * height)
                if y > DANGER_LINE_Y:
                    danger = True
                    break
            mp_drawing.draw_landmarks(frame, face_landmarks, mp_face.FACEMESH_CONTOURS)

    # Check hand mesh
    if hands_result.multi_hand_landmarks:
        for hand_landmarks in hands_result.multi_hand_landmarks:
            for lm in hand_landmarks.landmark:
                y = int(lm.y * height)
                if y > DANGER_LINE_Y:
                    danger = True
                    break
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    # Check pose points
    if pose_result.pose_landmarks:
        for lm in pose_result.pose_landmarks.landmark:
            y = int(lm.y * height)
            if y > DANGER_LINE_Y:
                danger = True
                break
        mp_drawing.draw_landmarks(frame, pose_result.pose_landmarks, mp_pose.POSE_CONNECTIONS)

    # Send command to Arduino
    if danger and last_state != "STOP":
        send_command("STOP")
        last_state = "STOP"
        cv2.putText(frame, "ALERT: STOP!", (20, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 3)
    elif not danger and last_state != "START":
        send_command("START")
        last_state = "START"

    # Show video
    cv2.imshow("MediaPipe Danger Line", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
