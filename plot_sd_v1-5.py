import json
conv2d_file_path = "/data/home/fengwen/dev_quant_tools/run_sd_v1-5/UNet2DConditionModel_06f5730368ef1a128ac8e3ae1728b45f2c7236621a050beb40bba85b1ef7b660_conv2d_calibrate_info.json"
linear_file_path = "/data/home/fengwen/dev_quant_tools/run_sd_v1-5/UNet2DConditionModel_06f5730368ef1a128ac8e3ae1728b45f2c7236621a050beb40bba85b1ef7b660_linears_calibrate_info.json"
compute_density_info = "/data/home/fengwen/dev_quant_tools/run_sd_v1-5/UNet2DConditionModel_06f5730368ef1a128ac8e3ae1728b45f2c7236621a050beb40bba85b1ef7b660_costs_calibrate_info.json"

conv_info = json.load(open(conv2d_file_path))
linear_info = json.load(open(linear_file_path))
compute_density_info = json.load(open(compute_density_info))

new_result = {}
conv_linear_lst = [(k,v) for k,v in {**linear_info, **conv_info}.items()]
conv_linear_lst.sort(key=lambda x: x[1]["mae"])

def normalize(lst: list):
    x_min = min(lst)
    x_max = max(lst)
    return [(x - x_min) / (x_max - x_min) for x in lst]

lst = [x[1]["mae"] for x in conv_linear_lst]
lst = normalize(lst)
avg = sum(lst) / len(lst)
for (key, value), vv in zip(conv_linear_lst, lst):
    if vv < avg:
        new_result[key] = value
    else:
        break


for key, value in compute_density_info.items():
    if value["compute_density"] < 100 and key in new_result:
        del new_result[key]

json.dump(new_result, open("sd_v1-5_conv2d_linear_calibrate_info.json", "w"))


conv_info = linear_info

import plotly.graph_objs as go
from plotly.offline import plot

# "time_embedding.linear_2": {
#     "mse": 5.960464477539063e-08,
#     "mae": 9.834766387939453e-05,
#     "max_diff": 0.001953125
# },
mse_list = [x["mse"] for x in conv_info.values()]
mae_list = [x["mae"] for x in conv_info.values()]
max_diff_list = [x["max_diff"] for x in conv_info.values()]

# 归一化
def normalize(lst: list):
    x_min = min(lst)
    x_max = max(lst)
    return [(x - x_min) / (x_max - x_min) for x in lst]
x = list(range(len(mse_list)))
y1 = normalize(mse_list)
y2 = normalize(mae_list)
y3 = normalize(max_diff_list)


# 创建折线图的数据对象
# trace1 = go.Scatter(x=x, y=y1, mode='lines', name='Line 1', line=dict(color='blue'))
# trace2 = go.Scatter(x=x, y=y2, mode='lines', name='Line 2', line=dict(color='red'))

trace1 = go.Scatter(x=x, y=y1, mode='lines', name='mse', line=dict(color='blue'))
trace2 = go.Scatter(x=x, y=y2, mode='lines', name='mae', line=dict(color='red'))
trace3 = go.Scatter(x=x, y=y3, mode='lines', name='max_diff', line=dict(color='green'))


# 设置布局
# layout = go.Layout(title='Multiple Line Plot', xaxis=dict(title='X-axis'), yaxis=dict(title='Y-axis'))
layout = go.Layout(title = "sd_v1-5 Linear Line Plot", xaxis=dict(title='index'), yaxis=dict(title='value'))
# 组合数据对象
data = [trace1, trace2, trace3]

# 创建图形对象
fig = go.Figure(data=data, layout=layout)

# 在线绘制并保存为HTML文件
plot(fig, filename='sd_v1-5_linear.html')


# Quantized conv: 85 
# Quantized linear: 173 
# Time: 0.3136s 

# Quantized conv: 73 
# Quantized linear: 156 
# Time: 0.2598s 

# Quantized conv: 73 
# Quantized linear: 133 
# Time: 0.2682s 