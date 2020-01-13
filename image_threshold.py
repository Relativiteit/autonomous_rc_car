import cv2

# Loading image from disk and showing it.
img = cv2.imread('/Users/Chevre/PycharmProjects/autonomous_rc_car/images/Original_files/RCcar.jpg')
# resize image so it fits on my screen, you can change this depending on your screen needs!
imgs = cv2.resize(img, (640, 480))
# cv2.imshow('original img', img)
cv2.imshow('original_img', imgs)

# Finding the threshold array to be shown in the next image.
# retval, threshold = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY)
retval, threshold = cv2.threshold(imgs, 50, 255, cv2.THRESH_BINARY)

grayscaled = cv2.cvtColor(imgs, cv2.COLOR_BGR2GRAY)
# grayscaled = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# retval2, threshold2 = cv2.threshold(grayscaled, 12, 255, cv2.THRESH_BINARY)
retval2, threshold2 = cv2.threshold(grayscaled, 40, 255, cv2.THRESH_BINARY)

# gaus = cv2.adaptiveThreshold(grayscaled, 255 ,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
gaus = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 2)

cv2.imshow('threshold', threshold)
cv2.imshow('threshold2', threshold2)
cv2.imshow('gaus', gaus)

# Wait so the image doesn't instantly disappear.
cv2.waitKey(0)
cv2.destroyAllWindows()
