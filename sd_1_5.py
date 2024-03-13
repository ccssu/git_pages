"""Usage
python sd_1_5.py --model_id /share_nfs/hf_models/stable-diffusion-v1-5 \
    --output_file astronaut_rides_horse_onediff_quant.png \
    --quantize \
    --quality_level 7 \
    --output_file astronaut_rides_horse_onediff_quant_7.png \
"""

import torch
import argparse
from diffusers import StableDiffusionPipeline
from onediff.infer_compiler import oneflow_compile

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model_id", type=str, default="runwayml/stable-diffusion-v1-5")
    parser.add_argument("--prompt", type=str, default="a photo of an astronaut riding a horse on mars")
    parser.add_argument("--output_file", type=str, default="sd_v1-5_5.png")
    parser.add_argument("--seed", type=int, default=1)
    parser.add_argument("--backend", type=str, default="onediff", choices=["onediff", "torch"])
    parser.add_argument("--quality_level", type=int, default=5, choices=list(range(8)))
    parser.add_argument("--compute_density_threshold", type=int, default=100)
    parser.add_argument("--quantize", action="store_true")
    parser.add_argument("--cache_dir", type=str, default="./run_sd_v1-5")
    args = parser.parse_args()
    return args

args = parse_args()
pipe = StableDiffusionPipeline.from_pretrained(args.model_id, torch_dtype=torch.float16)
pipe = pipe.to("cuda")

prompt = args.prompt
if args.backend == "onediff":
    pipe.unet = oneflow_compile(pipe.unet)
    if args.quantize:
        pipe.unet.quantize(cache_dir=args.cache_dir, quality_level=args.quality_level, compute_density_threshold=args.compute_density_threshold)
generator = torch.manual_seed(1)
image = pipe(prompt).images[0]  
image.save(args.output_file)
