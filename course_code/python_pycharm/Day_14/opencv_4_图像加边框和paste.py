import cv2

img = cv2.imread("OIP-C.jpg")
img_paste = cv2.imread("Mom.jpg")
print(img_paste.shape)
print(img.shape)
scale_img_paste = cv2.resize(img_paste, dsize=(20, int(20 * 1.6)))
# cv2.imshow('img_paste', scale_img_paste)
# 对原图进行赋值
h, w, c = img.shape
h_p, w_p, c_p = scale_img_paste.shape
padding = 10
img[:padding, :] = (255, 0, 0)
img[h - padding:h, padding:w - padding] = [0, 255, 0]
img[:, 0:padding] = (0, 255, 255)
img[:, w - padding:] = (255, 255, 0)
img[50:h_p+50, 50:w_p+50] = scale_img_paste[:, :]


cv2.imshow('img', img)

cv2.waitKey(0)
cv2.destroyAllWindows()