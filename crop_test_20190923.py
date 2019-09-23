import numpy as np
import cv2


raw_img1 = cv2.imread("Output_Tall_Ind-2.0.png")
raw_img2 = cv2.imread("Output_Tall_AR-2.0.png")

img1 = raw_img1.copy()
img2 = raw_img2.copy()
#crp_AR = cpy_AR [251:780, 1:1120]
img1 = img1[1:250, 1:500]
img2 = img2[250:780, 1:500]
img3 = cv2.vconcat([img1, img2])
cv2.imshow('', img3)

cv2.imwrite('merged image.jpeg',img3)

cv2.waitKey(0)
cv2.destroyAllWindows()