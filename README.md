# iSEE-AI
AI application for **iSee** project, attending [GoogleSolutionChallenge2024](https://developers.google.com/community/gdsc-solution-challenge). 

iSee aims to provide visual assitance for individuals with visual impairments. 

## TL;DR
```bash
docker build -f Dockerfile -t isee-ai-server .
docker run --rm -p 8000:8000 isee-ai-server
```

## Prerequisites
- Build by docker
    - `nvidia-container-runtime`
- Build from source
    - `conda`

## Build & Run

```bash
git clone --recursive https://github.com/GDSC-KU-SolutionChallenge-iSEE/iSEE-AI

# If already cloned,
cd iSEE-AI && git submodules update --recursive

conda env create --file environment.yaml
conda activate isee-ai
python isee-ai/server.py
```

## Development
- Designed to run on nvidia gpu environment
    - depends on `torch.cuda`

