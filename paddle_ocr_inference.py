import os
import sys
import subprocess

__dir__ = os.path.dirname(os.path.abspath(__file__))
sys.path.append(__dir__)
sys.path.insert(0, os.path.abspath(os.path.join(__dir__, '../..')))

os.environ["FLAGS_allocator_strategy"] = 'auto_growth'

import cv2
import copy
import numpy as np
import json
import time
import logging
from PIL import Image
import PaddleOCR.tools.infer.utility as utility
import PaddleOCR.tools.infer.predict_rec as predict_rec
import PaddleOCR.tools.infer.predict_det as predict_det
import PaddleOCR.tools.infer.predict_cls as predict_cls
from PaddleOCR.ppocr.utils.utility import get_image_file_list, check_and_read
from PaddleOCR.ppocr.utils.logging import get_logger
from PaddleOCR.tools.infer.utility import draw_ocr_box_txt, get_rotate_crop_image, get_minarea_rect_crop
logger = get_logger()

from PaddleOCR.tools.infer.predict_system import main



if __name__ == "__main__":
    args = utility.parse_args()
    args.use_onnx = True
    args.use_gpu = True
    args.det_model_dir = "./inference/det_onnx/model.onnx"
    args.rec_model_dir = "./inference/rec_onnx/model.onnx"
    args.cls_model_dir = "./inference/cls_onnx/model.onnx"
    
    args.rec_char_dict_path = "./PaddleOCR/ppocr/utils/dict/korean_dict.txt"
    
    for i in os.listdir("./cropped_bus"):
        args.image_dir = f"./cropped_bus/{i}"
        main(args)
    # import pdb;pdb.set_trace()
    main(args)
    pass