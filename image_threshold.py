import cv2

# Loading image from disk and showing it.
img = cv2.imread('/Users/Chevre/PycharmProjects/Code/OpenCVWithPythonForImage/bookpage.jpg')
cv2.imshow('original img', img)

# Finding the threshold array to be shown in the next image.
retval, threshold = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY)
cv2.imshow('threshold', threshold)

# Wait so the image doesn't instantly disappear.
cv2.waitKey(0)
cv2.destroyAllWindows()
