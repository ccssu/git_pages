import torch

from onediffx import compile_pipe
from onediffx.deep_cache import StableDiffusionXLPipeline
import torch
import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model_id", type=str, default="/share_nfs/hf_models/stable-diffusion-xl-base-1.0")
    parser.add_argument("--prompt", type=str, default="a photo of an astronaut riding a horse on mars")
    parser.add_argument("--output_file", type=str, default="sdxl_deepcache_onediff_3.png")
    parser.add_argument("--seed", type=int, default=1)
    parser.add_argument("--quality_level", type=int, default=3, choices=list(range(8)))
    parser.add_argument("--compute_density_threshold", type=int, default=100)
    parser.add_argument("--backend", type=str, default="onediff", choices=["onediff", "torch"])
    parser.add_argument("--quantize", action="store_true")
    parser.add_argument("--cache_dir", type=str, default="./run_sdxl_deepcache")
    args = parser.parse_args()
    return args
args = parse_args()

pipe = StableDiffusionXLPipeline.from_pretrained(
    args.model_id,
    torch_dtype=torch.float16,
    variant="fp16",
    use_safetensors=True
)
pipe.to("cuda")

pipe = compile_pipe(pipe)


if args.quantize:
    # import pdb;pdb.set_trace()
    pipe.unet.quantize(cache_dir=args.cache_dir, quality_level=args.quality_level, compute_density_threshold=args.compute_density_threshold, quantize_conv=False)# fast_unet
    # pipe.fast_unet.quantize(cache_dir=args.cache_dir, quality_level=args.quality_level, compute_density_threshold=args.compute_density_threshold)

prompt = "street style, detailed, raw photo, woman, face, shot on CineStill 800T"
# Warmup
for i in range(10):
    deepcache_output = pipe(
        prompt, 
        cache_interval=3, cache_layer_id=0, cache_block_id=0,
        output_type='pil'
    ).images[0]

torch.manual_seed(1)
deepcache_output = pipe(
    prompt, 
    cache_interval=3, cache_layer_id=0, cache_block_id=0,
    output_type='pil'
).images[0]

# save image
deepcache_output.save(args.output_file)