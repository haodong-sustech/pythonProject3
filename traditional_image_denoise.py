import bm3d
from skimage import img_as_float
import cv2
import matplotlib.pyplot as plt
import numpy as np
from skimage.restoration import denoise_nl_means, estimate_sigma
from scipy import ndimage as nd
import tifffile as tiff
import imageio as io

noisy_img = io.volread('substack.tif')
noisy_img = img_as_float(noisy_img)


#Gaussian 算法
gaussian_img = nd.gaussian_filter(noisy_img, sigma=3)


# median 算法
#media_img = nd.median_filter(noisy_img, size=3)

'''
# NL 算法
sigma_est = np.mean(estimate_sigma(noisy_img, channel_axis=None))
nl_img = denoise_nl_means(noisy_img,
                               h=1.*sigma_est,
                               fast_mode=True,
                               patch_size=5,
                               patch_distance=3,
                               channel_axis=None)
'''

#BM3D算法
#BM3D_denoised = bm3d.bm3d(noisy_img, sigma_psd=0.01, stage_arg=bm3d.BM3DStages.ALL_STAGES)


denoise_data = gaussian_img
# Limit and scale reconstruction.
denoise_data[denoise_data<0] = 0
denoise_data /= np.max(denoise_data)
denoise_data = np.round(denoise_data * 65535).astype(np.uint16)

# 保存为三维TIFF文件
tiff.imwrite("C:/pythonProject3/gaussian_img.tif", denoise_data)

'''
plt.title("Noisy Image")
plt.imshow(noisy_img, cmap='gray')
plt.show()

plt.title("Denoised Image")
plt.imshow(media_img, cmap='gray')
plt.show()
'''