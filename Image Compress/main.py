import cv2
import numpy as np
url = input("Enter image Location: ")
img = cv2.imread(url)

arR = np.array(list(img))
a_r,s_r,vr = np.linalg.svd(arR[:,:,0])
a_g ,s_g,vg = np.linalg.svd(arR[:,:,1])
a_b,s_b,vb = np.linalg.svd(arR[:,:,2])


print(a_r.shape,vr.shape)

resize = int(input("Enter the resize size: "))
Red = a_r[:,:resize]@np.diag(s_r[:resize])@vr[:resize,:]
Green = a_g[:,:resize]@np.diag(s_r[:resize])@vg[:resize,:]
Blue = a_b[:,:resize]@np.diag(s_r[:resize])@vb[:resize,:]

R = np.clip(Red,0,255).astype(np.uint8)
G = np.clip(Green,0,255).astype(np.uint8)
B = np.clip(Blue,0,255).astype(np.uint8)

ResizeImage = cv2.merge([R,G,B])

cv2.imwrite("Compressed image.jpeg",ResizeImage,[int(cv2.IMWRITE_JPEG_QUALITY), 80])
cv2.imshow("Image",ResizeImage)
cv2.waitKey(0)