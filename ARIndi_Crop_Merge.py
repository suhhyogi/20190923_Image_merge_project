import cv2
import numpy as np

#Only Indi
Indi = cv2.imread("Output_Tall_Ind-2.0.png")
cpy_Indi = Indi.copy()
## cv2.imshow('Indi',cpy_Indi)
#Crop AR
AR = cv2.imread("Output_Tall_AR-2.0.png")
cpy_AR = AR.copy()
# cv2.imshow('AR',cpy_AR)

crp_AR = cpy_AR [251:780, 1:1120]
cv2.imshow('crop',crp_AR)
print(type(cpy_AR))
print(type(crp_AR))

#cv2.imshow("crp_AR", crp_AR)

#Merge Indi & AR
cpy_Indi[251:780, 1:1120] = crp_AR
#cv2.imshow("Merged AR & Indi", cpy_Indi)

#Imge write
cv2.imwrite('Tall_-2.0.png',cpy_Indi)


cv2.waitKey(0)
cv2.destroyAllWindows()