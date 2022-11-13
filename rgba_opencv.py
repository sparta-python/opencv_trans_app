import cv2

mask_img = cv2.imread("images/otahuku.png", -1)
print(mask_img)
print(mask_img.shape)

# 画像データに背景も含めて持っている
