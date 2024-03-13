import os
import cv2
from skimage.metrics import structural_similarity as ssim
import cv2
import json

url_root="https://ccssu.github.io/git_pages.io"
# conv_linear_calibrate_info ="run_sd_v1-5_deepcache/conv_linear_calibrate_infoUNet2DConditionModel_06f5730368ef1a128ac8e3ae1728b45f2c7236621a050beb40bba85b1ef7b660.html"
# conv_linear_calibrate_info = f'{url_root}/{conv_linear_calibrate_info}'
# print(f'[sd_v1-5:conv_linear_calibrate_info]({conv_linear_calibrate_info})')
# const_cailbrate_info = "run_sd_v1-5/CostsQuantizationCalibratorUNet2DConditionModel_06f5730368ef1a128ac8e3ae1728b45f2c7236621a050beb40bba85b1ef7b660.json.html"
# const_cailbrate_info = f'{url_root}/{const_cailbrate_info}'
# print(f'[sd_v1-5:const_cailbrate_info]({const_cailbrate_info})')


# conv_linear_calibrate_info = "run_sdxl/conv_linear_calibrate_infoUNet2DConditionModel_34f5bd9d3416cc1703c40491d1fa89fc50081c344f7a9ccf7b64f853a711f342.html"
# conv_linear_calibrate_info = f'{url_root}/{conv_linear_calibrate_info}'
# print(f'[sdxl:conv_linear_calibrate_info]({conv_linear_calibrate_info})')
# const_cailbrate_info = "run_sdxl/costs_calibrate_info_UNet2DConditionModel_34f5bd9d3416cc1703c40491d1fa89fc50081c344f7a9ccf7b64f853a711f342.json.html"

# const_cailbrate_info = f'{url_root}/{const_cailbrate_info}'
# print(f'[sdxl:const_cailbrate_info]({const_cailbrate_info})')






basic_key="sdxl_deepcache"
basic = "sdxl_torch.png"

print(f'| {basic_key} | PyTorch  | OneDiff| SSIM | ')
print(f'|---|---|---|---|')


if basic is None:
    im1 = cv2.imread(f"{basic_key}_torch.png")
else:
    im1 = cv2.imread(basic)

im2_lst = [cv2.imread(f"{basic_key}_onediff.png")]
im2_lst.extend([cv2.imread(f"{basic_key}_{i}.png") for i in range(5)])

i = -1
for im2 in im2_lst:
    ssim_val = ssim(im1, im2, channel_axis=2)
    out_key = f'{url_root}/{basic_key}'
    if i> -1:
        file_path = f'run_{basic_key}/config.quality_level={i}.json'
        info = json.load(open(file_path))
        linear_names_length = info["linear_names_length"]
        conv_names_length = info["conv_names_length"]
        if basic is None:
            print(f'| quality_level: {i} | ![]({out_key}_torch.png)|  ![]({out_key}_{i}.png) | {ssim_val:.4f} |')
        else:
            print(f'| quality_level: {i} | ![]({out_key}_torch.png)|  ![]({out_key}_{i}.png) | {ssim_val:.4f} |')


    else:
        print(f'|  | ![]({out_key}_torch.png)|  ![]({url_root}/{basic}) | {ssim_val:.4f}| ')
    i = i + 1
