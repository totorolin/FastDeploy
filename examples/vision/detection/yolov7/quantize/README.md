# YOLOv7量化模型部署
FastDeploy已支持部署量化模型,并提供一键模型自动化压缩的工具.
用户可以使用一键模型自动化压缩工具,自行对模型量化后部署, 也可以直接下载FastDeploy提供的量化模型进行部署.

## FastDeploy一键模型自动化压缩工具
FastDeploy 提供了一键模型自动化压缩工具, 能够简单地通过输入一个配置文件, 对模型进行量化.
详细教程请见: [一键模型自动化压缩工具](../../../../../tools/common_tools/auto_compression/)

## 下载量化完成的YOLOv7模型
用户也可以直接下载下表中的量化模型进行部署.(点击模型名字即可下载)


Benchmark表格说明:
- Runtime时延为模型在各种Runtime上的推理时延,包含CPU->GPU数据拷贝,GPU推理,GPU->CPU数据拷贝时间. 不包含模型各自的前后处理时间.
- 端到端时延为模型在实际推理场景中的时延, 包含模型的前后处理.
- 所测时延均为推理1000次后求得的平均值, 单位是毫秒.
- INT8 + FP16 为在推理INT8量化模型的同时, 给Runtime 开启FP16推理选项
- INT8 + FP16 + PM, 为在推理INT8量化模型和开启FP16的同时, 开启使用Pinned Memory的选项,可加速GPU->CPU数据拷贝的速度
- 最大加速比, 为FP32时延除以INT8推理的最快时延,得到最大加速比.
- 策略为量化蒸馏训练时, 采用少量无标签数据集训练得到量化模型, 并在全量验证集上验证精度, INT8精度并不代表最高的INT8精度.
- CPU为Intel(R) Xeon(R) Gold 6271C, 所有测试中固定CPU线程数为1.  GPU为Tesla T4, TensorRT版本8.4.15.

#### Runtime Benchmark
| 模型                 |推理后端            |部署硬件    | FP32 Runtime时延   | INT8 Runtime时延 | INT8 + FP16 Runtime时延  | INT8+FP16+PM Runtime时延  | 最大加速比    | FP32 mAP | INT8 mAP | 量化方式   |
| ------------------- | -----------------|-----------|  --------     |--------      |--------      | --------- |-------- |----- |----- |----- |
| [YOLOv7](https://bj.bcebos.com/paddlehub/fastdeploy/yolov7_quant.tar)            | TensorRT   |    GPU    |     27.47    |  6.52   |  6.74| 5.19|    5.29       | 51.1| 50.4|量化蒸馏训练 |
| [YOLOv7](https://bj.bcebos.com/paddlehub/fastdeploy/yolov7_quant.tar)            | Paddle-TensorRT |    GPU    |     27.87|None|6.91|5.86      |      4.76       | 51.1| 50.4|量化蒸馏训练 |
| [YOLOv7](https://bj.bcebos.com/paddlehub/fastdeploy/yolov7_quant.tar)             | ONNX Runtime     |    CPU    |     996.65        |  467.15 |None|None          |  2.13           | 51.1 | 43.3|量化蒸馏训练 |
| [YOLOv7](https://bj.bcebos.com/paddlehub/fastdeploy/yolov7_quant.tar)             | Paddle Inference  |    CPU    |     995.85  |     477.93|None|None      |   2.08         |51.1 | 46.2|量化蒸馏训练 |

#### 端到端 Benchmark
| 模型                 |推理后端            |部署硬件    | FP32 End2End时延   | INT8 End2End时延 | INT8 + FP16 End2End时延  | INT8+FP16+PM End2End时延  | 最大加速比    | FP32 mAP | INT8 mAP | 量化方式   |
| ------------------- | -----------------|-----------|  --------     |--------      |--------      | --------- |-------- |----- |----- |----- |
| [YOLOv7](https://bj.bcebos.com/paddlehub/fastdeploy/yolov7_quant.tar)            | TensorRT   |    GPU    |     36.47   |  18.81  |  20.33| 17.58|    2.07      | 51.1| 50.4|量化蒸馏训练 |
| [YOLOv7](https://bj.bcebos.com/paddlehub/fastdeploy/yolov7_quant.tar)            | Paddle-TensorRT |    GPU    |     37.06|None|20.26|17.53    |      2.11      | 51.1| 50.4|量化蒸馏训练 |
| [YOLOv7](https://bj.bcebos.com/paddlehub/fastdeploy/yolov7_quant.tar)             | ONNX Runtime     |    CPU    |     988.85       |  478.08 |None|None          |  2.07          | 51.1 | 43.3|量化蒸馏训练 |
| [YOLOv7](https://bj.bcebos.com/paddlehub/fastdeploy/yolov7_quant.tar)             | Paddle Inference  |    CPU    |     1031.73 |     500.12|None|None      |   2.06         |51.1 | 46.2|量化蒸馏训练 |

## 详细部署文档

- [Python部署](python)
- [C++部署](cpp)
