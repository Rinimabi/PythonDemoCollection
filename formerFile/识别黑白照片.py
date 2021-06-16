# 黑白照片（灰度图）识别
from PIL import Image
import numpy as np
import os


def isGrayMap(img, threshold=15):
    """
    入参：
    img：PIL读入的图像
    threshold：判断阈值，图片3个通道间差的方差均值小于阈值则判断为灰度图。
    阈值设置的越小，容忍出现彩色面积越小；设置的越大，那么就可以容忍出现一定面积的彩色，例如微博截图。
    如果阈值设置的过小，某些灰度图片会被漏检，这是因为某些黑白照片存在偏色，例如发黄的黑白老照片、
    噪声干扰导致灰度图不同通道间值出现偏差（理论上真正的灰度图是RGB三个通道的值完全相等或者只有一个通道，
    然而实际上各通道间像素值略微有偏差看起来仍是灰度图）
    出参：
    bool值
    """
    if len(img.getbands()) == 1:
        return True
    img1 = np.asarray(img.getchannel(channel=0), dtype=np.int16)
    img2 = np.asarray(img.getchannel(channel=1), dtype=np.int16)
    img3 = np.asarray(img.getchannel(channel=2), dtype=np.int16)
    diff1 = (img1 - img2).var()
    diff2 = (img2 - img3).var()
    diff3 = (img3 - img1).var()
    diff_sum = (diff1 + diff2 + diff3) / 3.0
    if diff_sum <= threshold:
        return True
    else:
        return False


def is_color_image(url):
    heibai=0.0
    caise=0.0
    im = Image.open(url)
    pix = im.convert('RGB')
    width = im.size[0]
    height = im.size[1]
    oimage_color_type = True
    is_color = []
    for x in range(width):
        for y in range(height):
            r, g, b = pix.getpixel((x, y))
            r = int(r)
            g = int(g)
            b = int(b)
            if (r == g) and (g == b):
                heibai+=1.0
            else:
                caise+=1.0
    # print(heibai/(heibai+caise))
    if heibai/(heibai+caise)<0.7:
        oimage_color_type = False
    return oimage_color_type

address = "C:/Users/Administrator/Documents/Tencent Files/453211317/Image/Group/"
source = "C:\\Users\\Administrator\\Documents\\Tencent Files\\453211317\\Image\\Group\\"
target = "C:\\Users\\Administrator\\Desktop\\images\\"
list = os.listdir(address)
for i in range(0, len(list)):
    if list[i].endswith(".jpg") or list[i].endswith(".png"):
        path = os.path.join(address, list[i])
        if os.path.isfile(path):
            if is_color_image(path) == True:
                os.system("copy \"{0}\" \"{1}\"".format("{0}{1}".format(source, list[i]), "{0}{1}".format(target, list[i])))

# print(is_color_image(
#     'C:/Users/Administrator/Documents/Tencent Files/453211317/Image/Group/1E27ENSWFZNK4UFB7X0_PK2.jpg'))
# print(is_color_image('C:/Users/Administrator/Desktop/img1.jpg'))
