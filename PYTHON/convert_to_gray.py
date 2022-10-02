import cv2
img_val = input("Enter the image name: ")
img = cv2.imread(img_val)
cv2.imshow("Original Image", img)
img1 = cv2.resize(img, (300, 300))
cv2.imshow("Resized image", img1)
gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
cv2.imshow("grayscale",gray)
