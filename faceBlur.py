import cv2
import mediapipe as mp

def plot_one_box(x, img):        
    try:
        # Create ROI coordinates
        topLeft = (int(x[0]), int(x[1]))
        bottomRight = (int(x[2]), int(x[3]))
        cv2.rectangle(img, topLeft, bottomRight,  (230, 0,0), thickness=1, lineType=cv2.LINE_AA)
        x, y = topLeft[0], topLeft[1]
        w, h = bottomRight[0] - topLeft[0], bottomRight[1] - topLeft[1]

        ROI = img[y:y+h, x:x+w]
        blur = cv2.GaussianBlur(ROI, (135,135), 0)

        # Insert ROI back into image
        img[y:y+h, x:x+w] = blur
    except:
        print("Error")

# resultvid = cv2.VideoWriter('DEMO.mp4',
#                          cv2.VideoWriter_fourcc(*'mp4v'),
#                          25, (1920, 1080))

mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

# For webcam input:
cap = cv2.VideoCapture(0)
with mp_face_detection.FaceDetection(
    model_selection=1, min_detection_confidence=0.4) as face_detection:
  while cap.isOpened():
    success, image = cap.read()
    #image = cv2.resize(image, (0, 0), fx=2, fy=2)
    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      continue

    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image.flags.writeable = False
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = face_detection.process(image)

    # Draw the face detection annotations on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    if results.detections:
      for detection in results.detections:
        #mp_drawing.draw_detection(image, detection)
        location_data = detection.location_data
        if location_data.format == location_data.RELATIVE_BOUNDING_BOX:
            bb = location_data.relative_bounding_box
            bb_box = [
                bb.xmin, bb.ymin,
                bb.width, bb.height,
            ]
            x1 = (bb_box[0]) * image.shape[1]
            y1 = (bb_box[1]) * image.shape[0]
            x2 = (bb_box[0] + bb_box[2]) * image.shape[1]
            y2 = (bb_box[1] + bb_box[3]) * image.shape[0]

            final_box = [x1, y1, x2, y2]
            plot_one_box(final_box, image)
            # print(f"RBBox: {bb_box}")
    # Flip the image horizontally for a selfie-view display.
    # resultvid.write(image)
    cv2.imshow('MediaPipe Face Detection', image)
    if cv2.waitKey(5) & 0xFF == 27:
      break

cap.release()
#resultvid.release()
cv2.destroyAllWindows()