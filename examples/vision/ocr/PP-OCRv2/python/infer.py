# Copyright (c) 2022 PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import fastdeploy as fd
import cv2
import os


def parse_arguments():
    import argparse
    import ast
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--det_model", required=True, help="Path of Detection model of PPOCR.")
    parser.add_argument(
        "--cls_model",
        required=True,
        help="Path of Classification model of PPOCR.")
    parser.add_argument(
        "--rec_model",
        required=True,
        help="Path of Recognization model of PPOCR.")
    parser.add_argument(
        "--rec_label_file",
        required=True,
        help="Path of Recognization model of PPOCR.")
    parser.add_argument(
        "--image", type=str, required=True, help="Path of test image file.")
    parser.add_argument(
        "--device",
        type=str,
        default='cpu',
        help="Type of inference device, support 'cpu' or 'gpu'.")
    parser.add_argument(
        "--backend",
        type=str,
        default="default",
        help="Type of inference backend, support ort/trt/paddle/openvino, default 'openvino' for cpu, 'tensorrt' for gpu"
    )
    parser.add_argument(
        "--device_id",
        type=int,
        default=0,
        help="Define which GPU card used to run model.")
    parser.add_argument(
        "--cpu_thread_num",
        type=int,
        default=9,
        help="Number of threads while inference on CPU.")
    return parser.parse_args()


def build_option(args):
    option = fd.RuntimeOption()
    if args.device.lower() == "gpu":
        option.use_gpu(0)

    option.set_cpu_thread_num(args.cpu_thread_num)

    if args.backend.lower() == "trt":
        assert args.device.lower(
        ) == "gpu", "TensorRT backend require inference on device GPU."
        option.use_trt_backend()
    elif args.backend.lower() == "pptrt":
        assert args.device.lower(
        ) == "gpu", "Paddle-TensorRT backend require inference on device GPU."
        option.use_trt_backend()
        option.enable_paddle_trt_collect_shape()
        option.enable_paddle_to_trt()
    elif args.backend.lower() == "ort":
        option.use_ort_backend()
    elif args.backend.lower() == "paddle":
        option.use_paddle_infer_backend()
    elif args.backend.lower() == "openvino":
        assert args.device.lower(
        ) == "cpu", "OpenVINO backend require inference on device CPU."
        option.use_openvino_backend()
    return option


args = parse_arguments()

# Detection模型, 检测文字框
det_model_file = os.path.join(args.det_model, "inference.pdmodel")
det_params_file = os.path.join(args.det_model, "inference.pdiparams")
# Classification模型，方向分类，可选
cls_model_file = os.path.join(args.cls_model, "inference.pdmodel")
cls_params_file = os.path.join(args.cls_model, "inference.pdiparams")
# Recognition模型，文字识别模型
rec_model_file = os.path.join(args.rec_model, "inference.pdmodel")
rec_params_file = os.path.join(args.rec_model, "inference.pdiparams")
rec_label_file = args.rec_label_file

# 对于三个模型，均采用同样的部署配置
# 用户也可根据自行需求分别配置
runtime_option = build_option(args)

# PPOCR的cls和rec模型现在已经支持推理一个Batch的数据
# 定义下面两个变量后, 可用于设置trt输入shape, 并在PPOCR模型初始化后, 完成Batch推理设置
cls_batch_size = 1
rec_batch_size = 6

# 当使用TRT时，分别给三个模型的runtime设置动态shape,并完成模型的创建.
# 注意: 需要在检测模型创建完成后，再设置分类模型的动态输入并创建分类模型, 识别模型同理.
# 如果用户想要自己改动检测模型的输入shape, 我们建议用户把检测模型的长和高设置为32的倍数.
det_option = runtime_option
det_option.set_trt_input_shape("x", [1, 3, 64, 64], [1, 3, 640, 640],
                               [1, 3, 960, 960])
# 用户可以把TRT引擎文件保存至本地
# det_option.set_trt_cache_file(args.det_model  + "/det_trt_cache.trt")
det_model = fd.vision.ocr.DBDetector(
    det_model_file, det_params_file, runtime_option=det_option)

cls_option = runtime_option
cls_option.set_trt_input_shape("x", [1, 3, 48, 10],
                               [cls_batch_size, 3, 48, 320],
                               [cls_batch_size, 3, 48, 1024])
# 用户可以把TRT引擎文件保存至本地
# cls_option.set_trt_cache_file(args.cls_model  + "/cls_trt_cache.trt")
cls_model = fd.vision.ocr.Classifier(
    cls_model_file, cls_params_file, runtime_option=cls_option)

rec_option = runtime_option
rec_option.set_trt_input_shape("x", [1, 3, 32, 10],
                               [rec_batch_size, 3, 32, 320],
                               [rec_batch_size, 3, 32, 2304])
# 用户可以把TRT引擎文件保存至本地
# rec_option.set_trt_cache_file(args.rec_model  + "/rec_trt_cache.trt")
rec_model = fd.vision.ocr.Recognizer(
    rec_model_file, rec_params_file, rec_label_file, runtime_option=rec_option)

# 创建PP-OCR，串联3个模型，其中cls_model可选，如无需求，可设置为None
ppocr_v2 = fd.vision.ocr.PPOCRv2(
    det_model=det_model, cls_model=cls_model, rec_model=rec_model)

# 给cls和rec模型设置推理时的batch size
# 此值能为-1, 和1到正无穷
# 当此值为-1时, cls和rec模型的batch size将默认和det模型检测出的框的数量相同
ppocr_v2.cls_batch_size = cls_batch_size
ppocr_v2.rec_batch_size = rec_batch_size

# 预测图片准备
im = cv2.imread(args.image)

#预测并打印结果
result = ppocr_v2.predict(im)

print(result)

# 可视化结果
vis_im = fd.vision.vis_ppocr(im, result)
cv2.imwrite("visualized_result.jpg", vis_im)
print("Visualized result save in ./visualized_result.jpg")
