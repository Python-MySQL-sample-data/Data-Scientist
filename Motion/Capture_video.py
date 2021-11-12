import cv2, time
# 0 camera, 1 another camera, etc else video file
video=cv2.VideoCapture("IMG_2232.mov")
#interate through each frame till hit "q"
#how many frames - increment "a"
a=1
while True:
    a=a+1
    check, frame = video.read()

    print(check)
    print(frame)

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("Capturing",gray)
    key=cv2.waitKey(1)  # 1 millisecond, very fast
    if key==ord('q'):
        break

print(a," frames")
video.release()
cv2.destroyAllWindows