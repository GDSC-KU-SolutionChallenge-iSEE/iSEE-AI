# iSEE-AI
AI application for **iSee** project, attending [GoogleSolutionChallenge2024](https://developers.google.com/community/gdsc-solution-challenge). 

iSee aims to provide visual assitance for individuals with visual impairments. 



# 프로젝트명

이 프로젝트는 YOLO v8을 사용하여 객체 탐지를 수행하고, Paddle OCR을 사용하여 이미지 내의 텍스트를 인식합니다.

## 시작하기

프로젝트를 시작하기 전에 필요한 라이브러리와 환경을 설정해야 합니다.

### 환경 설정

Anaconda를 사용하여 필요한 환경을 구성합니다. 먼저, 다음 명령어로 환경을 생성하세요:

\```bash
conda env create --file environment.yaml
\```

환경이 성공적으로 생성되면, 생성된 환경을 활성화합니다:

\```bash
conda activate [환경명]
\```

### YOLO v8 추론

YOLO v8을 사용하여 이미지에서 객체를 탐지하기 위해, 아래 명령어를 실행하세요:

\```bash
python yolo_inference.py
\```

`yolo_inference.py` 스크립트는 입력 이미지를 처리하고 탐지 결과를 출력합니다. 스크립트를 실행하기 전에, 입력 이미지 경로와 결과를 저장할 경로를 스크립트 내에서 설정해야 할 수 있습니다.

### Paddle OCR 추론

Paddle OCR을 사용하여 이미지 내의 텍스트를 인식하기 위해, 다음 명령어를 실행하세요:

\```bash
python paddle_ocr_inference.py
\```

`paddle_ocr_inference.py` 스크립트는 입력 이미지를 처리하고 인식된 텍스트를 출력합니다. 스크립트를 실행하기 전에, 입력 이미지 경로와 결과를 저장할 경로를 스크립트 내에서 설정해야 할 수 있습니다.