calibrate_info = "sd_1_5.txt"


def load_new_calibrate_info(calibrate_info_file_path)->dict:
    callable_info = {}
    with open(calibrate_info_file_path, "r") as f:
        for line in f.readlines():
            line = line.strip()
            items = line.split("\t")
            callable_info[items[0]] = (items[1], float(items[2]) )

    return callable_info

calibrate_info = load_new_calibrate_info(calibrate_info)
print(f'{len(calibrate_info)}')
# print(list(sdxl_calibrate_info.keys()))
# print(f'{new_sdxl_calibrate_info=}')

name_list = list(calibrate_info.keys())
data_list = [value[1] for _, value in calibrate_info.items()]
def normalize(data):
    min_val, max_val = min(data) , max(data)
    return ((x - min_val) / (max_val - min_val) * 1e3 for x in data)


data_list = list(normalize(data_list))

data_list = [(name,value) for name,value in zip(name_list, data_list)] 

sorted_data_list = sorted(data_list, key=lambda x: x[1])



y = sum(x >= 1 for _, x in sorted_data_list)
print(f'{y=}')
results = {name: value for name, value in sorted_data_list if value <=1 }

import json 

json.dump(results, open("sd1_5.json", "w"))

