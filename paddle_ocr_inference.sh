python PaddleOCR/tools/infer/predict_system.py --use_gpu=True --use_onnx=True \
    --det_model_dir=./inference/det_onnx/model.onnx  \
    --rec_model_dir=./inference/rec_onnx/model.onnx  \
    --cls_model_dir=./inference/cls_onnx/model.onnx  \
    --image_dir=/home/cvlab09/projects/joungbin/iSEE-AI/cropped_bus/test9.png \
    --rec_char_dict_path=./PaddleOCR/ppocr/utils/dict/korean_dict.txt