import cv2
import skimage.io as io
img = io.imread('templates/mario_bros.png')
print(img.shape)
io.imshow(img)
cropped = img[32:32+16,178:178+12]
print(cropped.shape)