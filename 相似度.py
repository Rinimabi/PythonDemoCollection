
from skimage.measure import compare_ssim
from imageio import imread
import numpy as np

# 读取图片
img1 = imread('C:/Users/Administrator/Desktop/img1.jpg')
img2 = imread('C:/Users/Administrator/Desktop/img2.jpg')
img2 = np.resize(img2, (img1.shape[0], img1.shape[1], img1.shape[2]))
print(img1.shape)
print(img2.shape)
ssim = compare_ssim(img1, img2, multichannel=True)
print(ssim)
