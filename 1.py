import sys
import cv2
import numpy as np
import math


def H(x, y, cx, cy, rad):
    f = (x - cx) ** 2 + (y - cy) ** 2
    f = math.exp(-(f / (2 * (rad ** 2))))
    return f


imageSource = 'lab 3/97.jpg'
img = cv2.imread(imageSource, cv2.IMREAD_GRAYSCALE)

res = np.fft.fft2(img)
fshift = np.fft.fftshift(res)
magnitude_spectrum = 20 * np.log(np.abs(fshift))

cv2.imshow("Magnitude Spectrum", np.array(magnitude_spectrum, dtype=np.uint8))

rows, cols = img.shape
crow, ccol = int(rows / 2), int(cols / 2)
filter_type = sys.argv[1]
rad = float(sys.argv[2])
if filter_type == 'H':
    for i in range(rows):
        for j in range(cols):
            fshift[i, j] = fshift[i, j] * (1 - H(i, j, crow, ccol, rad))
else:
    for i in range(rows):
        for j in range(cols):
            fshift[i, j] = fshift[i, j] * H(i, j, crow, ccol, rad)
f_ishift = np.fft.ifftshift(fshift)
img_back = np.fft.ifft2(f_ishift)
img_back = np.abs(img_back)
cv2.imshow("Original", img)
if filter_type == 'H':
    cv2.imshow("After HPF", np.array(img + img_back, dtype=np.uint8))
else:
    cv2.imshow("After LPF", np.array(img_back, dtype=np.uint8))

cv2.waitKey(20000)
cv2.destroyAllWindows()
