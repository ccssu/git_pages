set -e  # exit on error
export CUDA_VISIBLE_DEVICES=7
export ONEDIFF_DEBUG=1

basic_key=sd_v1-5_deepcache
model_id=/share_nfs/hf_models/stable-diffusion-v1-5
py_script=sd_v1-5_deepcache.py

python $py_script --model_id $model_id \
    --output_file ${basic_key}_onediff.png 

echo "Done with one diffusion"


for i in {0..4}
do
    python $py_script --model_id $model_id \
        --quantize \
        --quality_level $i \
        --output_file ${basic_key}_$i.png
        echo "Done with quality level $i"
done


