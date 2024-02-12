import os
import sys

import torch

__dir__ = os.path.dirname(os.path.abspath(__file__))
sys.path.append(__dir__)
sys.path.insert(0, os.path.abspath(os.path.join(__dir__, '../..')))

os.environ["FLAGS_allocator_strategy"] = 'auto_growth'

from PaddleOCR.tools.infer import utility
from PaddleOCR.tools.infer.predict_system import TextSystem, main

def ocr_load():
    args = utility.parse_args()
    args.use_onnx = True
    args.use_gpu = torch.cuda.is_available()
    args.det_model_dir = "./inference/det_onnx/model.onnx"
    args.rec_model_dir = "./inference/rec_onnx/model.onnx"
    args.cls_model_dir = "./inference/cls_onnx/model.onnx"
    args.rec_char_dict_path = "./PaddleOCR/ppocr/utils/dict/korean_dict.txt"
    return TextSystem(args)


def ocr_inference(ocr_model:TextSystem, input_images):
    return main(images=input_images, ocr_model=ocr_model)
