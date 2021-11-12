import cv2
face_cascade=cv2.CascadeClassifier("harrcascade_frontalface_default.xml")
# reading as color
img=cv2.imread("photo.jpg")
# best to do facial reconition as gray scale
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# find coordinates for face in image
faces=face_cascade.detectMultiScale(gray_img,scaleFactor=1.05,minNeighbors=5)
#                                        blue, green red
for x, y, w, h, in faces:
    img=cv2.rectangle(img, (x,y),(x+w,y+h),(0,255,0),3)

print(type(faces))
print(faces)


cv2.imshow("Gray",gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()