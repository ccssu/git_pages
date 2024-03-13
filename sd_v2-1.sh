set -e  # exit on error

basic_key=sd_v2-1
model_id=/share_nfs/hf_models/stable-diffusion-2-1/
python sd_1_5.py --model_id $model_id \
    --output_file ${basic_key}_onediff.png 

echo "Done with one diffusion"
for i in {0..7}
do
    python sd_1_5.py --model_id $model_id \
        --quantize \
        --quality_level $i \
        --output_file ${basic_key}_$i.png
        echo "Done with quality level $i"
done


