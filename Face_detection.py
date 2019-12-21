import cv2

face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
image = cv2.imread("many-faces.jpg",1)
gray_image= cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray_image,scaleFactor=1.1,minNeighbors=5)
print(faces)

for x,y,w,h in faces:
    image = cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),3)
    
cv2.imshow("images",image)
cv2.imwrite("face-detected.jpg",image)
cv2.waitKey(2000)
cv2.destroyAllWindows()
