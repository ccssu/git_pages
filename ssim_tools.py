from skimage.metrics import structural_similarity as ssim
import cv2
import json

def out(basic_key):
    print(f'--'*20, basic_key, '--'*20)
    print(f'|{basic_key}| quality_level| SSIM| Conv-Count| Linear-Count|')
    print(f'|--|--|--|--|--|')
    for i in range(5):
        im1 = cv2.imread(f"{basic_key}_torch.png")
        im2 = cv2.imread(f"{basic_key}_{i}.png")

        # 计算 SSIM 值
        ssim_value = ssim(im1, im2, channel_axis=2)

        file_path = f'run_{basic_key}/config.quality_level={i}.json'
        info = json.load(open(file_path))
        linear_names_length = info["linear_names_length"]
        conv_names_length = info["conv_names_length"]
        print(f"|{basic_key}| {i} | {ssim_value} | {conv_names_length} | {linear_names_length} |")

        # print(f"quality_level: {i} SSIM 值为: {ssim_value}")
        

    print(f'--'*20, "end", '--'*20)

basic_key = "sd_v1-5"
out(basic_key)
basic_key = "sdxl"
out(basic_key)

