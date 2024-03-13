"""
python sdxl.py --model_id /share_nfs/hf_models/stable-diffusion-xl-base-1.0 
"""
from diffusers import StableDiffusionXLPipeline
import torch
import argparse
from onediff.infer_compiler import oneflow_compile

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model_id", type=str, default="/share_nfs/hf_models/stable-diffusion-xl-base-1.0 ")
    parser.add_argument("--prompt", type=str, default="a photo of an astronaut riding a horse on mars")
    parser.add_argument("--output_file", type=str, default="astronaut_rides_horse_onediff_quant.png")
    parser.add_argument("--seed", type=int, default=1)
    parser.add_argument("--quality_level", type=int, default=2, choices=list(range(8)))
    parser.add_argument("--compute_density_threshold", type=int, default=100)
    parser.add_argument("--backend", type=str, default="onediff", choices=["onediff", "torch"])
    parser.add_argument("--quantize", action="store_true")
    parser.add_argument("--cache_dir", type=str, default="./run_sdxl")
    args = parser.parse_args()
    return args
args = parse_args()
pipe = StableDiffusionXLPipeline.from_pretrained(args.model_id, torch_dtype=torch.float16, use_safetensors=True, variant="fp16")
pipe.to("cuda")

prompt = "street style, detailed, raw photo, woman, face, shot on CineStill 800T"
torch.manual_seed(args.seed)
if args.backend == "onediff":
    pipe.unet = oneflow_compile(pipe.unet)
    if args.quantize:
        pipe.unet.quantize(cache_dir=args.cache_dir, quality_level=args.quality_level, compute_density_threshold=args.compute_density_threshold)
images = pipe(prompt=prompt, height = 1024, width = 1024, num_inference_steps=50).images[0]

images.save(args.output_file)


