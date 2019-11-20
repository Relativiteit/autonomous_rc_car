import cv2

# Loading image from disk and showing it.
img = cv2.imread('/Users/Chevre/PycharmProjects/Code/OpenCVWithPythonForImage/bookpage.jpg')
cv2.imshow('original img', img)

# Finding the threshold array to be shown in the next image.
retval, threshold = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY)

grayscaled = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
retval2, threshold2 = cv2.threshold(grayscaled, 12, 255, cv2.THRESH_BINARY)

gaus = cv2.adaptiveThreshold(grayscaled, 255 ,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)

cv2.imshow('threshold', threshold)
cv2.imshow('threshold2', threshold2)
cv2.imshow('gaus', gaus)

# Wait so the image doesn't instantly disappear.
cv2.waitKey(0)
cv2.destroyAllWindows()
