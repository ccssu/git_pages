import os
import cv2
from skimage.metrics import structural_similarity as ssim
import cv2
import json
basic_key = "sdxl"
url_root="https://ccssu.github.io/git_pages.io"

im1 = cv2.imread(f"{basic_key}_torch.png")
im2 = f"{basic_key}_deepcache_onediff.png"
im2 = cv2.imread(im2)
ssim_val = ssim(im1, im2, channel_axis=2)
print(ssim_val)

