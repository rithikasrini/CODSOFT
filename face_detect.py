import cv2

cascade_face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def check_camera(index):
    cap = cv2.VideoCapture(index)
    if not cap.isOpened():
        print(f"Error: Could not open video capture with index {index}")
        return False
    else:
        print(f"Camera with index {index} opened successfully")
        return True

def facedet():
    if not check_camera(0):
        print("Error: Could not open video capture")
        return
    
    cap = cv2.VideoCapture(0)
    while True:
        ret, img = cap.read()
        if not ret:
            print("Error: Failed to capture frame")
            break
            
        g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        f = cascade_face.detectMultiScale(g, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        if len(f) == 0:
            print("No faces are detected.")
        else:
            for (x,y,w,h) in f:
                cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 4)
                cv2.imshow('img', img)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    # Release the capture and close windows
    cap.release()
    cv2.destroyAllWindows()

facedet()
