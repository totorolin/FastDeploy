# PaddleDetection模型部署

## 模型版本说明

- [PaddleDetection Release/2.4](https://github.com/PaddlePaddle/PaddleDetection/tree/release/2.4)

## 支持模型列表

目前FastDeploy支持如下模型的部署

- [PP-YOLOE(含PP-YOLOE+)系列模型](https://github.com/PaddlePaddle/PaddleDetection/tree/release/2.4/configs/ppyoloe)
- [PicoDet系列模型](https://github.com/PaddlePaddle/PaddleDetection/tree/release/2.4/configs/picodet)
- [PP-YOLO系列模型(含v2)](https://github.com/PaddlePaddle/PaddleDetection/tree/release/2.4/configs/ppyolo)
- [YOLOv3系列模型](https://github.com/PaddlePaddle/PaddleDetection/tree/release/2.4/configs/yolov3)
- [YOLOX系列模型](https://github.com/PaddlePaddle/PaddleDetection/tree/release/2.4/configs/yolox)
- [FasterRCNN系列模型](https://github.com/PaddlePaddle/PaddleDetection/tree/release/2.4/configs/faster_rcnn)
- [MaskRCNN系列模型](https://github.com/PaddlePaddle/PaddleDetection/tree/release/2.4/configs/mask_rcnn)
- [SSD系列模型](https://github.com/PaddlePaddle/PaddleDetection/tree/release/2.5/configs/ssd)
- [YOLOv5系列模型](https://github.com/PaddlePaddle/PaddleYOLO/tree/release/2.5/configs/yolov5)
- [YOLOv6系列模型](https://github.com/PaddlePaddle/PaddleYOLO/tree/release/2.5/configs/yolov6)
- [YOLOv7系列模型](https://github.com/PaddlePaddle/PaddleYOLO/tree/release/2.5/configs/yolov7)
- [RTMDet系列模型](https://github.com/PaddlePaddle/PaddleYOLO/tree/release/2.5/configs/rtmdet)

## 导出部署模型

在部署前，需要先将PaddleDetection导出成部署模型，导出步骤参考文档[导出模型](https://github.com/PaddlePaddle/PaddleDetection/blob/release/2.4/deploy/EXPORT_MODEL.md)

**注意**
- 在导出模型时不要进行NMS的去除操作，正常导出即可  
- 如果用于跑原生TensorRT后端（非Paddle Inference后端），不要添加--trt参数
- 导出模型时，不要添加`fuse_normalize=True`参数

## 下载预训练模型

为了方便开发者的测试，下面提供了PaddleDetection导出的各系列模型，开发者可直接下载使用。

其中精度指标来源于PaddleDetection中对各模型的介绍，详情各参考PaddleDetection中的说明。


| 模型                                                               | 参数大小    | 精度    | 备注 |
|:---------------------------------------------------------------- |:----- |:----- | :------ |
| [picodet_l_320_coco_lcnet](https://bj.bcebos.com/paddlehub/fastdeploy/picodet_l_320_coco_lcnet.tgz) |23MB | Box AP 42.6% |
| [ppyoloe_crn_l_300e_coco](https://bj.bcebos.com/paddlehub/fastdeploy/ppyoloe_crn_l_300e_coco.tgz) |200MB | Box AP 51.4% |
| [ppyoloe_plus_crn_m_80e_coco](https://bj.bcebos.com/fastdeploy/models/ppyoloe_plus_crn_m_80e_coco.tgz) |83.3MB | Box AP 49.8% |
| [ppyolo_r50vd_dcn_1x_coco](https://bj.bcebos.com/paddlehub/fastdeploy/ppyolo_r50vd_dcn_1x_coco.tgz) | 180MB | Box AP 44.8% | 暂不支持TensorRT |
| [ppyolov2_r101vd_dcn_365e_coco](https://bj.bcebos.com/paddlehub/fastdeploy/ppyolov2_r101vd_dcn_365e_coco.tgz) | 282MB | Box AP 49.7% | 暂不支持TensorRT |
| [yolov3_darknet53_270e_coco](https://bj.bcebos.com/paddlehub/fastdeploy/yolov3_darknet53_270e_coco.tgz) |237MB | Box AP 39.1% | |
| [yolox_s_300e_coco](https://bj.bcebos.com/paddlehub/fastdeploy/yolox_s_300e_coco.tgz) | 35MB | Box AP 40.4% | |
| [faster_rcnn_r50_vd_fpn_2x_coco](https://bj.bcebos.com/paddlehub/fastdeploy/faster_rcnn_r50_vd_fpn_2x_coco.tgz) | 160MB | Box AP 40.8%| 暂不支持TensorRT |
| [mask_rcnn_r50_1x_coco](https://bj.bcebos.com/paddlehub/fastdeploy/mask_rcnn_r50_1x_coco.tgz) | 128M | Box AP 37.4%, Mask AP 32.8%| 暂不支持TensorRT、ORT |
| [ssd_mobilenet_v1_300_120e_voc](https://bj.bcebos.com/paddlehub/fastdeploy/ssd_mobilenet_v1_300_120e_voc.tgz) | 24.9M | Box AP 73.8%| 暂不支持TensorRT、ORT |
| [ssd_vgg16_300_240e_voc](https://bj.bcebos.com/paddlehub/fastdeploy/ssd_vgg16_300_240e_voc.tgz) | 106.5M | Box AP 77.8%| 暂不支持TensorRT、ORT |
| [ssdlite_mobilenet_v1_300_coco](https://bj.bcebos.com/paddlehub/fastdeploy/ssdlite_mobilenet_v1_300_coco.tgz) | 29.1M | | 暂不支持TensorRT、ORT |
| [rtmdet_l_300e_coco](https://bj.bcebos.com/paddlehub/fastdeploy/rtmdet_l_300e_coco.tgz) | 224M | Box AP 51.2%|  |
| [rtmdet_s_300e_coco](https://bj.bcebos.com/paddlehub/fastdeploy/rtmdet_s_300e_coco.tgz) | 42M | Box AP 44.5%|  |
| [yolov5_l_300e_coco](https://bj.bcebos.com/paddlehub/fastdeploy/yolov5_l_300e_coco.tgz) | 183M | Box AP 48.9%|  |
| [yolov5_s_300e_coco](https://bj.bcebos.com/paddlehub/fastdeploy/yolov5_s_300e_coco.tgz) | 31M | Box AP 37.6%|  |
| [yolov6_l_300e_coco](https://bj.bcebos.com/paddlehub/fastdeploy/yolov6_l_300e_coco.tgz) | 229M | Box AP 51.0%|  |
| [yolov6_s_400e_coco](https://bj.bcebos.com/paddlehub/fastdeploy/yolov6_s_400e_coco.tgz) | 68M | Box AP 43.4%|  |
| [yolov7_l_300e_coco](https://bj.bcebos.com/paddlehub/fastdeploy/yolov7_l_300e_coco.tgz) | 145M | Box AP 51.0%|  |
| [yolov7_x_300e_coco](https://bj.bcebos.com/paddlehub/fastdeploy/yolov7_x_300e_coco.tgz) | 277M | Box AP 53.0%|  |

## 详细部署文档

- [Python部署](python)
- [C++部署](cpp)
