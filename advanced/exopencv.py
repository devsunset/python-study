# $ pip install opencv-python

''' 
import cv2
 
# case 1
img = cv2.imread('test.jpg', 1) 
cv2.imshow('Test Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('test2.png', img)


# case 2
cap = cv2.VideoCapture(0)           
#cap = cv2.VideoCapture("test.mp4") 
 
while cap.isOpened():
    success, frame = cap.read()
    if success:
        cv2.imshow('Camera Window', frame)

        key = cv2.waitKey(1) & 0xFF
        if (key == 27): 
            break
 
cap.release()
cv2.destroyAllWindows()

# case 3 
cap = cv2.VideoCapture(0); 
 
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
print("size: {0} x {1}".format(width, height))
 
fourcc = cv2.VideoWriter_fourcc(*'XVID')
writer = cv2.VideoWriter('test.avi', fourcc, 24, (int(width), int(height)))
 
while cap.isOpened():
    success, frame = cap.read()
    if success:
        writer.write(frame)  
        cv2.imshow('Video Window', frame)
 
        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break
    else:
        break
 
cap.release()
writer.release()  
cv2.destroyAllWindows()

# case 4 
from matplotlib import pyplot as plt
 
img = cv2.imread('happyfish.jpg', 1)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img)
plt.show()

'''