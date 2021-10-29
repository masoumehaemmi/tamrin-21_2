import cv2

woman = cv2.imread("woman.jpg", 0)
man= cv2.imread("man.jpg", 0)

for i in range(woman.shape[0]):
    for j in range(woman.shape[1]):
        woman[i, j] = 255 - woman[i, j]

for i in range(man.shape[0]):
    for j in range(man.shape[1]):
        man[i, j] = 255 - man[i, j]

cv2.imwrite("woman1.jpg", woman)
cv2.imwrite("man1.jpg", man)

cv2.waitKey()