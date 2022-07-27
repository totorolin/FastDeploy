# 编译PPYOLOE示例


```
# 下载和解压预测库
wget https://bj.bcebos.com/paddle2onnx/fastdeploy/fastdeploy-linux-x64-0.0.3.tgz
tar xvf fastdeploy-linux-x64-0.0.3.tgz

# 编译示例代码
mkdir build & cd build
cmake ..
make -j

# 下载模型和图片
wget https://bj.bcebos.com/paddle2onnx/fastdeploy/models/ppdet/ppyoloe_crn_l_300e_coco.tgz
tar xvf ppyoloe_crn_l_300e_coco.tgz
wget https://raw.githubusercontent.com/PaddlePaddle/PaddleDetection/release/2.4/demo/000000014439_640x640.jpg

# 执行
./ppyoloe_demo
```

执行完后可视化的结果保存在本地`vis_result.jpg`，同时会将检测框输出在终端，如下所示
```
DetectionResult: [xmin, ymin, xmax, ymax, score, label_id]
162.380249,132.057449, 463.178345, 413.167114, 0.962918, 33
414.914642,141.148666, 91.275269, 308.688293, 0.951003, 0
163.449234,129.669067, 35.253891, 135.111786, 0.900734, 0
267.232239,142.290436, 31.578918, 126.329773, 0.848709, 0
581.790833,179.027115, 30.893127, 135.484940, 0.837986, 0
104.407021,72.602615, 22.900627, 75.469055, 0.796468, 0
348.795380,70.122147, 18.806061, 85.829330, 0.785557, 0
364.118683,92.457428, 17.437622, 89.212891, 0.774282, 0
75.180283,192.470490, 41.898407, 55.552414, 0.712569, 56
328.133759,61.894299, 19.100616, 65.633575, 0.710519, 0
504.797760,181.732574, 107.740814, 248.115082, 0.708902, 0
379.063080,64.762360, 15.956146, 68.312546, 0.680725, 0
25.858747,186.564178, 34.958130, 56.007080, 0.580415, 0
```